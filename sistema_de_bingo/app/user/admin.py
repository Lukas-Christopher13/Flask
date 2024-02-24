from flask import render_template, redirect, url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView

from app.models import Cartela

from ..ext.admin import admin
from ..ext.data_base import db


class CustomCreateView(AdminIndexView):
    def dispatch_request(self):
        return redirect(url_for('cartela_admin.custom_create_view'))

class CartelaView(ModelView):
    page_size = 20

    create_template = "user/cartela_form.html"


def admin_config():

    admin.index_view = CustomCreateView()
    admin.add_view(CartelaView(Cartela, db.session)) 

