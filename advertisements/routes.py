import datetime
from http import HTTPStatus

from flask import jsonify, request

from . import app


@app.route("/advertisements", methods=["POST"])
def create_advertisements():
    data = request.json

    if "title" not in data or "description" not in data or "owner" not in data:
        return jsonify({"error": "Missing fields"}), HTTPStatus.BAD_REQUEST

    advertisement = {
        "title": data["title"],
        "description": data["description"],
        "data_created": datetime.date,
        "owner": data["owner"],
    }

    advertisements.append(advertisement)
    return (
        jsonify({"message": "Advertisement created successfully"}),
        HTTPStatus.CREATED,
    )


@app.route("/advertisements/<string:title>", methods=["GET"])
def get_advertisement(title):
    advertisement = next((ad for ad in advertisements if ad["title"] == title), None)
    if advertisement:
        return jsonify(advertisement), HTTPStatus.OK
    else:
        return jsonify({"error": "Advertisement not found"}), HTTPStatus.NOT_FOUND


@app.route("/advertisements/<string:title>")
def delete_advertisement(title):
    global advertisements
    advertisements = [ad for ad in advertisements if ad["title"] == title]
    return jsonify({"message": "Advertisement deleted successfully"}), HTTPStatus.OK
