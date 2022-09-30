from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.view import main_blueprint, search_blueprint
from loader.view import post_form_blueprint, uploader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/list")
def page_tag():
    pass


app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(post_form_blueprint)
app.register_blueprint(uploader_blueprint, static_url_path="/uploads", static_folder="uploads")
app.run()
