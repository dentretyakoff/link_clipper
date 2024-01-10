# yacut/yacut/views.py

import random
from http import HTTPStatus

from flask import abort, render_template, flash, redirect

from . import app, db
from .forms import URLForm
from .models import URLMap
from settings import ALPHABET_FOR_SHORT_URL


def get_unique_short_id() -> str:
    """Генерирует уникальный шестизначный код из цифр от 0 до 9
    и букв латинского алфавита."""
    symbols = ALPHABET_FOR_SHORT_URL
    while True:
        random.shuffle(symbols)
        short = ''.join([random.choice(symbols) for _ in range(6)])
        if not URLMap.query.filter_by(short=short).first():
            return short


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        if URLMap.query.filter_by(short=form.custom_id.data).first():
            flash('Короткая ссылка уже занята.')
        else:
            short = form.custom_id.data or get_unique_short_id()
            url_map = URLMap(original=form.original_link.data, short=short)
            db.session.add(url_map)
            db.session.commit()
            return render_template('index.html', form=form, short=short)
    return render_template('index.html', form=form)


@app.route('/<path:short>', methods=['GET'])
def redirect_view(short):
    original_url = URLMap.query.filter_by(short=short).first()
    if original_url:
        return redirect(original_url.original)
    abort(HTTPStatus.NOT_FOUND)
