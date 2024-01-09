# yacut/yacut/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 2000, message=('Максимальная длина оригинальной '
                                             'ссылки 2000 символов'))])
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 6, message=('Длинна короткой ссылки '
                                          'строго 6 символов')), Optional()])
    submit = SubmitField('Создать')
