from app import app

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello World, Part 2"

