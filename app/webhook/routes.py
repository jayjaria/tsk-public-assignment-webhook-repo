from flask import Blueprint, request, json
from app.extensions import mongo
from bson import json_util

webhook = Blueprint("Webhook", __name__, url_prefix="/webhook")


@webhook.route("/receiver", methods=["POST"])
def receiver():
    mongo.db.webhook.insert_one(request.json)
    return {}, 200


@webhook.route("/get_all_messages", methods=["GET"])
def get_msgs():
    msgs = mongo.db.webhook.find()
    return json.loads(json_util.dumps(msgs))
