# from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from libapp.models import Book, Dvd, Libuser, Libitem, Suggestion,User
from django.shortcuts import get_object_or_404, render, render_to_response
from libapp.forms import SuggestionForm, SearchlibForm,UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from random import randint
from django.template import RequestContext
from datetime import datetime
from django.core.mail import send_mail



def index(request):
    itemlist = Libitem.objects.all().order_by('title')[:10]
    return render(request, 'libapp/index.html', {'itemlist': itemlist, 'user': request.user})




def about(request):
    c = RequestContext(request)
    visits = int(request.COOKIES.get('visits', '0'))
    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 0:
            response = render_to_response('libapp/about.html', {'visits': visits + 1}, c, {'user': request.user})
            response.set_cookie('visits', visits + 1)
            response.set_cookie('last_visit', datetime.now())
    else:
        response = render_to_response('libapp/about.html', {'visits': visits + 1}, c, {'user': request.user})
        response.set_cookie('visits', visits + 1)
        response.set_cookie('last_visit', datetime.now())

    return response


def detail(request, item_id):
    # item = Libitem.objects.get(id=item_id)
    item = get_object_or_404(Libitem, pk=item_id)
    return render(request, 'libapp/detail.html', {'item': item})


def suggestions(request):
    suggestionlist = Suggestion.objects.all()[:10]
    return render(request, 'libapp/suggestions.html', {'itemlist': suggestionlist})



def newitem(request):
    suggestions = Suggestion.objects.all()
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.num_interested = 1
            suggestion.save()
            return HttpResponseRedirect(reverse('libapp:suggestions'))
        else:
            return render(request, 'libapp/newitem.html', {'form': form, 'itemlist': suggestions})
    else:
        form = SuggestionForm()
        return render(request, 'libapp/newitem.html', {'form': form, 'itemlist': suggestions})


def searchlib(request):
    form = SearchlibForm()
    return render(request, 'libapp/searchlib.html', {'form': form})


def searchresult(request):
    form = SearchlibForm(request.GET)
    if request.GET.get("title") != '':
        booklist = Book.objects.filter(title__contains=request.GET.get("title"))
        dvdlist = Dvd.objects.filter(title__contains=request.GET.get("title"))
        if request.GET.get("by") != '':
            booklist = booklist.filter(author__contains=request.GET.get("by"))
            dvdlist = dvdlist.filter(maker__contains=request.GET.get("by"))
        return render(request, 'libapp/searchlib.html', {'form': form, 'booklist': booklist, 'dvdlist': dvdlist})
    elif request.GET.get("by") != '':
        booklist = Book.objects.filter(author__contains=request.GET.get("by"))
        dvdlist = Dvd.objects.filter(maker__contains=request.GET.get("by"))
        return render(request, 'libapp/searchlib.html', {'form': form, 'booklist': booklist, 'dvdlist': dvdlist})
    else:
        return render(request, 'libapp/searchlib.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        luckynum = randint(0, 9)
        if request.session.get('luckynum') == None :
            request.session['luckynum'] = luckynum
            request.session.set_expiry(3600)
        else:
            luckynum = 0
            request.session['luckynum'] = luckynum
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('libapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'libapp/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('libapp:index')))


def myitems(request):
    if request.user.is_authenticated():
        libitem = Libitem.objects.filter(checked_out=True).filter(user_id=request.user)
        return render(request, 'libapp/myitems.html', {'itemlist': libitem,'msg':''})
    else:
        msg = "You are not libuser"
        return render(request, 'libapp/myitems.html', {'msg': msg})


def forgot_password(request):
    if request.method == 'POST':
        username=request.POST['username']
        user=User.objects.get(username=username)
        if user:
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            msg='Your password is:'+password
            send_mail(
                'Password Recovery',
                msg,
                'ghumanharpuneet@gmail.com',
                [user.email],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('libapp:user_login'))
        else:
            return render(request, 'libapp/forgot_password.html', {'msg':'Invalid username. Please contact administrator.'})
    else:
        return render(request, 'libapp/forgot_password.html', {'msg':''})



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = Libuser.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect(reverse('libapp:index'))
    else:
        form = UserForm()
        return render(request, 'libapp/register.html', {'form': form})
