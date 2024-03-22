import os
import sqlite3
from faker import Faker

# Social Network Database Path
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

# Main Function
def main():
    create_people_table()
    populate_people_table()

# Create People Table Function
def create_people_table():
    """Create the people table in the database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    create_people_query = """
        CREATE TABLE IF NOT EXISTS people
        (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE
        );
    """
    cursor.execute(create_people_query)
    conn.commit()
    conn.close()

# Populate People Table Function
def populate_people_table():
    """Populate the people table with 200 fake people"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    fake = Faker()

    for _ in range(100):
        name = fake.name()
        age = fake.random_int(min=18, max=90)
        email = fake.email()

        insert_person_query = "INSERT INTO people (name, age, email) VALUES (?, ?, ?)"
        cursor.execute(insert_person_query, (name, age, email))

    conn.commit()
    conn.close()

# Entry Point
if __name__ == '__main__':
    main()
