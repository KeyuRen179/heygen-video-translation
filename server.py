from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

DELAY = 10
ERROR_PROBABILITY = 0.1
start_time = time.time()

@app.route('/status', methods=['GET'])
def status():
    elapsed_time = time.time() - start_time
    if elapsed_time < DELAY:
        return jsonify({"result": "pending"})
    if random.random() < ERROR_PROBABILITY:
        return jsonify({"result": "error"})
    return jsonify({"result": "completed"})

if __name__ == '__main__':
    app.run(port=5000)
