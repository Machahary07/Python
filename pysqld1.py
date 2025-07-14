import mysql.connector
import csv

# Step 1: Connect to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4529111",
        database="jeu"
    )
    cursor = connection.cursor()
    print("✅ Connected to MySQL database.\n")
except mysql.connector.Error as err:
    print(f"❌ Database connection failed: {err}")
    exit()

# Step 2: Insert from CSV (Auto – no prompt)
csv_path = r"D:\PYTHON\Datasets\d1.csv"
try:
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("📄 Reading CSV:", csv_path)
        print("✅ CSV Headers:", reader.fieldnames)

        for row in reader:
            try:
                cursor.execute("""
                    INSERT INTO saas_companies 
                    (Company, Founded_Year, HQ, Industry, Total_Funding, ARR, Valuation, Employees, Top_Investors, Product, G2_Rating, c_rank)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    row['Company Name'], row['Founded Year'], row['HQ'], row['Industry'],
                    row['Total Funding'], row['ARR'], row['Valuation'], row['Employees'],
                    row['Top Investors'], row['Product'], row['G2 Rating'], row['c_rank']
                ))
            except Exception as e:
                print(f"❌ Error inserting row ({row.get('Company Name', 'Unknown')}): {e}")
        connection.commit()
        print("✅ All CSV data inserted.\n")
except FileNotFoundError:
    print("❌ CSV file not found at:", csv_path)

# Step 3: Choose Action
print("📌 Choose an action:")
print("1. Update a record")
print("2. Delete old companies")
print("3. View top 5 companies by c_rank")
choice = input("Enter choice (1-3): ").strip()

if choice == "1":
    company = input("🔧 Enter company name to update: ").strip()
    column = input("📝 Column to update (e.g., HQ, Employees, Valuation): ").strip()
    new_value = input(f"💡 New value for {column}: ").strip()
    try:
        cursor.execute(f"UPDATE saas_companies SET {column} = %s WHERE Company = %s", (new_value, company))
        connection.commit()
        print(f"✅ Updated {column} for {company}.\n")
    except Exception as e:
        print(f"❌ Update error: {e}")

elif choice == "2":
    year = input("🗑️ Delete companies founded before year (e.g., 2000): ").strip()
    try:
        cursor.execute("DELETE FROM saas_companies WHERE Founded_Year < %s", (year,))
        connection.commit()
        print(f"✅ Deleted companies founded before {year}.\n")
    except Exception as e:
        print(f"❌ Deletion error: {e}")

elif choice == "3":
    try:
        cursor.execute("SELECT * FROM saas_companies ORDER BY c_rank LIMIT 5")
        top_companies = cursor.fetchall()
        print("\n🏆 Top 5 Companies by c_rank:")
        for row in top_companies:
            print(row)
        print()
    except Exception as e:
        print(f"❌ Retrieval error: {e}")

else:
    print("❗ Invalid choice.")

# Step 4: Close connection
cursor.close()
connection.close()
print("🔒 Connection closed.")
