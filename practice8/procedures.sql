CREATE OR REPLACE PROCEDURE upsert_contact(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_contacts(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    bad_data TEXT[];
BEGIN
    FOR i IN 1..array_length(p_names,1) LOOP
        -- Проверка: телефон должен состоять только из цифр
        IF p_phones[i] ~ '^[0-9]+$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_names[i]) THEN
                UPDATE phonebook
                SET phone = p_phones[i]
                WHERE first_name = p_names[i];
            ELSE
                INSERT INTO phonebook(first_name, phone)
                VALUES (p_names[i], p_phones[i]);
            END IF;
        ELSE
            bad_data := array_append(bad_data, p_names[i] || ':' || p_phones[i]);
        END IF;
    END LOOP;

    -- Выводим некорректные данные
    IF bad_data IS NOT NULL THEN
        RAISE NOTICE 'Некорректные данные: %', bad_data;
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_value
       OR phone = p_value;

    RAISE NOTICE 'Удалены записи с именем или телефоном: %', p_value;
END;
$$;
