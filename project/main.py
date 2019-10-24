from flask import Blueprint
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Returning index @main index route'

@main.route('/profile')
def profile():
    return 'Returning profile @main profile route'


