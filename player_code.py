#docstring- Zac Newman- player databse aplication
#imports
import sqlite3

#constants and variables
DATABASE = "player.db"
PASSWORD1 = "pbkdf2:sha256:600000$ZI1UeAvvyxlnqov2$8a8d9f8345109ad68e25766bb4bc7c7f52030e11643e818405bf390b1ee12e60"

#functions
def print_all_data():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM data;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("ID  Name                Top_Speed     Distance      Average")
    for data in results:
        print(f"{data[0]:<4}{data[1]:<20}{data[2]}{" km/hr":<12}{data[3]}{" km":<10}{data[4]}{" km/hr":<6}")
    #loop finshed here
    db.close()

def print_top_speed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM data ORDER BY top_speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("ID  Name                Top_Speed     Distance      Average")
    for data in results:
        print(f"{data[0]:<4}{data[1]:<20}{data[2]}{" km/hr":<12}{data[3]}{" km":<10}{data[4]}{" km/hr":<6}")
    #loop finshed here
    db.close()

def print_total_distance():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM data ORDER BY distance DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("ID  Name                Top_Speed     Distance      Average")
    for data in results:
        print(f"{data[0]:<4}{data[1]:<20}{data[2]}{" km/hr":<12}{data[3]}{" km":<10}{data[4]}{" km/hr":<6}")
    #loop finshed here
    db.close()

def print_average_speed():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM data ORDER BY average DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("ID  Name                Top_Speed     Distance      Average")
    for data in results:
        print(f"{data[0]:<4}{data[1]:<20}{data[2]}{" km/hr":<12}{data[3]}{" km":<10}{data[4]}{" km/hr":<6}")
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
    else:
        print("That was not an option!\n")