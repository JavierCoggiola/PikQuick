# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.core.mail import send_mail
from django.http import HttpResponse
from pikquick.models import Entrada, Coment, Follow , Imagen
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

@login_required(login_url='/usuario/ingreso')
def inicio(request):
    context = RequestContext(request)

    imagenes = Imagen.objects.all()
    user_reg = request.user
    who_follows = user_reg.who_follows.values('follower__username')
    users_follow=[]
    lista_followers = []

    for followers in user_reg.who_follows.all():
        users_follow.append(followers.follower)

    for v in who_follows:
        lista_followers.append(v['follower__username'])

    posts = Entrada.objects.filter(usuario__in=users_follow)

    return render_to_response('inicio.html',
                              {'posts':posts,
                              'imagenes': imagenes,
                              'lista_followers':lista_followers},
                              context)

@login_required(login_url='/usuario/ingreso')
def inicioAll(request):
    context = RequestContext(request)

    user_reg = request.user
    who_follows = user_reg.who_follows.values('follower__username')

    lista_followers = []
    for v in who_follows:
        lista_followers.append(v['follower__username'])

    posts = Entrada.objects.all()
    imagenes = Imagen.objects.all()
    return render_to_response('inicio.html',
                              {'posts':posts,
                              'imagenes': imagenes,
                              'lista_followers':lista_followers},
                              context)

@login_required(login_url='/usuario/ingreso')
def perfil(request, usuario):
    context = RequestContext(request)
    nombreusuario = usuario

    ###

    user_reg = request.user
    who_follows = user_reg.who_follows.values('follower__username')

    lista_followers = []
    for v in who_follows:
        lista_followers.append(v['follower__username'])

    user2view = User.objects.get(username=usuario)
    siguiendo=len(user2view.who_follows.values('follower__username'))-1
    seguidores=len(user2view.who_is_followed.values('follower__username'))-1

    ###
    posts = Entrada.objects.filter(usuario = usuario)
    entradas = posts.count()

    imagenes = Imagen.objects.all()

    return render_to_response('perfil.html',
                              {'imagenes': imagenes,
                              'posts':posts,
                              'seguidores':seguidores,
                              'siguiendo':siguiendo,
                              'usuario':nombreusuario,
                              'lista_followers':lista_followers,
                              'entradas':entradas
                              },
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

            ####AUTOSEGUIRSE
            toFollow = request.user
            seguir = Follow()
            seguir.following = request.user #YO
            seguir.follower = toFollow #YO
            seguir.save()

            return HttpResponse(status=204)
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
                    if not Follow.objects.filter(follower=request.user, following=request.user).exists():
                        toFollow = request.user
                        seguir = Follow()
                        seguir.following = request.user #YO
                        seguir.follower = toFollow #YO
                        seguir.save()
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
        pub.descPub=request.POST['descPub']
        pub.save()
        for i in range(1,3):
            key_img = 'img' + str(i)
            key_desc = 'desc' + str(i)
            if request.POST.get(key_img, True):
                img = Imagen(entrada=pub, img=request.FILES[key_img], desc=request.POST[key_desc])
                img.save()
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

@login_required(login_url='/usuario/ingreso')
def ver_message(request):
    context = RequestContext(request)
    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        coments = Coment.objects.filter(entrada=mi_post, published = True)

    return render_to_response('mensajes.html',
                              {'coments':coments},
                              context)

@login_required(login_url='/usuario/ingreso')
def ajustes(request):
    context = RequestContext(request)
    return render_to_response('ajustes.html',
                              context)

@login_required(login_url='/usuario/ingreso')
def deletePost(request):
    context = RequestContext(request)
    if request.method == 'POST':
        post = Entrada.objects.get(id=request.POST['id'])
        post.delete()
    Entrada.objects.all()
    return redirect('/')

@login_required(login_url='/usuario/ingreso')
def follow(request, toFollow_un):
    context = RequestContext(request)
    toFollow = User.objects.get(username=toFollow_un)
    seguir = Follow()
    seguir.following = request.user #YO
    seguir.follower = toFollow #El Otro
    seguir.save()

    return redirect('/')

@login_required(login_url='/usuario/ingreso')
def unFollow(request, toUnFollow_un):
    context = RequestContext(request)
    user = request.user
    toUnFollow = User.objects.get(username=toUnFollow_un) # user to unfollow
    try:
        Follow.objects.get(follower=toUnFollow, following=user).delete()
    except:
        print("No es posible dejar de seguir")
    return redirect('/')

def buscador(request, busqueda):
    context = RequestContext(request)
    try:
        imagenes = Imagen.objects.all()
        posts = Entrada.objects.filter(usuario = busqueda)
        nombreusuario = busqueda
        user_reg = request.user
        who_follows = user_reg.who_follows.values('follower__username')
        lista_followers = []
        for v in who_follows:
            lista_followers.append(v['follower__username'])
        user2view = User.objects.get(username=busqueda)
        siguiendo=len(user2view.who_follows.values('follower__username'))-1
        seguidores=len(user2view.who_is_followed.values('follower__username'))-1
        entradas = posts.count()
        imagenes = Imagen.objects.all()
        return render_to_response('perfil.html',
                                  {'imagenes': imagenes,
                                  'posts':posts,
                                  'seguidores':seguidores,
                                  'siguiendo':siguiendo,
                                  'usuario':nombreusuario,
                                  'lista_followers':lista_followers,
                                  'entradas':entradas
                                  },
                                  context)
    except Exception as e:
        print "No hay usuario"
        return redirect("/")

def notificaciones(request):
    context = RequestContext(request)
    user_reg = request.user
    users_follow=[]
    for followers in user_reg.who_follows.all():
        users_follow.append(followers.follower)
    posts = Entrada.objects.filter(usuario__in=users_follow)
    coments = Coment.objects.filter(usuario__in=users_follow)
    coments = coments.order_by('fecha_pub')
    return render_to_response('notificaciones.html',
                              {'posts':posts,
                               'coments':coments},
                              context)

def like(request, post, imge):
    if request.method == 'POST':
        for img in post.imagenes:
            if img.id == imge:
                img.liked.add(request.user)
            else:
                img.liked.remove(request.user)
    return redirect("/")

from django.http import JsonResponse
from django.http import HttpResponse

def countLike(request, post):
    context = RequestContext(request)
    imge = str(request.GET['imgid'])
    post_obj = Entrada.objects.get(pk=post)
    cont=0
    for img in post_obj.imagenes.all():
        print img
        print "{} - {} ".format(img.id, imge)
        if int(img.id) == int(imge):
            if request.user in img.liked.all():
                img.liked.remove(request.user)
            else:
                img.liked.add(request.user)
        else:
            print "remove {}".format(request.user)
            img.liked.remove(request.user)
        if cont==0:
            print "aa"
            imagen1=img
        else:
            print "bb"
            imagen2=img
        cont+=1

    likes1= str(imagen1.getLikes())
    likes2= str(imagen2.getLikes())
    data = {'image1': likes1, 'image2': likes2}
    return JsonResponse(data)
