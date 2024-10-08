# Generated by Django 5.1 on 2024-08-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_alter_userworddata_period_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, unique=True)),
                ('chat_list', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
