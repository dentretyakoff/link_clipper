# yacut/yacut/api_views.py

import re
from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from settings import REG_EXP_SHORT_ID


@app.route('/api/id/', methods=['POST'])
def get_short_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    short = data.get('custom_id') or get_unique_short_id()
    if not re.match(REG_EXP_SHORT_ID, short):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=short).first():
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.')
    url_map = URLMap(original=data['url'], short=short)
    short_link = url_for('index_view', _external=True) + short
    db.session.add(url_map)
    db.session.commit()
    return (jsonify(
        {'url': url_map.original, 'short_link': short_link}),
        HTTPStatus.CREATED)


@app.route('/api/id/<path:short>/', methods=['GET'])
def get_original_link(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if not url_map:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK
