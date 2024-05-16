#docstring- Zac Newman- player databse aplication
#imports
import sqlite3

#constants and variables
DATABASE = "player.db"

#functions
def print_all_data():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM data;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("ID  Name                Top_Speed  Distance  Average")
    for data in results:
        print(f"{data[0]:<4}{data[1]:<20}{data[2]:<11}{data[3]:<10}{data[4]:<6}")
    #loop finshed here
    db.close()

def print_top_speed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM data ORDER BY top_speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("ID  Name                Top_Speed  Distance  Average")
    for data in results:
        print(f"{data[0]:<4}{data[1]:<20}{data[2]:<11}{data[3]:<10}{data[4]:<6}")
    #loop finshed here
    db.close()

def print_total_distance():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM data ORDER BY distance DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("ID  Name                Top_Speed  Distance  Average")
    for data in results:
        print(f"{data[0]:<4}{data[1]:<20}{data[2]:<11}{data[3]:<10}{data[4]:<6}")
    #loop finshed here
    db.close()

def print_average_speed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM data ORDER BY average DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("ID  Name                Top_Speed  Distance  Average")
    for data in results:
        print(f"{data[0]:<4}{data[1]:<20}{data[2]:<11}{data[3]:<10}{data[4]:<6}")
    #loop finshed here
    db.close()
while True:
    user_input = input(
"""
What would you like to do?
1. Print all players data
2. Print top speed
3. Print distance
4. Print average speed
5. Exit
"""
    )
    try:
        if user_input == "1":
            print_all_data()
        elif user_input == "2":
            print_top_speed()
        elif user_input == "3":
            print_total_distance()
        elif user_input == "4":
            print_average_speed()
        elif user_input == "5":
            break
    except ValueError:
        print("That was not an option!\n")