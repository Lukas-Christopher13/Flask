from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class ProdutosForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    quantidade = IntegerField('quantidade', validators=[DataRequired()])
    fornecedor = StringField('fornecedor', validators=[DataRequired()])

