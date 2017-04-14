import MySQLdb
import decimal
from Database import Database
db = Database()
# Returns difficulty of trail based on distance and gain
def get_difficulty(distance, gain):
    # TODO handle null and negative input
    print str(distance) + " " + str(gain)
    dist = distance * 5280.0 # Convert from miles to feet
    d = dist / 20000
    g = gain / 2000.0
    s = (gain * 20) / dist
    difficulty = d + g + s
    return min(10.0, difficulty)

# Returns starting level of user
def get_first_lvl(weight, height, level):
    # Autoset level if invalid input
    if level > 10 or level < 0 or weight < 0 or height < 0:
        return 1
    bmi = weight / (height ** 2)
    lvl = 0.0
    if bmi > 25:
        lvl = min(level, 2.5)
    elif bmi > 30:
        lvl = 1.0
    else:
        lvl = level

    return lvl

# Updates user level after hike completed
def update_usr_lvl(usr_id, trl_id):

    # Open database
    # TODO migrate to driver file
    # db = MySQLdb.connect(host="hikeaway.crmldenzgavh.us-west-2.rds.amazonaws.com",    # your host, usually localhost
    #                      user="hikeaway",         # your username
    #                      passwd="hikeaway",  # your password
    #                      db="hikeaway")        # name of the data base
    # c = db.cursor()

    # Get levels from database
    # c.execute("SELECT skill FROM User WHERE userID = " + str(usr_id))
    usr_lvl = db.get_user(usr_id).skill
    # c.execute("SELECT difficulty FROM Trail WHERE trailID = '" + trl_id + "'")
    trail_lvl = db. get_trail_difficulty #c.fetchone()[0]
    # c.execute("SELECT liked FROM User_Hike WHERE userID = " + str(usr_id) + " AND trailID = '" + trl_id + "'")
    temp = db.get_liked_trails(usr_id, trl_id)
    if temp is None:
        liked = None
    else:
        liked = temp[0]

    if liked is not None:
        # Too easy
        if liked == -1:
            # Raise level
            if trail_lvl >= usr_lvl:
                usr_lvl = min(10.0, trail_lvl + decimal.Decimal(.5))
            else:
                usr_lvl = min(10.0, usr_lvl + decimal.Decimal(.25))

        # Too hard
        elif liked == 1:
            # Lower level
            if trail_lvl <= usr_lvl:
                usr_lvl = max(0.0, trail_lvl - decimal.Decimal(.5))
            else:
                usr_lvl = min(10, usr_lvl - decimal.Decimal(.25))

        # Perfect
        else:
            if trail_lvl > (usr_lvl + decimal.Decimal(.2)):
                usr_lvl = min(10.0, trail_lvl)
            elif trail_lvl < (usr_lvl - decimal.Decimal(.2)):
                usr_lvl = max(0.0, trail_lvl)
            else:
                usr_lvl = trail_lvl
    print usr_lvl
    db.update_user_level(usr_id, usr_lvl)
    # c.execute("UPDATE User SET skill = " + str(usr_lvl) + " WHERE userID = " + str(usr_id))

    # db.commit()
    # db.close()


update_usr_lvl(2, 'cascade-trail')
