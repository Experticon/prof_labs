from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import url
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


def custom_login(request):
    return redirect('home')


def index(request):
    return render(request, 'main/index.html', {'role': get_role(request.user)})


def main(request):
    data = {
        'title': 'Что это такое?',
        'role': get_role(request.user)
    }
    return render(request, 'main/main.html', data)


def table_view(request, idx):
    role = get_role(request.user)
    locked_tables = [0]

    if idx in locked_tables and (role == "Client" or role == ""):
        return redirect('/main')

    table = []
    model = [CallHistory, StudentInfo, ClientGroup, Faculty, Discipline]
    table_name = ["История обращений", "Информация о студенте", "Группы студентов", "Факультеты", "Предмет"]

    if idx == 0:
        for m in CallHistory.objects.all():
            table.append({"id": m.id, 0: m.fio, 1: m.email, 2: m.text, 3: m.group_name, 4: m.faculty})

    elif idx == 1:
        for m in StudentInfo.objects.all():
            table.append({"id": m.id, 0: m.fio, 1: m.address, 2: m.age, 3: m.phoneNumber, 4: m.group_name})

    elif idx == 2:
        for m in ClientGroup.objects.all():
            table.append({"id": m.id, 0: m.group_name, 1: m.faculty})

    elif idx == 3:
        for m in Faculty.objects.all():
            table.append({"id": m.id, 0: m.faculty})

    elif idx == 4:
        for m in Discipline.objects.all():
            table.append({"id": m.id, 0: m.discipline, 1: m.faculty})

    return render(request, 'main/table_show.html',
                  {'table_id': idx,
                   'table': table,
                   'names': model[idx].names,
                   'table_name': table_name[idx],
                   'role': role})


def table_change(request, idx, el, command):
    forms = [CallHistoryForm, StudentInfoForm, ClientGroupForm, FacultyForm, Discipline_form]
    model = [CallHistory, StudentInfo, ClientGroup, Faculty, Discipline]
    form = forms[idx]
    error = ''

    role = get_role(request.user)

    locked_tables = [0, 1]

    if idx in locked_tables and (role == "Client" or role == ""):
        return redirect('/main')

    if request.method == "POST":
        form = forms[idx].clone(request.POST)
        if form.is_valid():
            if command == 'add':
                form.save()
            elif command == 'edit':
                editing_model = model[idx].objects.filter(id=el)[0]
                for field in form._meta.fields:
                    setattr(editing_model, field, form.cleaned_data.get(field))
                editing_model.save()
            return redirect('table_show', idx)
        else:
            error = 'Данные введены неправильно'

    if command == 'edit':
        form = forms[idx].clone_for_edit(model[idx].objects.filter(id=el)[0])

    if command == 'delete':
        model[idx].objects.filter(id=el).delete()
        return redirect('table_show', idx)

    return render(request, "main/form.html", {
        'form': form,
        'names': model[idx].names,
        'error': error,
        'role': get_role(request.user)})

    #
    # if command == 'delete':
    #     model[idx].objects.filter(id=el).delete()
    #     return redirect('/table_show/' + str(idx))
    #
    # elif command == 'edit':
    #     if request.method == 'POST':
    #         editing_model = model[idx].objects.filter(id=el)[0]
    #         if editing_model.is_valid():
    #             for field in form._meta.fields:
    #                 setattr(editing_model, field, form.cleaned_data.get(field))
    #             editing_model.save()
    #             return redirect('/table_show/' + str(idx))
    #         else:
    #             error = "Данные введены неправильно"
    #             return render(request, 'main/form.html',
    #                           {'form': form, 'names': model[idx].names, 'error': error})
    #     form = forms[idx].clone_for_edit(model[idx].objects.filter(id=el)[0])
    #
    # elif command == 'add':
    #     if request.method == 'POST':
    #         form = forms[idx].clone(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/table_show/' + str(idx))
    #         else:
    #             error = "Данные введены неправильно"
    #             return render(request, 'main/form.html',
    #                           {'form': form, 'names': model[idx].names, 'error': error})
    #
    # return render(request, 'main/form.html',
    #               {'form': form, 'names': model[idx].names, 'error': error})


def login(request):
    if request.user.is_authenticated:
        return redirect('/main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Неверное имя пользователя или пароль')

        context = {

        }
        return render(request, 'registration/login.html', context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('/main')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                # Group.objects.get(name="Client").user_set.add(User.objects.last())
                messages.success(request, "Аккаунт зарегестрирован")
                return redirect('login')
        context = {
            'form': form
        }
        return render(request, 'registration/registration.html', context)


def get_role(user):
    template = ""
    if user.is_authenticated:
        if user.is_superuser:
            template = "Admin"
        elif user.groups.filter(name='Client').exists():
            template = "Client"
        elif user.groups.filter(name='Director').exists():
            template = "Director"
    return template
