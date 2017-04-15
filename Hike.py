
class Hike(object):
    def __init__(self, trail_id, name, difficulty, lat, lng):
        self.trail_id = trail_id
        self.name = name
        self.difficulty = difficulty
        self.lat = lat
        self.lng = lng
class User(object):
    def __init__(self, user_id, name, skill, lat, lng):
        self.user_id = user_id
        self.name = name
        self.skill = skill
        self.lat = lat
        self.lng = lng
