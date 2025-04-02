import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SHOW COLUMNS FROM subscribers")
columns = [col[0] for col in cursor.fetchall()]

# Check if subscription_date column exists
assert "subscription_date" in columns, "❌ subscription_date column missing!"
print("✅ subscription_date column exists. Schema is correct.")

cursor.close()
conn.close()
