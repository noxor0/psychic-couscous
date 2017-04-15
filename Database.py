import MySQLdb
import json
from decimal import Decimal
from Hike import Hike, User
class Database(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="hikeaway.crmldenzgavh.us-west-2.rds.amazonaws.com",    # your host, usually localhost
                                    user="hikeaway",         # your username
                                    passwd="hikeaway",  # your password
                                    db="hikeaway")        # name of the data base

        self.cursor = self.conn.cursor()
    def close(self):
        self.conn.close()
        self.cursor.close()
    def add_trails(self):
        with open('hikes.json') as data_file:
            data = json.load(data_file)
        for trail in data:
            try:
                distance = float(trail['length'])
                lat = float(trail['lat'])
                lng = float(trail['lng'])
                if trail['elevGain'] is None:
                    gain = 0
                else:
                    gain = float(trail['elevGain'])
                diff = self.get_difficulty(distance, gain)
                sql = """INSERT INTO Trail(trailID, trailName, difficulty, lat, lng) VALUES ('%s', "%s", '%3.1f', '%7.4f', '%7.4f')""" % (trail['id'], trail['name'], diff, lat, lng)
                print sql
                try:
                    self.cursor.execute(sql)
                    self.conn.commit()
                except:
                    self.conn.rollback()
            except:
                pass
        self.conn.close()

    def get_difficulty(self, distance, gain):
        print str(distance) + " " + str(gain)
        dist = distance * 5280.0 # Convert from miles to feet
        d = dist / 20000
        g = gain / 2000.0
        s = (gain * 20) / dist
        difficulty = d + g + s
        return min(10.0, difficulty)

    def get_hikes(self, user_id=1):
        hikes = []
        self.cursor.execute("SELECT trailID, trailName, difficulty, lat, lng \
                            FROM Trail t WHERE trailID NOT IN (SELECT trailID FROM User_Hike WHERE userID = %d);" % (user_id))
        result = self.cursor.fetchall()
        for hike in result:
            temp = Hike(hike[0], hike[1], hike[2], hike[3], hike[4])
            hikes.append(temp)

        return hikes

    def get_hike_frequency(self, user_id=1):
        trailSet = set()
        self.cursor.execute("SELECT trailID, COUNT(trailID) FROM User_Hike GROUP BY trailID")
        result = self.cursor.fetchall()
        for trailTuple in result:
            trailSet.add(trailTuple)
        return trailSet

    def get_user(self, user_id=1):
        self.cursor.execute("SELECT * FROM User WHERE userID = %d" % (user_id))
        temp = self.cursor.fetchone()
        return User(temp[0], temp[1], temp[2], temp[3], temp [4])

    def add_user_hike(self, user_id, trail_id, liked=None):
        self.cursor.execute("INSERT INTO User_Hike(userID, trailID)\
                             VALUES ('%s', '%s')" % (user_id, trail_id))
        self.conn.commit()

    def get_trail_difficulty(self, trail_id):
        self.cursor.execute("SELECT difficulty FROM Trail WHERE trailID = '" + trail_id + "'")
        return self.cursor.fetchone()[0]

    def get_liked_trails(self, user_id, trail_id):
        self.cursor.execute("SELECT liked FROM User_Hike WHERE userID = " + str(user_id) + " AND trailID = '" + trail_id + "'")
        return self.cursor.fetchone()[0]

    def update_user_level(self, user_id, user_skill):
        self.cursor.execute("UPDATE User SET skill = " + str(user_skill) + " WHERE userID = " + str(user_id))

        self.conn.commit()
    def update_user_hike(self, user_id, trail_id, liked):
        self.cursor.execute("UPDATE User_Hike SET liked = " + str(liked) + " WHERE userID = " + str(user_id)+ " AND trailID = '" + trail_id + "'")

        self.conn.commit()

    def update_usr_lvl(self, usr_id, trl_id):

        # Open database
        # TODO migrate to driver file
        # db = MySQLdb.connect(host="hikeaway.crmldenzgavh.us-west-2.rds.amazonaws.com",    # your host, usually localhost
        #                      user="hikeaway",         # your username
        #                      passwd="hikeaway",  # your password
        #                      db="hikeaway")        # name of the data base
        # c = db.cursor()

        # Get levels from database
        # c.execute("SELECT skill FROM User WHERE userID = " + str(usr_id))
        usr_lvl = self.get_user(usr_id).skill
        # c.execute("SELECT difficulty FROM Trail WHERE trailID = '" + trl_id + "'")
        trail_lvl = self.get_trail_difficulty(trl_id) #c.fetchone()[0]
        # c.execute("SELECT liked FROM User_Hike WHERE userID = " + str(usr_id) + " AND trailID = '" + trl_id + "'")
        temp = self.get_liked_trails(usr_id, trl_id)
        if temp is None:
            liked = None
        else:
            liked = temp

        if liked is not None:
            # Too easy
            if liked == -1:
                # Raise level
                if trail_lvl >= usr_lvl:
                    usr_lvl = min(10.0, trail_lvl + Decimal(.5))
                else:
                    usr_lvl = min(10.0, usr_lvl + Decimal(.25))

            # Too hard
            elif liked == 1:
                # Lower level
                if trail_lvl <= usr_lvl:
                    usr_lvl = max(0.0, trail_lvl - Decimal(.5))
                else:
                    usr_lvl = max(0.0, usr_lvl - Decimal(.25))

            # Perfect
            else:
                if trail_lvl > (usr_lvl + Decimal(.2)):
                    usr_lvl = min(10.0, trail_lvl)
                elif trail_lvl < (usr_lvl - Decimal(.2)):
                    usr_lvl = max(0.0, trail_lvl)
                else:
                    usr_lvl = trail_lvlhi

        self.update_user_level(usr_id, usr_lvl)
        # c.execute("UPDATE User SET skill = " + str(usr_lvl) + " WHERE userID = " + str(usr_id))

        # db.commit()
        # db.close()
