from wtforms import Form, StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired,Length(min=2, max=30,message="长度不正确")])
    page = IntegerField(validators=[NumberRange(min=0,max=99,message="必须为number")],default=0)