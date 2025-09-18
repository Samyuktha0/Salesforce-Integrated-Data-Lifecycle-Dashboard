from flask import Flask
from routes import dashboard

app = Flask(__name__)
app.register_blueprint(dashboard)

if __name__ == "__main__":
    app.run(debug=True)
