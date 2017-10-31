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

    form = PitchForm()
    category = Category(id)

    if form.validate_on_submit():

        title = form.title.data
        pitch = form.pitch.data

        new_pitch = Pitch(idea = pitch, category=category, user=current_user, title=title)

        new_pitch.save_pitch()

        return redirect(url_for('.category', id = category.id))

    title = f'{category.id} pitch'

    return render_template('new_pitch', title=title, pitch_form=form, category=category)


