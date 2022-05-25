from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.show import Show
from flask_app.models.user import User


@app.route('/new/show')
def new_show():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_show.html',user=User.get_by_id(data))  


@app.route('/show/show/<int:id>')
def show_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_show.html",shows=Show.get_one_show_with_user(data),user=User.get_by_id(user_data))

    

@app.route('/edit/show/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_show.html",edit=Show.get_one(data),user=User.get_by_id(user_data))

#! ori

# #* new item here 

@app.route('/create/show/', methods = ['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect('/new/show')
    data = {
        'title':request.form['title'],
        'network': request.form ['network'],
        'release_date': request.form ['release_date'], 
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    Show.save(data)
    return redirect ('/dashboard')


    #* update data 

@app.route('/update/show', methods = ['POST'])  #! removed back slash form the end of show (show/)
def update_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect('/new/show')
    data = {
        'title':request.form['title'],
        'network': request.form ['network'],
        'release_date': request.form ['release_date'],
        'description': request.form ['description'],
        'id': request.form ['id']
    }
    Show.update(data)
    return redirect ('/dashboard')

# #* destroy 

@app.route('/destroy/show/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id':id 
    }
    Show.destroy(data)
    return redirect('/dashboard')
