#docstring- Zac Newman- player database application
#imports
import sqlite3
import werkzeug

#constants and variables
DATABASE = "player.db"
test = 2
#functions
def John_Smith():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Players.name, data.top_speed, data.distance, data.average, data.date FROM data JOIN Players ON data.player_id = Players.player_id WHERE data.player_id = (?);", (test)
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                Top Speed     Distance     Avg Speed     Date")
    for data in results:
        print(f"{data[0]:<20}{data[1]}{" km/hr ":<12}{data[2]}{" km ":<9}{data[3]}{" km/hr ":<11}{data[4]}")
    #loop finshed here
    db.close()

#printing
John_Smith()