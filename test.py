from flask import Flask, jsonify
from flask_restful import Resource, Api
from HikeBuddy import HikeBuddy

app = Flask(__name__)
api = Api(app)

class hike(Resource):
    # @app.route('/todo/api/v1.0/tasks', methods=['GET'])
    def get(self):
        hb = HikeBuddy()
        tasks = hb.find_suggestions()
        return jsonify({'tasks': tasks})
api.add_resource(hike, '/todo/api/v1.0/tasks')
if __name__ == '__main__':
    app.run(debug=True)
