from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request,flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
login_manager = LoginManager()
login_manager.init_app(app)
ckeditor = CKEditor(app)
Bootstrap5(app)

# For adding profile images to the comment section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# TODO: Configure Flask-Login


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    """
        This callback is used to reload the user object from the user ID stored in the session.
        It connects the abstract user that Flask Login uses with the actual users in the model
        It should take the unicode ID of a user, and return the corresponding user object.

        It should return None (not raise an exception) if the ID is not valid.
        (In that case, the ID will manually be removed from the session and processing will continue.)

        :param user_id: unicode user ID
        :return: user object
        """
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()


# CREATE TABLE IN DB
# TODO: Create a User table for all your registered users.

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    posts = relationship('BlogPost',back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")



# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = relationship('User', back_populates='posts')
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    # ***************Child Relationship*************#
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text = db.Column(db.Text, nullable=False)
    posted_time = db.Column(db.String(250), nullable=False)


with app.app_context():
    #db.drop_all()
    db.create_all()

def admin_only(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        #is_admin = db.session.execute(db.Select(User).where(User.id == 1)).scalar()
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args,**kwargs)
        elif current_user.is_anonymous:
            return abort(403)
        else:
            return abort(403)
    return wrapper


def commenter_only(function):
    @wraps(function)
    def check(*args, **kwargs):
        user = db.session.execute(db.select(Comment).where(Comment.author_id == current_user.id)).scalar()
        if not current_user.is_authenticated or current_user.id != user.author_id:
            return abort(403)
        return function(*args, **kwargs)
    return check

# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    new_user_form = RegisterForm()
    if request.method == 'POST':
        if new_user_form.validate_on_submit():
            try:
                new_user = User(
                    email = new_user_form.email.data,
                    password = generate_password_hash(
                        new_user_form.password.data,
                        method='pbkdf2:sha256',
                        salt_length=8),
                    name = new_user_form.name.data
                )

                isExisting = db.session.execute(db.Select(User).where(User.email == new_user.email)).scalar()
                if isExisting:
                    flash("User with that email already exist! Please Log In")
                    return redirect(url_for('login'))
            except KeyError:
                return print(f"Something went wrong!")
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('get_all_posts'))
    return render_template("register.html",form=new_user_form)

@app.route('/login', methods=['GET','POST'])
def login():
    login_user_form = LoginForm()
    if request.method == 'POST':
        if login_user_form.validate_on_submit():
            email = login_user_form.email.data
            password = login_user_form.password.data

    # Find user by email entered.
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        #user = db.session.execute(db.select(User).where(User.email == login_user_form.email.data)).first()
        if not user:
            flash('One or more details are incorrect, please try again.')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('One or more details are incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts', name=user.name))
    return render_template("login.html", form = login_user_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>',methods = ['GET','POST'])
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    comment_form = CommentForm()
    the_post = db.get_or_404(BlogPost, post_id)
    if comment_form.validate_on_submit():
        if current_user.is_authenticated:
            new_comment = Comment(
                text=comment_form.comment_text.data,
                comment_author=current_user,
                parent_post=the_post,
                posted_time=date.today().strftime('%B %d, %I:%M%p')
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
        else:
            flash('Login Required, Please Log In!')
            return redirect(url_for('login'))
    return render_template("post.html", post=the_post, form=comment_form)


@app.route("/delete/comment/<int:comment_id>/<int:post_id>")
@commenter_only
@admin_only
def delete_comment(post_id, comment_id):
    comment_to_delete = db.get_or_404(Comment, comment_id)
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for('show_post', post_id=post_id))

# TODO: Use a decorator so only an admin user can create a new post
# TODO: add_new_post() to create a new blog post

@app.route('/new-post',methods=['GET','POST'])
@admin_only
def add_new_post():
    new_post_form = CreatePostForm()
    if new_post_form.validate_on_submit():
        try:
            post_to_add = BlogPost(
                title=new_post_form.title.data,
                subtitle=new_post_form.subtitle.data,
                author=current_user,
                img_url=new_post_form.img_url.data,
                body=new_post_form.body.data,
                date=date.today().strftime('%B %d, %I:%M%p')
            )
        except KeyError:
            return print(f"Something went wrong with adding new post")
            #return jsonify(error={"Bad Request": "Some or all fields were incorrect or missing."})
        else:
            db.session.add(post_to_add)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    return render_template('make-post.html',form=new_post_form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
