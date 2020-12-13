import json
import re

from flask import Flask, request
from correction import post_process
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/corrections', methods=["POST"])
def post_processing():
    # skip the content requirement by force=True
    data = request.get_json(force=True)

    corrected_array = post_process(data)

    return json.dumps(corrected_array)


if __name__ == '__main__':
    # app.run(debug="true", port=3000)
    app.run(debug=True)
