from flask import Flask
from app.extensions import mongo
from app.webhook.routes import webhook
from flask_cors import CORS


# Creating our flask app
def create_app():
    app = Flask(__name__)

    # registering all the blueprints
    app.register_blueprint(webhook)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/database"
    mongo.init_app(app)
    CORS(app)
    return app
