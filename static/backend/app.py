from pickle import TRUE
from flask import *

app = Flask(__name__, template_folder="../frontend/templates")

@app.route("/")
def index():
    return render_template("breathing.html")



if __name__ == "__main__":
    app.run(debug=True)
