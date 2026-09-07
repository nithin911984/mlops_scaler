from flask import Flask


app = Flask(__name__) # app is now a Flask application instance
<<<<<<< HEAD
# __name__ points the app to the current file - simple_app.py
=======
# __name__ points the app to the current file 
>>>>>>> a15694a9f1680cfc41f3fa573beb8025217ce988

#decorator
@app.route("/hello", methods=["GET"])
def hello():
    return "Hello from Flask!"

# click on run
if __name__ == "__main__":
    app.run(debug=True)