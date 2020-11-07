import pymysql as sql

def connect_to_database():
	connection = pymysql.connect(
		host="localhost",
        port=33066
		user="root",
		passwd="password",
		database="Brew"
	)
	cursor = connection.cursor()
	# cursor.execute("INSERT INTO drink (id, name, type, temp) VALUES (%s, %s, %s, %s)", args)
	connection.commit()
	cursor.close()
	connection.close()

# import pymysql as sql

# def connect_database():
#     connection = sql.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "Brew")
#     cursor = connection.cursor()
#     #cursor.execute("SELECT drinkID FROM Drinks")
#     cursor.execute('SELECT IF(500<1000, "TRUE", "FALSE")')
#     connection.commit()
#     rows = cursor.fetchall()
#     cursor.close()
#     connection.close()
    
#     for row in rows:
#         print(row)

#     print("rows")
#     return