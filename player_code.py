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
    """Print the Players Name, Top Speed, Distance, Average Speed and the Date entered"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Players.name, data.top_speed, data.distance, data.average, data.date FROM data JOIN Players ON data.player_id = Players.player_id WHERE data.player_id = ? ORDER BY SUBSTRING(data.date, 4, 2) DESC;"
    cursor.execute(sql, (id,))
    results = cursor.fetchall()
    #loop through all the results
    print("Name                Top Speed     Distance     Avg Speed     Date")
    for data in results:
        print(f"{data[0]:<20}{data[1]}{" km/hr ":<12}{data[2]}{" km ":<9}{data[3]}{" km/hr ":<11}{data[4]}")
    #loop finshed here
    db.close()

def user():
    """Print the players ID and Name out for the user to choose from"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT player_id, name FROM Players"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("\nWho's data would you like to see?")
    for data in results:
        print(f"{data[0]}{"." :<3}{data[1]}")
    print("11.  Exit")
    #loop finshed here
    db.close()

#tell them the password
print("The password is Player\n")
#generate password and check if the user is correct
werkzeug.security.generate_password_hash(password, method='pbkdf2', salt_length=16)
while True:
    password = input("Password: ")
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
    user()
    id = int(input(""))
    if id < 11:
        print_player(int(id))
    elif id == 11:
        break
    else:
        print("That was not an option!")