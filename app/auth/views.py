from . import auth
from flask import render_template,redirect,request,url_for
from .forms import RegistrationForm,LoginForm

    
@auth.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Account successfully created!')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',form=form,title='Create Account')
