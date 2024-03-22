import os
import sqlite3
import csv
from create_db import db_path, script_dir

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT name, age FROM people WHERE age >= 50"
    cursor.execute(query)
    old_people = cursor.fetchall()

    conn.close()
    return old_people

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    for person in name_and_age_list:
        print(f"Name: {person[0]}, Age: {person[1]}")

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age'])
        writer.writerows(name_and_age_list)

if __name__ == '__main__':
    main()
