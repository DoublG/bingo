from flask import current_app, Blueprint, render_template
main = Blueprint('main', __name__,)

@main.route('/')
def index():
    return render_template('welcome.html' )

@main.route('/load_data')
def load():
    return 'Load Data' 


@main.route('/get_file')
def get_file():
    return 'Load Data'   