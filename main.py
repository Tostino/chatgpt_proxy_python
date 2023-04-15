from flask import Flask
from config import host, port
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True, load_dotenv=True)
