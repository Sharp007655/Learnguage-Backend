# Generated by Django 5.1 on 2024-08-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllWordData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('read', models.CharField(max_length=100)),
                ('mean', models.CharField(max_length=200)),
                ('language', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LanguageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_ja', models.CharField(max_length=20)),
                ('lang_en', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ModeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OriginalWordData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('word', models.CharField(max_length=50)),
                ('read', models.CharField(max_length=100)),
                ('mean', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuizData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.CharField(max_length=20)),
                ('word', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, unique=True)),
                ('language', models.IntegerField(blank=True, null=True)),
                ('mode', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserWordData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('word', models.IntegerField()),
                ('count', models.IntegerField(default=1)),
                ('quiz', models.IntegerField(default=1)),
                ('correct', models.IntegerField(default=1)),
                ('probability', models.FloatField(default=1)),
                ('period', models.IntegerField(default=0)),
                ('hide', models.BooleanField(default=False)),
            ],
        ),
    ]
