# -*- coding: utf-8 -*-
from PIL import Image, ImageFile
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.core.mail.message import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.utils.html import escape
from django.views.generic import View
from forms import *
from models import *
from unidecode import unidecode
import json
import os
import random
import re
import string
import struct
import requests

# Create your views here.
def procesar_pedido(request):
    # http://scoringservice.moni.com.ar:7001/api/v1/scoring/?document_number=30156149&gender=M&email=fran@mail.com
    api_url = "http://scoringservice.moni.com.ar:7001/api/v1/scoring/"
    form = FormularioPedido()
    if request.method == "POST":
        form  = FormularioPedido(request.POST)
        if form.is_valid():
            # la api deberia deberia accederse por POST, caso contrario seguiria el formato suministrado
            # suponiendo que la api responda suministrando los datos document_number, email, amount
            # los otros datos asumo seran para proceso de registro de nuevo usuario

            # El formulario de pedido de prestamos el usuario debe ingresar dni, nombre y apellido, genero, email y monto solicitado.
            # faltarían datos de autenticacion para uso de la API

            data = {
                "document_number": form.cleaned_data.get("dni"),
                "amount": form.cleaned_data.get("amount"),
                "email": form.cleaned_data.get("email")
            }

            response = requests.post(api_url, data = data)
            if response.status_code == requests.codes.ok:
                # suponiendo que la API responda en formato JSON y emita dentro de la respuesta un estatus ok para pedidos procesados exitosamente

                response_json = response.json()
                if response_json["status"] == "OK":
                    success = True
                    message = "Felicidades! se ha aprobado su prestamo por %s, revise su email donde encontrara la informacion" % (str(form.cleaned_data.get("amount")))

                    if not request.user.is_authenticated:
                        # se pudiera procesar usuarios nuevos en este putno redirigir, etc
                        pass

                    pedido = form.save(commit=False)
                    pedido.status = "approved"
                    # agegar otros datos de ser preciso
                    pedido.save()
                else:
                    # este mensaje sera desplegado en el front
                    # pudiera estudiarse que codigo de respuesta da la api para detemrinar acciones a tomar
                    error_message = "Se ha presentado un error al procesar su pago: \n%s" % (response_json["message"])
            else:
                # este mensaje sera desplegado en el front
                error_message = "Error al intentar procesar su pedido"

    return render_to_response("pedidos-moni.html", locals(), RequestContext(request))