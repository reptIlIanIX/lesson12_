from flask import Blueprint, render_template, request, send_from_directory, jsonify

from functions import post_save
from loader.util import save_picture

post_form_blueprint = Blueprint("post_form_blueprint", __name__, template_folder='templates')
uploader_blueprint = Blueprint("uploader_blueprint", __name__, template_folder='templates')


@post_form_blueprint.route("/post")
def page_post_form():
    return render_template('post_form.html')


@uploader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    content = request.form.get('content')
    picture = request.files.get('picture')
    if not picture or not content:
        return "Нет картинки, нет текста "
    picture_path: str = save_picture(picture)
    post = post_save({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
