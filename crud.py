import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="G369"
)

mycursor = mydb.cursor()

# Create database (if it doesn't exist)
mycursor.execute("CREATE DATABASE IF NOT EXISTS my_database")

# Use the database
mycursor.execute("USE my_database")

# Create a table (if it doesn't exist)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE
)
""")

# Insert data (replace with your data)
def insert(name,email):
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql, val)

# Commit changes
    mydb.commit()

    print("Database and table created, data inserted successfully!")

# Close connection
    mydb.close()


def read(table):

      mycursor.execute("SELECT * FROM "+table)
      myresult = mycursor.fetchall()

# Print results
      for row in myresult:
          print(row)
      
      mydb.close()

# Close connection (same as Create)


def update(id,email):
     sql = "UPDATE users SET email = %s WHERE id = %s"
     val = (email, id)  
     mycursor.execute(sql, val)

     print("User email updated successfully!")
     mydb.close()




def delete():
     sql = "DELETE FROM users WHERE id = 1"
      
     mycursor.execute(sql)



     print("User deleted successfully!")
     mydb.close()


#insert()
delete()

