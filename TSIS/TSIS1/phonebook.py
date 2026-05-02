import psycopg2, json, csv
from connect import get_connection

def filter_by_group(group_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.first_name, c.email, c.birthday, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name ILIKE %s
    """, (group_name,))
    rows = cur.fetchall()
    if not rows:
        print("Нет контактов в этой группе.")
    else:
        for row in rows:
            print(row)
    conn.close()

def search_by_email(pattern):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT first_name, email FROM contacts WHERE email ILIKE %s", ('%' + pattern + '%',))
    for row in cur.fetchall():
        print(row)
    conn.close()

def sort_contacts(field):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT first_name, email, birthday, created_at FROM contacts ORDER BY {field}")
    for row in cur.fetchall():
        print(row)
    conn.close()

def paginate_contacts():
    conn = get_connection()
    cur = conn.cursor()
    page, limit = 0, 2
    while True:
        cur.execute("SELECT first_name, email FROM contacts ORDER BY id LIMIT %s OFFSET %s", (limit, page * limit))
        rows = cur.fetchall()
        if not rows:
            print("Нет данных.")
        else:
            for r in rows: print(r)
        cmd = input("next/prev/quit: ")
        if cmd == "next": page += 1
        elif cmd == "prev" and page > 0: page -= 1
        elif cmd == "quit": break
    conn.close()

def export_json(filename="contacts.json"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.first_name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)
    data = []
    for row in cur.fetchall():
        data.append({
            "name": row[0], "email": row[1], "birthday": str(row[2]),
            "group": row[3], "phone": row[4], "type": row[5]
        })
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    conn.close()

def import_json(filename="contacts.json"):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    for contact in data:
        cur.execute("SELECT id FROM contacts WHERE first_name=%s", (contact["name"],))
        existing = cur.fetchone()
        if existing:
            choice = input(f"Contact {contact['name']} exists. Overwrite? (y/n): ")
            if choice.lower() == "y":
                cur.execute("UPDATE contacts SET email=%s, birthday=%s WHERE id=%s",
                            (contact["email"], contact["birthday"], existing[0]))
        else:
            cur.execute("INSERT INTO contacts(first_name,email,birthday) VALUES (%s,%s,%s)",
                        (contact["name"], contact["email"], contact["birthday"]))
    conn.commit()
    conn.close()

def import_csv(filename="contacts.csv"):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("INSERT INTO contacts(first_name,email,birthday) VALUES (%s,%s,%s)",
                        (row["name"], row["email"], row["birthday"]))
    conn.commit()
    conn.close()

def main():
    while True:
        print("1. Filter by group\n2. Search by email\n3. Sort\n4. Paginate\n5. Export JSON\n6. Import JSON\n7. Import CSV\n0. Quit")
        choice = input("Select: ")
        if choice == "1": filter_by_group(input("Group: "))
        elif choice == "2": search_by_email(input("Email pattern: "))
        elif choice == "3": sort_contacts(input("Sort by (first_name,birthday,created_at): "))
        elif choice == "4": paginate_contacts()
        elif choice == "5": export_json()
        elif choice == "6": import_json()
        elif choice == "7": import_csv()
        elif choice == "0": break

if __name__ == "__main__":
    main()
