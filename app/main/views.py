from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from . import main
from .forms import PitchForm, ReviewForm, CategoryForm, UpdateProfile
from ..models import Pitch, Review, User, Category, PhotoProfile
from .. import db, photos


@main.route('/')
@login_required

def index():

    categories = Category.get_category(id)

    return render_template('index.html', categories=categories)


@main.route('/category/<int:id>')
def category(id):

    category = Category.query.get(id)

    pitch = Pitch.get_pitch(id)

    title = f'All pitches for {category.name}'

    return render_template('category.html', category=category, pitch=pitch, title=title)


@main.route('/category/new', methods=['GET','POST'])
def new_category():

    form = CategoryForm()

    if form.validate_on_submit():

        name = form.name.data

        new_category = Category(name=name)

        new_category.save_category()

        return redirect(url_for('.index'))

    return render_template('new_category.html', category_form=form)


@main.route('/pitch/<int:id>')
def single_pitch(id):

    single_pitch = Pitch.query.get(id)
    reviews = Review.get_reviews(id)

    if single_pitch is None:
        abort (404)

    return render_template('pitch.html', pitch=single_pitch, reviews=reviews)


@main.route('/category/pitch/new/<int:id>', methods=['GET', 'POST'])
def new_pitch(id):

    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    form = PitchForm()

    if form.validate_on_submit():

        title = form.title.data
        pitch = form.pitch.data

        new_pitch = Pitch(pitch = pitch, category=category, user=current_user, title=title)

        new_pitch.save_pitch()

        return redirect(url_for('.category', id = category.id))

    title = f'{category.id} pitch'

    return render_template('new_pitch.html', title=title, pitch_form=form, category=category)


@main.route('/pitch/review/new/<int:id>', methods=['GET', 'POST'])
def new_review(id):

    pitch = Pitch.query.filter_by(id=id).first()

    if pitch is None:
        abort(404)

    form = ReviewForm()

    if form.validate_on_submit():

        review = form.review.data

        new_review = Review(review=review, user=current_user)

        new_review.save_review()

        return redirect(url_for('.single_pitch', id=pitch.id))

    return render_template('new_review.html', review_form=form, pitch=pitch)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update_profile.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


