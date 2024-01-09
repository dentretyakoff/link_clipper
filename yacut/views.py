# yacut/yacut/views.py

import random

from flask import abort, render_template, flash, url_for

from . import app, db
from .forms import URLForm
from .models import URLMap
from settings import ALPHABET_FOR_SHORT_URL


def get_unique_short_id() -> str:
    symbols = ALPHABET_FOR_SHORT_URL
    random.shuffle(symbols)
    custom_id = ''.join([random.choice(symbols) for _ in range(6)])
    return custom_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        # original_link = form.original_link.data
        # if URLMap.query.filter_by(original=original_link).first():
        #     flash('Такая ссылка уже есть в БД!')
        #     return render_template('add_opinion.html', form=form)
        return render_template('index.html',
                               form=form,
                               short=get_unique_short_id())
    return render_template('index.html', form=form)
