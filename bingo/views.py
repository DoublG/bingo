from flask import current_app, Blueprint, render_template
import json
from flask import current_app, Blueprint, render_template, redirect, request
from nltk.corpus import stopwords
import nltk
from collections import defaultdict
from random import choices

main = Blueprint('main', __name__,)

def get_distribution():
    with open('data/sessions.json', 'r') as f:
        data = json.load(f)
        complete_list = []
        for i in data.get('sectionList'):
            for item in i.get('items'):
                abstract_words = nltk.word_tokenize(item.get('abstract'), language='english', preserve_line=False) + nltk.word_tokenize(item.get('title'), language='english', preserve_line=False)
                filtered_sentence = [w.lower() for w in abstract_words if not w.lower() in stopwords.words('english') and w.isalpha()]
                complete_list.extend(filtered_sentence)

        return nltk.FreqDist(complete_list)        
         


@main.route('/', methods=('GET', 'POST'))
def index():
    print(current_app.config)
    if request.method == 'POST':
        return random(5)
    else:
        distribution = get_distribution()

        d = defaultdict(list)
        for item in distribution.items():
            d[item[1]].append(item[0])

        return render_template('welcome.html', words=sorted([{ 'count': t[0], 'words':  t[1] } for t in d.items()], key=lambda x: x['count'], reverse=True))
 
@main.route('/random/<int:k>')
def random(k):
    distribution = get_distribution()
    values = list(distribution.keys()) 
    weights = list(distribution.values())
    
    division = max(weights)
    norm_weights = [(division - float(i))/division for i in weights]
    print(norm_weights)

    words = choices(values, weights=norm_weights, k = k)
    print(words)

    return render_template('bingo.html', words=words)
 