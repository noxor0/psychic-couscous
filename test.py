from flask import Flask, jsonify
from HikeBuddy import HikeBuddy

app = Flask(__name__)
hb = HikeBuddy()
tasks = hb.find_suggestions()

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
