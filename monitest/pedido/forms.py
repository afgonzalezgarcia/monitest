# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import *
from django.forms.widgets import CheckboxSelectMultiple
from django.template.loader import render_to_string


class FormularioPedido(forms.ModelForm):
    class Meta:
        exclude = ["created_at", "updated_at"]
        model = Pedido