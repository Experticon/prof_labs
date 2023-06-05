# Generated by Django 4.2.1 on 2023-06-04 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, verbose_name='ClientGroup')),
            ],
            options={
                'verbose_name': 'Группа студентов',
                'verbose_name_plural': 'Группы студентов',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=50, verbose_name='Faculty')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('age', models.IntegerField(default=0, verbose_name='Возраст')),
                ('phoneNumber', models.IntegerField(default=0, verbose_name='Номер телефона')),
                ('group_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.clientgroup')),
            ],
            options={
                'verbose_name': 'Информация о студенте',
                'verbose_name_plural': 'Информация о студенте',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(max_length=100, verbose_name='Дисциплина')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faculty')),
            ],
            options={
                'verbose_name': 'Дициплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.AddField(
            model_name='clientgroup',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faculty'),
        ),
        migrations.CreateModel(
            name='CallHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('text', models.CharField(max_length=300, verbose_name='Тип обращения')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faculty')),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.clientgroup')),
            ],
            options={
                'verbose_name': 'История обращений',
                'verbose_name_plural': 'История обращений',
            },
        ),
    ]
