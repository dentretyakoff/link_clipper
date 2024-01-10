# yacut/yacut/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from settings import (REG_EXP_SHORT_ID, MAX_LEN_SHORT, MAX_LEN_ORIGINAL,
                      MIN_LEN_ORIGINAL, MIN_LEN_SHORT)


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Укажите длинную ссылку.'),
            Length(MIN_LEN_ORIGINAL, MAX_LEN_ORIGINAL,
                   message=('Максимальная длина оригинальной ссылки '
                            f'{MAX_LEN_ORIGINAL} символов.'))])
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Regexp(REG_EXP_SHORT_ID,
                   message=('Короткая ссылка может состоять из цифр и букв '
                            'латинского алфавита.')),
            Length(MIN_LEN_SHORT, MAX_LEN_SHORT,
                   message=('Длинна  короткой ссылки не более '
                            f'{MAX_LEN_SHORT} символов.')), Optional()])
    submit = SubmitField('Создать')
