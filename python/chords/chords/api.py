import os.path
import json

from flask import request, Response, url_for, send_from_directory
from werkzeug.utils import secure_filename
from jsonschema import validate, ValidationError

import models
import decorators
import analysis
from chords import app
from database import session
from utils import upload_path

#  Add a GET endpoint for /songs which returns a list of all of the songs as JSON.

@app.route("/api/songs", methods=["GET"])
def songs_get():
    # Get a list of songs

    songs = session.query(models.Song).all()
    for song in songs:
        return song.as_dictionary()
    # convert the songs to JSON and return a response
    data = song.as_dictionary()
    return Response(json.dumps(data), 200, mimetype="application.json")

# Add a POST endpoint for /songs which allows you to add a new song to the database. 

@app.route("/api/songs", methods=["POST"])
def songs_post():
    # Add a new song to the database 
    db_song = models.Song(file_id=file.id)
    session.add(db_song)
    session.commit()
    data = db_song.as_dictionary()
    return Response(json.dumps(data), 201, mimetype="application/json")

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

@app.route("/uploads/<filename>", methods=["GET"])
def uploaded_file(filename):
    return send_from_directory(upload_path(), filename)


"""
Check whether a song with the correct ID exists
Get the filename of the song from the database
Call the analyse function, passing in the path of the uploaded file
Return the results of the analysis as a JSON object
"""

@app.route("/api/songs/<id>/analysis", methods=["GET"])
def analyse_song():
    file = request.files.get("file")
    if file.id == "<id>":
        pass
    if file.id != "<id>":
        data = {"message": "Wrong file id"}
        return Response(json.dumps(data), 422, mimetype="application/json")
    filename = secure_filename(file.filename)
    db_file = models.File(filename=filename)


# pass in the path of the uploaded file
    analyse(upload_path(filename))
    return Response(json.dumps(data), 201, mimetype="application/json")



