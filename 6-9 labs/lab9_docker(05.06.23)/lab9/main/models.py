from django.db import models


class CallHistory(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    email = models.CharField('email', max_length=100)
    text = models.CharField('Тип обращения', max_length=300)
    group_name = models.ForeignKey('ClientGroup', on_delete=models.CASCADE)  ##################
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)  ##########################

    names = ["id", "ФИО", "email", "Текст", "группа", "факультет"]

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'История обращений'
        verbose_name_plural = 'История обращений'


class StudentInfo(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    address = models.CharField('Адрес', max_length=150)
    age = models.IntegerField('Возраст', default=0)
    phoneNumber = models.IntegerField('Номер телефона', default=0)
    group_name = models.OneToOneField('ClientGroup', on_delete=models.CASCADE)

    names = ["id", "ФИО", "Адрес", "Возраст", "Номер телефона", "Группа"]

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Информация о студенте'
        verbose_name_plural = 'Информация о студенте'


class Faculty(models.Model):
    faculty = models.CharField('Faculty', max_length=50)

    names = ["id", "Факультет"]

    def __str__(self):
        return self.faculty

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class ClientGroup(models.Model):
    group_name = models.CharField('ClientGroup', max_length=100)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)  ##########################
    names = ["id", "Группа", "Факультет"]

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'Группа студентов'
        verbose_name_plural = 'Группы студентов'


class Discipline(models.Model):
    discipline = models.CharField('Дисциплина', max_length=100)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)  ##########################
    names = ["id", "Дисциплина", "Факультет"]

    def __str__(self):
        return self.discipline

    class Meta:
        verbose_name = 'Дициплина'
        verbose_name_plural = 'Дисциплины'

# class User(models.Model):
#     login = models.CharField(max_length=150, default="")
#     password = models.CharField(max_length=150, default="")
#     role = models.CharField(max_length=150, default="client")
#
#     names = ["Индекс", "Логин", "Пароль", "Роль"]
#     title = "Пользователи"
#
#     class Meta:
#         verbose_name = 'Тип банка'
#         verbose_name_plural = 'Типы банков'
#
#
#     def __str__(self):
#         return str(self.login)
#
