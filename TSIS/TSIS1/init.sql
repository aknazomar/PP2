INSERT INTO groups(name) VALUES ('Work'), ('Family'), ('Friend'), ('Other');

INSERT INTO contacts(first_name, email, birthday, group_id)
VALUES 
('Aknaz', 'aknaz@gmail.com', '2002-05-15', (SELECT id FROM groups WHERE name='Friend')),
('John Doe', 'john.doe@work.com', '1990-03-10', (SELECT id FROM groups WHERE name='Work')),
('Jane Smith', 'jane.smith@yahoo.com', '1985-07-20', (SELECT id FROM groups WHERE name='Family'));

INSERT INTO phones(contact_id, phone, type)
VALUES 
((SELECT id FROM contacts WHERE first_name='Aknaz'), '87071112233', 'mobile'),
((SELECT id FROM contacts WHERE first_name='John Doe'), '87075554433', 'work'),
((SELECT id FROM contacts WHERE first_name='Jane Smith'), '87079998877', 'home');
