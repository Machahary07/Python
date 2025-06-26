import csv
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='4529111',
    database='jeu'
)
cursor = conn.cursor()

# Create Table with 'c_rank' instead of 'Rank'
cursor.execute("""
CREATE TABLE IF NOT EXISTS saas_companies (
    c_rank INT PRIMARY KEY,
    Company VARCHAR(255),
    Founded YEAR,
    HQ VARCHAR(255),
    Industry VARCHAR(255),
    Website VARCHAR(255),
    Revenue VARCHAR(255),
    Employees VARCHAR(255)
)
""")

# Path to CSV
csv_path = r'D:\PYTHON\Datasets\d1_top_100_saas_companies_2025.csv'

# Load CSV and Insert into DB
with open(csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            cursor.execute("""
                INSERT INTO saas_companies (c_rank, Company, Founded, HQ, Industry, Website, Revenue, Employees)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE Company=VALUES(Company)
            """, (
                int(row['Rank']),
                row['Company'],
                int(row['Founded']) if row['Founded'].isdigit() else None,
                row['HQ'],
                row['Industry'],
                row['Website'],
                row['Revenue (est.)'],
                row['Employees (est.)']
            ))
        except Exception as e:
            print(f"Error inserting row: {row.get('Company', 'Unknown')} – {e}")

conn.commit()

# Data Manipulation

print("\nTop 5 Companies by c_rank:")
cursor.execute("SELECT * FROM saas_companies ORDER BY c_rank LIMIT 5")
for row in cursor.fetchall():
    print(row)

print("\nUpdating HQ of Company='Zapier' to 'Remote':")
cursor.execute("UPDATE saas_companies SET HQ='Remote' WHERE Company='Zapier'")
conn.commit()

print("\nDeleting companies founded before 2000:")
cursor.execute("DELETE FROM saas_companies WHERE Founded < 2000")
conn.commit()

# Final Query
print("\nRemaining Companies in DB:")
cursor.execute("SELECT Company, Founded FROM saas_companies")
for row in cursor.fetchall():
    print(row)

# Close DB connection
cursor.close()
conn.close()