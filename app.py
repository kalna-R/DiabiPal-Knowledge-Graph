import re

from flask import Flask, request
from correction import post_process
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


# from autocorrect import Speller
# import spacy
# from spacy.matcher import Matcher
# import en_core_web_sm
#
# nlp = en_core_web_sm.load()
#
# # nlp = spacy.load('en_core_web_sm')
# matcher = Matcher(nlp.vocab)
# @app.route('/spell')
# def hey():
#     spell = Speller()
#     return spell('court')


@app.route('/corrections', methods=["POST"])
def post_processing():
    # skip the content requirement by force=True
    data = request.get_json(force=True)

    corrected_array = post_process(data)

    return corrected_array


if __name__ == '__main__':
    app.run(port=3000)
