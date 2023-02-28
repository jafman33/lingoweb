from dataclasses import dataclass
from app import app
# from config import client, s3, os
# from newDoc import *

import hashlib
from functools import wraps
from datetime import datetime
# import pytz

from flask import (
    render_template, 
    redirect, 
    url_for, 
    request, 
    session, 
    make_response, 
    send_from_directory,
    flash
    )

import re
# import yaml
import json
# import myLib

# from werkzeug.utils import secure_filename
# from faunadb import query as q
# from faunadb.objects import Ref

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# GTTS
# from flask_gtts import gtts
# gtts(app, temporary=False, tempdir='flask_gtts', route=True, route_path='/gtts')


# # Login decorator to ensure user is logged in before accessing certain routes
# def login_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if "user" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)

#     return decorated

# Index route, this route redirects to login/register page
# @app.route("/", methods=["GET", "POST"])
# def index():
#     return redirect(url_for("login"))



# @app.route("/reset_password", methods=["GET", "POST"])
# def reset_password():

#     if request.method == "POST":
        
#         email = request.form["email"]
#         password = request.form["password"]
        
#         # password cannot be empty!
#         if not password and not email:
#             flash("Must enter and email and a new password")
#             return redirect(url_for('reset_password'))
        
#         try:
#             user = client.query(q.get(q.match(q.index("userEmail_index"), email)))
#             id = user["ref"].id()
#             myLib.resetPassword(id,hashlib.sha512(password.encode()).hexdigest())
#             flash("Password updated successfully")
#             return redirect(url_for("login"))
#         except:
#             flash("Email not found")
#             return redirect(url_for("reset_password"))
            
#     return render_template("reset_password.html")


# @app.route("/password", methods=["GET", "POST"])
# @login_required
# def update_password():

#     if request.method == "POST":
        
#         password1 = request.form["password1"]
#         password2 = request.form["password2"]
        
#         # password cannot be empty!
#         if not password1:
#             flash("Passwords cannot be empty")
#             return redirect(url_for('update_password'))
#         elif password1 != password2:
#             flash("Passwords do not match!")
#             return redirect(url_for('update_password'))
#         else:
#             myLib.updatePassword(hashlib.sha512(password1.encode()).hexdigest())
#             flash("Password updated successfully")
#             return redirect(url_for("update_password"))
            
#     return render_template("password.html")

# # Register a new user and hash password
# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
        
#         # To setup validator for email
#         firstname = request.form["firstname"]
#         lastname = request.form["lastname"]
#         email = request.form["email"].strip().lower()
#         password = request.form["password"]
        
#         # Make sure no ther user with similar credentials is already registered
#         try:
#             user = client.query(q.get(q.match(q.index("userEmail_index"), email)))
#             if user:
#                 flash("Email already exists.")
#                 return redirect(url_for('register'))
        
#         except:
            
#             if not firstname or not lastname or not password or not email:
#                 flash("Please fill out the form completely.")
#                 return redirect(url_for('register'))
            
#             else:
        
#                 # Todo - add check for terms and conditions
#                 user = myLib.create_user(firstname, lastname, email, password) 
                
#                 # Create a new document for newly registered user
#                 newDoc(user["ref"].id())
                
#                 # Create new session for newly logged in user
#                 session["user"] = {
#                     "id": user["ref"].id(),
#                     "firstname": user["data"]["firstname"],
#                     "lastname": user["data"]["lastname"],
#                     "email": user["data"]["email"],
#                     "loggedin": True,
#                 }
                            
#                 return redirect(url_for("about"))
            
#     return render_template("register.html")

# @ app.route('/about', methods=['GET', 'POST'])
# @login_required
# def about():
#     user = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))

#     return render_template('about.html', user = user)

# @ app.route('/my-home', methods=['GET', 'POST'])
# @login_required
# def my_home():

#     keys = []
#     var = []
    
#     user = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))
#     # create new doc if it does not exist!
#     try: 
#         myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
#         lessonStatus = [myLessons['data']['lesson_'+str(i)]['status'] for i in range(1, 29)]
#     except:
#         newDoc(user["ref"].id())
#         myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
#         lessonStatus = [myLessons['data']['lesson_'+str(i)]['status'] for i in range(1, 29)]
    
#     for lessonNo in range(1,29):
#         phoneme = "yaml/phoneme" + str(lessonNo) + ".yaml"
#         print(phoneme)
#         lessonData = yaml.full_load(open(phoneme)) 
#         keys.append(lessonData['contrast']['key'])
#         var.append(lessonData['contrast']['var'])
        
#     return render_template('my-home.html', home_active='active', user=user, lessonStatus=lessonStatus, keys=keys, var=var)


# @ app.route('/my-lessons', methods=['GET', 'POST'])
# @login_required
# def my_lessons():

#     keys = []
#     var = []
#     grades = []

#     user = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
#     lessonStatus = [myLessons['data']['lesson_'+str(i)]['status'] for i in range(1, 29)]
    
#     for lessonNo in range(1,29):
#         phoneme = "yaml/phoneme" + str(lessonNo) + ".yaml"
#         lessonData = yaml.full_load(open(phoneme)) 
#         keys.append(lessonData['contrast']['key'])
#         var.append(lessonData['contrast']['var'])
#         try:
#             grades.append(myLessons['data']['lesson_'+str(lessonNo)]['review']['grade'])
#         except:
#             grades.append(0)
            
#     print(grades)

#     return render_template(
#         'lessons-list.html', 
#         lessons_active='active', 
#         user=user, 
#         lessonStatus=lessonStatus, 
#         keys=keys,
#         var = var,
#         grades = grades,
#         )


# @ app.route('/lesson-menu/<lesson>', methods=['GET', 'POST'])
# @login_required
# def lesson_menu(lesson=None):
    
#     user_data = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))
#     lessonNo = "lesson_" + lesson
#     phoneme_request = "yaml/phoneme" + str(lesson) + ".yaml"
#     lessonData = yaml.full_load(open(phoneme_request))
    
#      # Get Lesson Info from Fauna
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
#     statuses = myLessons['data'][lessonNo]
    
#     # update the status of the requested lesson to 'in-progress' IFF status != 'completed'
#     if myLessons['data'][lessonNo]['status'] != 'completed':
#         myLib.update_lesson_status(myLessons["ref"].id(),lessonNo, "in-progress", "0")
#         myLib.update_review_status(myLessons["ref"].id(), lessonNo, "not-started", "0")
#         myLib.update_lesson_overview(myLessons["ref"].id(), lessonNo, "not-started")
    
#     return render_template(
#         'lesson-menu.html',
#         user= user_data,
#         data = lessonData,
#         statuses = statuses
#         )
    
# @ app.route('/lesson-menu2/<lesson>', methods=['GET', 'POST'])
# @login_required
# def lesson_menu2(lesson=None):
    
#     user_data = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))
#     lessonNo = "lesson_" + lesson
#     phoneme_request = "yaml/phoneme" + str(lesson) + ".yaml"
#     lessonData = yaml.full_load(open(phoneme_request))
    
#      # Get Lesson Info from Fauna
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
#     statuses = myLessons['data'][lessonNo]
    
#     # update the status of the requested lesson to 'in-progress' IFF status != 'completed'
#     if myLessons['data'][lessonNo]['status'] != 'completed':
#         myLib.update_lesson_status(myLessons["ref"].id(),lessonNo, "in-progress", "0")
#         myLib.update_review_status(myLessons["ref"].id(), lessonNo, "not-started", "0")
#         myLib.update_lesson_overview(myLessons["ref"].id(), lessonNo, "not-started")

    
#     return render_template(
#         'lesson-menu2.html',
#         user= user_data,
#         data = lessonData,
#         statuses = statuses
#         )

# @ app.route('/lesson-overview/<lesson>', methods=['GET', 'POST'])
# @login_required
# def lesson_overview(lesson=None):
    
#     user_data = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))

#     lessonNo = "lesson_" + lesson
#     phoneme_request = "yaml/phoneme" + str(lesson) + ".yaml"
#     lessonData = yaml.full_load(open(phoneme_request))
    
#     # set status
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
#     if myLessons['data'][lessonNo]["overview"] != "completed":
#         myLib.update_lesson_overview(myLessons["ref"].id(), lessonNo, "completed")
    
#     return render_template(
#         'lesson-overview.html',
#         user= user_data,
#         data = lessonData
#         )
    
# @ app.route('/lesson-rhyme/<lesson>', methods=['GET', 'POST'])
# @login_required
# def rhyme(lesson=None):
    
#     user_data = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))

#     phoneme_request = "yaml/phoneme" + str(lesson) + ".yaml"
#     lessonData = yaml.full_load(open(phoneme_request))
        
#     return render_template(
#         'lesson-rhyme.html',
#         user= user_data,
#         data = lessonData
#         )


# @ app.route('/lesson', methods=['GET', 'POST'])
# @login_required
# def lesson():
    
#     lesson  = request.args.get('lesson', None)
#     pair  = request.args.get('pair', None)
    
#     # Get Lesson Data from input file
#     lessonNo = "lesson_" + lesson
#     pairNo = "pair_" + pair
#     phoneme_request = "yaml/phoneme" + str(lesson) + ".yaml"
#     lessonData = yaml.full_load(open(phoneme_request))

#     # Get Lesson Info from Fauna
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
#     pairs = myLessons['data'][lessonNo]["pairs"]
        
#     # set status
#     if myLessons['data'][lessonNo]["pairs"][pairNo]["status"] != 'completed':
#         myLib.update_pair_status(myLessons["ref"].id(), lessonNo, pairNo, "in-progress", "0")

#     # Update pair status and route if passed
#     if request.method == 'POST' and request.form['btn'] == 'Next!':
#         # grade defined here.
#         grade = request.form["grade"]
#         myLib.update_pair_status(myLessons["ref"].id(), lessonNo, pairNo, "completed", grade)
#         return redirect(url_for('lesson_menu', lesson = lesson))
    
#     # Update pair status and route if failed
#     if request.method == 'POST' and request.form['btn'] == 'Keep Learning':
#         return render_template('lesson-pair.html', data=lessonData, activePair = pair, pairs = pairs)
    
#     return render_template('lesson-pair.html', data=lessonData, activePair = pair, pairs = pairs)

# @ app.route('/lesson2', methods=['GET', 'POST'])
# @login_required
# def lesson2():
    
#     lesson  = request.args.get('lesson', None)
#     pair  = request.args.get('pair', None)
    
#     # Get Lesson Data from input file
#     lessonNo = "lesson_" + lesson
#     pairNo = "pair_" + pair
#     phoneme_request = "yaml/phoneme" + str(lesson) + ".yaml"
#     lessonData = yaml.full_load(open(phoneme_request))

#     # Get Lesson Info from Fauna
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
#     pairs = myLessons['data'][lessonNo]["pairs"]
        
#     # set status
#     if myLessons['data'][lessonNo]["pairs"][pairNo]["status"] != 'completed':
#         myLib.update_pair_status(myLessons["ref"].id(), lessonNo, pairNo, "in-progress", "0")

#     # Update pair status and route if passed
#     if request.method == 'POST' and request.form['btn'] == 'Next!':
#         grade = request.form["grade"]
#         myLib.update_pair_status(myLessons["ref"].id(), lessonNo, pairNo, "completed", grade)
#         return redirect(url_for('lesson_menu2', lesson = lesson))
#     elif request.method == 'POST' and request.form['btn'] == 'Keep Learning':
#         return render_template('lesson-pair2.html', data=lessonData, activePair = pair, pairs = pairs)
#     return render_template('lesson-pair2.html', data=lessonData, activePair = pair, pairs = pairs)

# @ app.route('/review', methods=['GET', 'POST'])
# @login_required
# def review():
    
#     lesson  = request.args.get('lesson', None)

#     # Get Lesson Data from input file
#     lessonNo = "lesson_" + lesson
#     phoneme_request = "yaml/phoneme" + str(lesson) + ".yaml"
#     lessonData = yaml.full_load(open(phoneme_request))

#     # Get Lesson Info from Fauna
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
    
#     # set status
#     if myLessons['data'][lessonNo]["review"]["status"] != "completed":
#         myLib.update_review_status(myLessons["ref"].id(),lessonNo, "in-progress", "0")

#     # Update pair status and route if passed
#     if request.method == 'POST' and request.form['btn'] == 'Next!':
#         grade = request.form["grade"]
#         myLib.update_review_status(myLessons["ref"].id(), lessonNo, "completed", grade)
#         # setup algo to compute lesson status here
#         #
#         #
#         myLib.update_lesson_status(myLessons["ref"].id(), lessonNo, "completed", grade)
#         return redirect(url_for('rhyme', lesson = lesson ))
    
#     if request.method == 'POST' and request.form['btn'] == 'Keep Learning':
#         return render_template('lesson-review.html', data=lessonData)
    
#     return render_template('lesson-review.html', data=lessonData)

# @ app.route('/review2', methods=['GET', 'POST'])
# @login_required
# def review2():
    
#     lesson  = request.args.get('lesson', None)
    
#     # Get Lesson Data from input file
#     lessonNo = "lesson_" + lesson
#     phoneme_request = "yaml/phoneme" + str(lesson) + ".yaml"
#     lessonData = yaml.full_load(open(phoneme_request))

#     # Get Lesson Info from Fauna
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
    
#     # set status
#     if myLessons['data'][lessonNo]["review"]["status"] != "completed":
#         myLib.update_review_status(myLessons["ref"].id(),lessonNo, "in-progress", "0")

#     # Update pair status and route if passed
#     if request.method == 'POST' and request.form['btn'] == 'Next!':
#         grade = request.form["grade"]
#         myLib.update_review_status(myLessons["ref"].id(), lessonNo, "completed", grade)
#         # setup algo to compute lesson status here
#         #
#         #
#         myLib.update_lesson_status(myLessons["ref"].id(), lessonNo, "completed", grade)
#         return redirect(url_for('rhyme', lesson = lesson ))
    
#     elif request.method == 'POST' and request.form['btn'] == 'Keep Learning':
#         return render_template('lesson-review2.html', data=lessonData)
#     return render_template('lesson-review2.html', data=lessonData)


# @ app.route('/about-3L-Ranch', methods=['GET', 'POST'])
# def how_to_play():
#     return render_template('how-to-play.html')

# @ app.route('/feedback', methods=['GET', 'POST'])
# @login_required
# def feedback():
#     name = session["user"]["firstname"]
    
#     if request.method == 'POST':
#         feedback = request.form["feedback"]
#         # create document
#         if feedback != '':
#             myLib.create_feedback(feedback)
#             flash("Feedback Sent!")
#             return redirect(url_for("feedback"))
#         else:
#             flash("Feedback field must not be left blank")
#             return redirect(url_for("feedback"))
    
#     return render_template('feedback.html', name = name)


# @ app.route('/under-construction', methods=['GET', 'POST'])
# def under_construction():
#     return render_template('page-under-construction.html')

# @ app.route('/leaderboard', methods=['GET', 'POST'])
# def leaderboard():
#     myLessons = client.query(q.get(q.match(q.index("user_id_index"), session["user"]['id'])))
    
#     # update user points
#     points = 0
#     lessons = 0 
#     for lessonNo in range(1,29):
#         try:
#             points = points + int(myLessons['data']['lesson_'+str(lessonNo)]['review']['grade'])
#             if int(myLessons['data']['lesson_'+str(lessonNo)]['review']['grade']) > 0:
#                 lessons = lessons + 1
#         except:
#             points = points + 0
#     myLib.update_user_points(session["user"]['id'], points)
#     user_data = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))
    
#     # get all users and their points
#     talents = myLib.getCollection("var", "users")    
#     sorted_talents = sorted(talents, key=lambda x: int(x["data"]["points"]), reverse=True)
    
#     # get your place
#     place = 0
#     for item in sorted_talents:
#         place = place + 1
#         if item["ref"].id() == session["user"]['id']:
#             break

#     return render_template('leaderboard.html', user=user_data, talents = sorted_talents, lessons = lessons, place = place)

# @ app.route('/email', methods=['GET', 'POST'])
# def users():
#     talents = myLib.getCollection("var", "users")    
#     return render_template('email.html', talents = talents)

# @app.route("/profile-edit", methods=["GET","POST"])
# @login_required
# def profile_edit():
#     payload = {}
#     user_data = client.query(q.get(q.match(q.index("userEmail_index"), session["user"]['email'])))

#     if request.method == 'POST':            
#         photo = request.files['file']
#         if photo.filename != '' and myLib.allowed_file(photo.filename):
#             photoUrl = myLib.uploadPhotoS3(photo)
#             payload.update({"photo": photoUrl})
        
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']  
        
#         payload.update({"firstname": firstname})
#         payload.update({"lastname": lastname})
        
#         myLib.updateProfile(payload)  

#         if request.form['btn'] == 'Save':
#             return redirect(url_for('my_home'))

#     return render_template("profile-edit.html", user = user_data)

# # Rout to the service-worker javascript file otherwise not found.
# @app.route('/service-worker.js')
# def sw():
#     response = make_response(
#         send_from_directory(
#             'templates',
#             path='service-worker.js'
#         )
#     )
#     response.headers['Content-Type'] = 'application/javascript'
#     # response.headers['Cache-Control'] = 'no-cache'
#     return response


# @app.route("/t2s/<contrastNo>/<name>", methods=['POST', 'GET'])
# def t2s(contrastNo, name):
#     from gtts import gTTS
#     import os
#     filename = "static/assets/audio/contrast" + \
#         contrastNo + "/words/" + name + ".mp3"
#     obj = gTTS(text=name, lang='en')
#     obj.save(filename)
#     return '', 204

# @app.route("/t2sRhyme/<contrastNo>/<rhyme>", methods=['POST', 'GET'])
# def t2sRhyme(contrastNo, rhyme):
#     from gtts import gTTS
#     import os
#     filename = "static/assets/audio/contrast" + \
#         contrastNo + "/rhyme/rhyme.mp3"
#     obj = gTTS(text=rhyme, lang='en')
#     obj.save(filename)
#     return '', 204



# @app.route("/t2sNav/<audio>", methods=['POST', 'GET'])
# def t2sNav(audio):
#     from gtts import gTTS
#     import os
#     filename = "static/assets/audio/common/navigation/learn.mp3"
#     obj = gTTS(text=audio, lang='en')
#     obj.save(filename)
#     return '', 204

# # @app.route('/manifest.json')
# # def manifest():
# #     return send_from_directory('static', 'manifest.json')

# @app.route("/terms", methods=["GET"])
# def terms():
#     return render_template("terms.html")

# @app.route('/logout')
# @login_required
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('login'))






if __name__ == '__main__':
    app.run(debug=True)
