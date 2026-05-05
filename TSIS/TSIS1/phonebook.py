from datetime import datetime
from connect import connect

conn = connect()
cursor = conn.cursor()


def init_db():
    with open("TSIS/TSIS1/schema.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    for statement in sql.split(";"):
        if statement.strip():
            cursor.execute(statement)

    conn.commit()

init_db()

def get_group_id(group_name: str):
    if not group_name:
        return None
    cursor.execute("SELECT id FROM groups WHERE name ILIKE %s", (group_name,))
    row = cursor.fetchone()
    return row[0] if row else None


def parse_date(date_str: str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date:", date_str)
        return None


def reading_from_console():
    name       = input("Name: ").strip()
    phone      = input("Phone: ").strip()
    phone_type = input("Type (home/work/mobile) [mobile]: ").strip().lower() or 'mobile'

    if phone_type not in ("home", "work", "mobile"):
        phone_type = "mobile"

    email      = input("Email (optional): ").strip() or None
    birthday   = parse_date(input("Birthday YYYY-MM-DD (optional): ").strip())
    group_name = input("Group (Family/Work/Friend/Other): ").strip()
    group_id   = get_group_id(group_name)

    cursor.execute(
        "INSERT INTO contacts (name, email, birthday, group_id) "
        "VALUES (%s, %s, %s, %s) RETURNING id",
        (name, email, birthday, group_id)
    )
    contact_id = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
        (contact_id, phone, phone_type)
    )

    conn.commit()
    print("Added")


def update_contact(contact_id, email=None, birthday=None, group_name=None):
    updates, params = [], []

    if email is not None:
        updates.append("email = %s")
        params.append(email)

    if birthday is not None:
        updates.append("birthday = %s")
        params.append(parse_date(birthday))

    if group_name is not None:
        updates.append("group_id = %s")
        params.append(get_group_id(group_name))

    if not updates:
        print("Nothing to update")
        return

    params.append(contact_id)

    cursor.execute(
        f"UPDATE contacts SET {', '.join(updates)} WHERE id = %s",
        params
    )
    conn.commit()
    print("Updated")


def update_phone(contact_id, old_phone, new_phone):
    cursor.execute(
        "UPDATE phones SET phone = %s WHERE contact_id = %s AND phone = %s",
        (new_phone, contact_id, old_phone)
    )
    conn.commit()
    print("Phone updated")


def filtering(name=None, phone_prefix=None, group_name=None, email=None):
    query = '''
        SELECT c.id, c.name, c.email, c.birthday, g.name,
               p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        LEFT JOIN phones p ON p.contact_id = c.id
        WHERE 1=1
    '''
    params = []

    if name:
        query += " AND c.name ILIKE %s"
        params.append(f"%{name}%")

    if phone_prefix:
        query += " AND p.phone LIKE %s"
        params.append(f"{phone_prefix}%")

    if group_name:
        query += " AND g.name ILIKE %s"
        params.append(f"%{group_name}%")

    if email:
        query += " AND c.email ILIKE %s"
        params.append(f"%{email}%")

    cursor.execute(query, params)

    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found")


def delete_by_name(name):
    cursor.execute("DELETE FROM contacts WHERE name = %s", (name,))
    conn.commit()
    print("Deleted" if cursor.rowcount else "Not found")


def delete_phone(phone):
    cursor.execute("DELETE FROM phones WHERE phone = %s", (phone,))
    conn.commit()
    print("Phone deleted" if cursor.rowcount else "Not found")


if __name__ == "__main__":
    init_db()

    while True:
        print("""
1. Filter by group
2. Search by email
3. Sort (по имени)
4. Paginate
5. Export JSON
6. Import JSON
7. Import CSV
0. Quit
""")

        choice = input("Select: ")

        if choice == "1":
            group = input("Введите группу: ")
            filtering(group_name=group)

        elif choice == "2":
            email = input("Введите email: ")
            filtering(email=email)

        elif choice == "3":
            # простая сортировка по имени
            cursor.execute("SELECT * FROM contacts ORDER BY name")
            for row in cursor.fetchall():
                print(row)

        elif choice == "4":
            limit = int(input("Сколько контактов на страницу: "))
            offset = int(input("Смещение (offset): "))
            cursor.execute("SELECT * FROM contacts ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
            for row in cursor.fetchall():
                print(row)

        elif choice == "5":
            from import_export import export_to_json
            export_to_json()

        elif choice == "6":
            from import_export import reading_csv
            path = input("Введите путь к JSON: ")
            # тут можно сделать импорт из JSON, если реализовано
            print("Импорт JSON пока не реализован")

        elif choice == "7":
            from import_export import reading_csv
            path = input("Введите путь к CSV: ")
            reading_csv(path)

        elif choice == "0":
            break

    cursor.close()
    conn.close()
