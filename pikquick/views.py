# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.core.mail import send_mail
from django.http import HttpResponse
from pikquick.models import Entrada, Coment #, Imagen
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

# Create your views here.
@login_required(login_url='/usuario/ingreso')
def inicio(request):
    context = RequestContext(request)
    posts = Entrada.objects.all
    return render_to_response('inicio.html',
                              {'posts':posts,},
                              context)

@login_required(login_url='/usuario/ingreso')
def perfil(request):
    context = RequestContext(request)
    usuario = request.user.username
    posts = Entrada.objects.filter(usuario = usuario)
    return render_to_response('perfil.html',
                              {'posts':posts},
                              context)

@requires_csrf_token
@login_required(login_url='/usuario/ingreso')
def enviar_mail(request):
    context = RequestContext(request)
    if request.method=='POST':
        send_mail(request.POST['asunto'], request.POST['mensaje'], 'pikquickcontact@gmail.com',
    [request.POST['mail']], fail_silently=False)
    return render_to_response('perfil.html',
                              context)

@requires_csrf_token
def nuevo_usuario(request):
    context = RequestContext(request)
    if request.method=='POST':
        username=request.POST['username']
        try:
            user = User.objects.get(username=username)
            return HttpResponse(status=203)
        except User.DoesNotExist:
            n_u=User()
            n_u.username=username
            n_u.email=request.POST['email']
            password=request.POST['password']
            n_u.set_password(password)
            n_u.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse(status=204)
        #return redirect('/')
    return render_to_response('nuevousuario.html',
                              context)

@requires_csrf_token
def ingreso_usuario(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("");
                else:
                    return HttpResponse(status=203)
            else:
                return HttpResponse(status=203)
        else:
            return render_to_response('loguear.html',
                                              context)
    else:
        return render_to_response('loguear.html',
                                              context)

@login_required(login_url='/usuario/ingreso')
def salir_usuario(request):
    logout(request)
    context = RequestContext(request)
    return redirect('/')

@login_required(login_url='/usuario/ingreso')
def cambiar_pass(request):
    context = RequestContext(request)
    if request.method=='POST':
        if request.user.check_password(request.POST['password1']):
            request.user.set_password(request.POST['password2'])
            request.user.save()
            user= authenticate(username=request.user.username, password=request.POST['password2'])
            login(request, user)
            return redirect("/perfil")
    return render_to_response('perfil.html',
                              context)

@login_required(login_url='/usuario/ingreso')
def nuevapublic(request):
    context = RequestContext(request)
    return render_to_response('nuevapublic.html',
                              context)

@login_required(login_url='/usuario/ingreso')
def crear_public(request):
    context = RequestContext(request)
    if request.method=='POST':
        pub=Entrada()
        pub.usuario=request.user.username
        pub.img1=request.FILES['img1']
        pub.img2=request.FILES['img2']
        pub.desc1=request.POST['desc1']
        pub.desc2=request.POST['desc2']
        pub.descPub=request.POST['descPub']
        pub.save()
        return redirect("/")
    return render_to_response('nuevapublic.html',
                              context)

@login_required(login_url='/usuario/ingreso')
def save_message(request):
    context = RequestContext(request)
    coment_txt = None
    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        print(mi_post)
        coment_txt= request.POST['coment_txt']
        msje = Coment()
        msje.coment_txt = coment_txt
        msje.usuario = request.user.username
        msje.entrada = mi_post
        msje.save()
        coments = Coment.objects.filter(entrada=mi_post, published = True)
    return render_to_response('mensajes.html',
                              {'coments':coments},
                              context)

def ver_message(request):
    context = RequestContext(request)
    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        coments = Coment.objects.filter(entrada=mi_post, published = True)

    return render_to_response('mensajes.html',
                              {'coments':coments},
                              context)

@login_required(login_url='/usuario/ingreso')
def deletePost(request):
    context = RequestContext(request)
    if request.method == 'POST':
        post = Entrada.objects.get(id=request.POST['id'])
        post.delete()
    Entrada.objects.all()
    return redirect('/')

def user_profile(request, username):
    context = RequestContext(request)
    posts = Entrada.objects.filter(usuario = username)
    return render_to_response('profiles.html',
                              {'posts':posts},
                              context)

