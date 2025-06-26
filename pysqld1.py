import mysql.connector
import csv

# Step 1: Connect to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # change if needed
        database="saas"
    )
    cursor = connection.cursor()
    print("✅ Connected to MySQL database.\n")
except mysql.connector.Error as err:
    print(f"❌ Database connection failed: {err}")
    exit()

# Step 2: Ask for action
print("📌 What would you like to do?")
print("1. Insert data from CSV")
print("2. Update a record")
print("3. Delete records")
print("4. View top companies")
choice = input("Enter choice (1-4): ").strip()

if choice == "1":
    # INSERT from CSV
    csv_file = input("Enter CSV filename (with .csv extension): ").strip()
    try:
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
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
                    print(f"❌ Error inserting row: {row.get('Company Name', 'Unknown')} – {e}")
            connection.commit()
            print("✅ Data inserted successfully.\n")
    except FileNotFoundError:
        print("❌ CSV file not found.\n")

elif choice == "2":
    # UPDATE
    company = input("Enter the company name to update: ").strip()
    column = input("Which column do you want to update (e.g., HQ, Employees, Valuation): ").strip()
    new_value = input(f"Enter new value for {column}: ").strip()

    try:
        cursor.execute(f"UPDATE saas_companies SET {column} = %s WHERE Company = %s", (new_value, company))
        connection.commit()
        print(f"✅ Updated {column} for {company}.\n")
    except Exception as e:
        print(f"❌ Error updating: {e}")

elif choice == "3":
    # DELETE
    year = input("Delete companies founded before which year? Enter year (e.g., 2000): ").strip()
    try:
        cursor.execute("DELETE FROM saas_companies WHERE Founded_Year < %s", (year,))
        connection.commit()
        print(f"✅ Deleted companies founded before {year}.\n")
    except Exception as e:
        print(f"❌ Error deleting: {e}")

elif choice == "4":
    # VIEW
    try:
        cursor.execute("SELECT * FROM saas_companies ORDER BY c_rank LIMIT 5")
        top_companies = cursor.fetchall()
        print("\n🏆 Top 5 Companies by c_rank:")
        for row in top_companies:
            print(row)
        print()
    except Exception as e:
        print(f"❌ Error retrieving data: {e}")
else:
    print("❗ Invalid choice. Please enter 1, 2, 3, or 4.")

# Step 3: Close connection
cursor.close()
connection.close()
print("🔒 Connection closed.")