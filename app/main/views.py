from flask import render_template,redirect,url_for,flash
from . import main
from .forms import UploadBlog
from ..models import User,Blogs,Comment
from flask_login import current_user,login_required
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/new/blog', methods=['GET','POST'])
@login_required
def uplaod_blog():
    form=UploadBlog()
    if form.validate_on_submit():
        blog=Blogs(category=form.category.data,blog=form.blog.data,user=current_user)
        db.session.add(blog)
        db.session.commit()
        flash('Blog Posted!')
        return redirect(url_for('main.index'))

    return render_template('upload_blog.html',form=form,title='New Blog' ,legend='Upload Blog')
