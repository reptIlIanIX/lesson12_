from flask import Blueprint, render_template, request
from functions import load_json, search_name

main_blueprint = Blueprint("maint_blueprint", __name__, template_folder='templates')
search_blueprint = Blueprint("search_blueprint", __name__, template_folder='templates')


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@search_blueprint.route('/search')
def search_page():
    s = request.args['s']
    posts = search_name(s)
    return render_template('post_list.html', posts=posts, s=s)
