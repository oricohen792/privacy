from flask import Flask, render_template

app = Flask(__name__)

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/delete-my-data")
def delete_my_data():
    return render_template("delete-my-data.html")

if __name__ == "__main__":
    app.run()
