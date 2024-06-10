#docstring- Zac Newman- player database application
#imports
import sqlite3
import werkzeug

#constants and variables
DATABASE = "player.db"
PASSWORD1 = "pbkdf2:sha256:600000$NxC2Y5JSlUOoRPnL$a58ab5f825032205b3487ddd25dcdfb56e194c4c930868cb4560584cf5596bd0"
attempts = 0
password = ""

#functions
def print_player(id):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Players.name, data.top_speed, data.distance, data.average, data.date FROM data JOIN Players ON data.player_id = Players.player_id WHERE data.player_id = ?;"
    cursor.execute(sql, (id,))
    results = cursor.fetchall()
    #loop through all the results
    print("Name                Top Speed     Distance     Avg Speed     Date")
    for data in results:
        print(f"{data[0]:<20}{data[1]}{" km/hr ":<12}{data[2]}{" km ":<9}{data[3]}{" km/hr ":<11}{data[4]}")
    #loop finshed here
    db.close()


#tell them the password
print("The password is Player\n")
werkzeug.security.generate_password_hash(password, method='pbkdf2', salt_length=16)
while True:
    password = input("Password: ")
    #check if passwords correct
    if werkzeug.security.check_password_hash(PASSWORD1, password) == False:
        #count tried attempts
        attempts += 1
        if attempts == 1:
            print("That was incorrect!")
        if attempts == 2:
            print("One last attempt!")
        if attempts >= 3:
            exit()
    else:
        break



while True:
    user_input = input(
"""
Who's data would you like to see?
1.  John Smith
2.  Micheal Brown
3.  David Johnson
4.  James Wilson
5.  William Lee
6.  Benjamin Wang
7.  James Newman
8.  Mathew James
9.  Ethan Donaldson
10. Daniel Davis
11. Exit
"""
    )
    if user_input != "11":
        print_player(int(user_input))
    elif user_input == "11":
        break
    else:
        print("That was not an option!\n")