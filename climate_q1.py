import matplotlib.pyplot as plt
import sqlite3  # Import the appropriate library for your database

# Connect to the database
conn = sqlite3.connect("climate.db")
cursor = conn.cursor()

# Write and execute an SQL query to fetch data
query = "SELECT Year, CO2, Temperature FROM ClimateData"
cursor.execute(query)

# Fetch all the rows from the query result
data = cursor.fetchall()

years = []
co2 = []
temp = []


# Populate the lists with data from the database
for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")



# Close the database connection
conn.close()