# Generated by Django 2.2.10 on 2020-07-09 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название опроса')),
                ('description', models.TextField(verbose_name='Описание опроса')),
                ('date_start', models.DateTimeField(verbose_name='Дата начала')),
                ('date_end', models.DateTimeField(verbose_name='Дата конца')),
            ],
            options={
                'verbose_name': 'опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Текст вопроса')),
                ('type', models.CharField(choices=[('checkbox', 'Ответ с выбором нескольких вариантов'), ('text', 'Ответ текстом'), ('radio', 'Ответ с выбором одного варианта')], max_length=8, verbose_name='Тип вопроса')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='interview.Interview', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
