from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import forms


# TODO мб нужно на английском
class CallHistoryForm(ModelForm):
    class Meta:
        model = CallHistory
        # fields = ["ФИО", "Дата", "Текст", "id клиента", "id банка"]
        fields = ["fio", "email", "text", "group_name", "faculty"]

    @staticmethod
    def clone(request):
        return CallHistoryForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return CallHistoryForm(instance=istans)


class StudentInfoForm(ModelForm):
    class Meta:
        model = StudentInfo
        # fields = ["Адрес", "Возраст", "Номер телефона"]
        fields = ["fio", "address", "age", "phoneNumber", "group_name"]

    @staticmethod
    def clone(request):
        return StudentInfoForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return StudentInfoForm(instance=istans)


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        # fields = ["Название банка", "Адрес", "Тип банка"]
        fields = ["faculty"]

    @staticmethod
    def clone(request):
        return FacultyForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return FacultyForm(instance=istans)


class ClientGroupForm(ModelForm):
    class Meta:
        model = ClientGroup
        # fields = ["Надёжный", "VIP", "Тип клиента"]
        fields = ["group_name", "faculty"]

    @staticmethod
    def clone(request):
        return ClientGroupForm(request)

    @staticmethod
    def clone_for_edit(istans):
        return ClientGroupForm(instance=istans)


class Discipline_form(ModelForm):
    class Meta:
        model = Discipline
        # fields = ["Тип банка"]
        fields = ["discipline", "faculty"]

    @staticmethod
    def clone(request):
        return Discipline_form(request)

    @staticmethod
    def clone_for_edit(istans):
        return Discipline_form(instance=istans)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
