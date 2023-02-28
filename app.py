from flask import Flask
from datetime import timedelta
# from flask_session import Session

app = Flask(__name__)
app.secret_key = "3L-Ranch key".encode('utf8')
app.config["SESSION_PERMANENT"] = True
# Session(app)

# --- UNCOMMENT FOR TIMED SESSION:
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)


# Here we need to assign secret key otherwise session will not work in Python.
# The secret key, ideally, should be in encrypted format.
# We have also configured the session timeout – 30 minutes because flask expires session
# once you close the browser unless you have a permanent session.
# Basically a session will exist for 30 minutes and in this 30 minutes a user’s
# visits will be unique for a particular URL. So to set the flag is_unique in
# table vistis_log you need to work on this.
