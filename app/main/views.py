from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from . import main
from ..models import Pitch, Review, User
from .. import db