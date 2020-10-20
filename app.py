import re

from flask import Flask, request

from correction import post_process

# from autocorrect import Speller

import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
app = Flask(__name__)


@app.route('/hey')
def process_array():
    ocr_array = '{FBS]'

    only_string = " ".join(re.findall('[a-zA-Z]+', ocr_array))
    print(only_string)

    return ocr_array


# @app.route('/hey')
# def hey():
#     spell = Speller()
#     return spell('{fbs]')


@app.route('/corrections', methods=["POST"])
def post_processing():
    # skip the content requirement by force=True
    data = request.get_json(force=True)

    corrected_array = post_process(data)

    return corrected_array


if __name__ == '__main__':
    app.run(port=3000)
