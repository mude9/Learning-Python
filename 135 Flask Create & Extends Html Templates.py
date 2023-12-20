# ----------------------------------------------
# -- Flask => Create & Extends Html Templates --
# ----------------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage.html", pagetitle="Homepage", cssfile="home")

@skills_app.route("/about")
def about():
  return render_template("about.html", pagetitle="About Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)