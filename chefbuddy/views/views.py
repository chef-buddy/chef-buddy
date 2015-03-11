from flask import Blueprint, flash, render_template

from .users import require_login, recipe


repos = Blueprint("repos", __name__)


@repos.route("/")
@require_login
def index():
    resp = github.get("/user/repos")
    return render_template("index.html", repos=resp.data)
