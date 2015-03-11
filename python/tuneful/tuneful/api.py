import json

from flask import request, Response, url_for, send_from_directory
from werkzeug.utils import secure_filename
from jsonschema import validate, ValidationError

import models
import decorators
from tuneful import app
from database import session
from utils import upload_path


# JSON Schema describing the structure of a song
song_schema = {
    "type": "object",
    "properties": {
        "file": {
            "type": "object",
            "properties": {
                "id": {"type": "number"}
            },
        },
    },
    "required": ["file"]
}


@app.route("/api/songs", methods=["GET"])
@decorators.accept("application/json")
def get_songs():
    """ Return a list of all the songs as JSON """

    # get the songs from the database
    songs = session.query(models.Song).all()

    # convert the songs to JSON and return a Response
    data = json.dumps([song.as_dictionary() for song in songs])
    return Response(data, 200, mimetype="application/json")


@app.route("/api/songs", methods=["POST"])
@decorators.accept("application/json")
@decorators.require("application/json")
def post_song():
    """ Add a new song """
    data = request.json
    print data

    # check that the JSON supplied is valid
    # if not return a 422 Unprocessable Entity
    try:
        validate(data, song_schema)
    except ValidationError as error:
        data = {"message": error.message}
        return Response(json.dumps(data), 422, mimetype="application/json")

    # add the song to the database
    song = models.Song(song_file_id=data["file"]["id"])
    session.add(song)
    session.commit()

    # return a 201 Created, containing the post as JSON and with the
    # location header set to the location of the post
    data = json.dumps(song.as_dictionary())
    headers = {"Location": url_for("get_songs")}
    return Response(data, 201, headers=headers, mimetype="application/json")


@app.route("/api/songs/<int:id>", methods=["PUT"])
@decorators.accept("application/json")
@decorators.require("application/json")
def update_song(id):
    """ Updating a single song """

    # check if the song exists, if not return a 404 with a helpful message
    song = session.query(models.Song).get(id)
    if not song:
        message = "Could not find song with id {}".format(id)
        data = json.dumps({"message": message})
        return Response(data, 404, mimetype="application/json")

    data = request.json

    # check that the JSON supplied is valid
    # if not, return a 422 Unprocessable Entity
    try:
        validate(data, song_schema)
    except ValidationError as error:
        data = {"message": error.message}
        return Response(json.dumps(data), 422, mimetype="application/json")

    song.song_file = data["song_file"]
    session.commit()

    # return an OK 200, containing the song as JSON with the
    # location header set to the location of the post
    data = json.dumps(song.as_dictionary())
    headers = {"Location": url_for("post_get", id=song.id)}
    return Response(
        data, 200, headers=headers,
        mimetype="application/json"
    )


@app.route("/api/songs/<int:id>", methods=["DELETE"])
@decorators.accept("application/json")
def delete_song(id):
    """ Delete a single song """
    # check if the song exists, if not return a 404 with a helpful message
    song = session.query(models.Song).get(id)
    if not song:
        message = "Could not find song with id {}".format(id)
        data = json.dumps({"message": message})
        return Response(data, 404, mimetype="application/json")

    # otherwise just delete the song
    session.delete(song)
    session.commit()

    message = "Successfully deleted song with id {}".format(id)
    data = json.dumps({"message": message})
    return Response(data, 200, mimetype="application/json")


@app.route("/api/songs/<int:id>", methods=["GET"])
@decorators.accept("application/json")
def get_single_song(id):
    """ Return a single song as JSON """
    # get the song from the database
    song = session.query(models.Song).get(id)

    # check if the song exists, if not return 404 with message
    if not song:
        message = "Could not find song with id {}".format(id)
        data = json.dumps({"message": message})
        return Response(data, 404, mimetype="application/json")

    # return song as JSON
    data = json.dumps(song.as_dictionary())
    return Response(data, 200, mimetype="application/json")


@app.route("/uploads/<filename>", methods=["GET"])
def uploaded_file(filename):
    return send_from_directory(upload_path(), filename)


@app.route("/api/files", methods=["GET"])
@decorators.accept("application/json")
def get_files():
    """ Return a list of all the files as JSON """
    # should we use query string arguments?

    # get the files from the database
    files = session.query(models.File).all()

    # convert the songs to JSON and return a Response
    data = json.dumps([file.as_dictionary() for file in files])
    return Response(data, 200, mimetype="application/json")


@app.route("/api/files", methods=["POST"])
@decorators.require("multipart/form-data")
@decorators.accept("application/json")
def file_post():
    file = request.files.get("file")
    if not file:
        data = {"message": "Could not find file data"}
        return Response(json.dumps(data), 422, mimetype="application/json")

    filename = secure_filename(file.filename)
    db_file = models.File(filename=filename)
    session.add(db_file)
    session.commit()
    file.save(upload_path(filename))

    data = db_file.as_dictionary()
    return Response(json.dumps(data), 201, mimetype="application/json")
