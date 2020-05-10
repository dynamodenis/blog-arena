from flask import render_template,redirect,url_for,flash,request
from . import main
from .forms import UploadBlog,Comments
from ..models import User,Blogs,Comment
from flask_login import current_user,login_required
from .. import db

@main.route('/')
def index():
    page=request.args.get('page',1,type=int)
    blogs=Blogs.query.order_by(Blogs.posted_date.desc()).paginate(page=page,per_page=10)
    return render_template('index.html',blogs=blogs ,page='index')

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

    return render_template('upload_blog.html',form=form,title='New Blog' ,legend='Upload Blog',page='upload')

@main.route('/<int:blog_id>/comment', methods=['GET','POST'])
@login_required
def comment(blog_id):
    form_comment=Comments()
    image=url_for('static',filename='profile/'+current_user.profile_pic_path)
    blog=Blogs.query.filter_by(id=blog_id).first()
    comment_query=Comment.query.filter_by(blog_id=blog.id).all()
    if form_comment.validate_on_submit():
        comment=Comment(comment=form_comment.comment.data,blog_id=blog.id,user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.comment',blog_id=blog.id))
    print(image)
    return render_template('blog.html',form=form_comment,blog=blog,comments=comment_query,image=image,title='Comments')

