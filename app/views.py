"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import time
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify
from werkzeug.utils import secure_filename
from forms import RegisterForm
from model import UserProfile
counter = 620000000
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/profile', methods=['POST','GET'])
def profile():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        User_Fname = request.form['FirstName']
        User_Lname = request.form['LastName']
        User_Age = request.form['Age']
        User_Gender = request.form['Gender']
        User_Bio = request.form['Bio']
         
        file_folder = app.config['UPLOAD_FOLDER']
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(file_folder, filename))
        ID = makeId()
        date = timeinfo()
        return redirect('home.html')
        
        
    else:
        flash('All fields are required')
        return render_template('user.html', form = form)
 
  
def timeinfo():
    current = time.strftime('%c')
    month = str(current[4:8])
    date = str(current[8:10])
    year = str(current[-4:])
    
    date_format = date + " " + month+ " " + year
    
    return date_format
  
      
       
def makeId():
   global counter
   counter +=1
   return counter
 


@app.route('/profiles')
def Userlist():
    
    
    
    return render_template('userlist.html')
 
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")    

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")