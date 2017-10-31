from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from . import main
from .forms import PitchForm, ReviewForm
from ..models import Pitch, Review, User, Category
from .. import db


@main.route('/')
@login_required

def index():

    categories = Category.get_category()

    return render_template('index.html', categories=categories)


@main.route('/category/<int:id>')
def category(id):

    category = Category.query.get(id)

    pitch = Pitch.get_pitch(id)

    title = f'All pitches for {category.name}'

    return render_template('group.html', category=category, pitch=pitch, title=title)


@main.route('/pitch/<int:id>')
def single_pitch(id):

    single_pitch = Pitch.query.get(id)

    if single_pitch is None:
        abort (404)

    return render_template('pitch.html', single_pitch=single_pitch)


@main.route('/category/pitch/new/<int:id>', methods=['GET', 'POST'])
def new_pitch(id):

    category = Category.query.filter_by(id).first()

    if category is None:
        abort(404)


    form = PitchForm()

    if form.validate_on_submit():

        title = form.title.data
        pitch = form.pitch.data

        new_pitch = Pitch(idea = pitch, category=category, user=current_user, title=title)

        new_pitch.save_pitch()

        return redirect(url_for('.category', id = category.id))

    title = f'{category.id} pitch'

    return render_template('new_pitch', title=title, pitch_form=form, category=category)


@main.route('/pitch/review/new/<int:id>', methods=['GET', 'POST'])
def new_review(id):

    pitch = Pitch.query.filter_by(id).first()

    if pitch is None:
        abort(404)

    form = ReviewForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        new_review = Review(pitch_review=review, title=title, user=current_user)

        new_review.save_review()

        return redirect(url_for('.single_pitch', id=pitch.id))

    return render_template('new_review.html', review_form=form, pitch=pitch)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


