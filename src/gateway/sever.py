import os, gridfs, pika, json 
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

sever = Flask(__name__)
sever.config["MONGO_URI"] ="mongodb://host.minikube.internal:27017/videos"

mongo = PyMongo(sever)

fs = gridfs.GridFs(mongo.db)

Connection = pika.BlockingConnection(pika.BlockingConnection("rabbitmq"))

channel = Connection.channel()

@sever.route("/login", methods=["POST"])

def login():
    token, err = access.login(request)