import mysql.connector

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

# Step 2: Show action menu
print("📌 What would you like to do?")
print("1. Update a record")
print("2. Delete records")
print("3. View top companies")
choice = input("Enter choice (1-3): ").strip()

if choice == "1":
    # UPDATE
    company = input("Enter the company name to update: ").strip()
    column = input("Which column do you want to update (e.g., HQ, Employees, Valuation): ").strip()
    new_value = input(f"Enter new value for '{column}': ").strip()

    try:
        query = f"UPDATE saas_companies SET {column} = %s WHERE Company = %s"
        cursor.execute(query, (new_value, company))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"✅ Successfully updated '{column}' for {company}.\n")
        else:
            print(f"⚠️ No matching company found: {company}\n")
    except Exception as e:
        print(f"❌ Error updating: {e}")

elif choice == "2":
    # DELETE
    year = input("Delete companies founded before which year? Enter year (e.g., 2000): ").strip()
    try:
        cursor.execute("DELETE FROM saas_companies WHERE Founded_Year < %s", (year,))
        connection.commit()
        print(f"✅ Deleted companies founded before {year}.\n")
    except Exception as e:
        print(f"❌ Error deleting: {e}")

elif choice == "3":
    # VIEW TOP COMPANIES
    try:
        cursor.execute("SELECT Company, c_rank FROM saas_companies ORDER BY c_rank LIMIT 5")
        top_companies = cursor.fetchall()
        print("\n🏆 Top 5 Companies by c_rank:")
        for company, rank in top_companies:
            print(f"🏢 {company} — Rank: {rank}")
        print()
    except Exception as e:
        print(f"❌ Error retrieving data: {e}")
else:
    print("❗ Invalid choice. Please enter 1, 2, or 3.")

# Step 3: Close connection
cursor.close()
connection.close()
print("🔒 Connection closed.")
