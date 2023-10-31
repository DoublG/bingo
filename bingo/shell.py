import json
from flask import current_app, Blueprint, render_template
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

com = Blueprint('load', __name__)

@com.cli.command("sessions")
def load_sessions():
    ps = PorterStemmer()
    with open('data/sessions.json', 'r') as f:
        data = json.load(f)
        for i in data.get('sectionList'):
            for item in i.get('items'):
                words = nltk.word_tokenize(item.get('abstract'))
                for word in words:
                    print(word)
                    print(ps.stem(word))
                #db.session.add(Session(title=item.get('title'), abstract=))
                #db.session.commit()