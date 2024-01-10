# yacut/yacut/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Укажите длинную ссылку.'),
            Length(1, 2000, message=('Максимальная длина оригинальной ссылки '
                                     '2000 символов.'))])
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Regexp(r'^[a-zA-Z0-9]+$',
                   message=('Короткая ссылка может состоять из цифр и букв '
                            'латинского алфавита.')),
            Length(1, 6, message=('Длинна  короткой ссылки не более '
                                  '6 символов.')), Optional()])
    submit = SubmitField('Создать')
