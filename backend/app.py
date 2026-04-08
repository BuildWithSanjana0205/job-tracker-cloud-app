from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

jobs = []

@app.route('/jobs', methods=['GET'])
def get_jobs():
    return jsonify({"jobs": jobs})

@app.route('/jobs', methods=['POST'])
def add_job():
    data = request.get_json()

    job = {
        "company": data.get("company"),
        "role": data.get("role")
    }

    jobs.append(job)

    return jsonify({"message": "Job added", "job": job})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
