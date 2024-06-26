# yacut/yacut/views.py

import random

from flask import render_template, flash, redirect

from . import app, db
from .forms import URLForm
from .models import URLMap
from settings import ALPHABET_FOR_SHORT_URL, MAX_LEN_AUTOGENERATED_SHORT


def get_unique_short_id() -> str:
    """Генерирует уникальный шестизначный код из цифр от 0 до 9
    и букв латинского алфавита."""
    while True:
        random.shuffle(ALPHABET_FOR_SHORT_URL)
        short = ''.join([
            random.choice(ALPHABET_FOR_SHORT_URL)
            for _ in range(MAX_LEN_AUTOGENERATED_SHORT)])
        if not URLMap.query.filter_by(short=short).first():
            return short


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    if URLMap.query.filter_by(short=form.custom_id.data).first():
        flash('Предложенный вариант короткой ссылки уже существует.')
    else:
        short = form.custom_id.data or get_unique_short_id()
        url_map = URLMap(original=form.original_link.data, short=short)
        db.session.add(url_map)
        db.session.commit()
        return render_template('index.html', form=form, short=short)
    return render_template('index.html', form=form)


@app.route('/<path:short>', methods=['GET'])
def redirect_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)
