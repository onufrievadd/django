# Generated by Django 3.2 on 2021-12-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='langs',
            field=models.CharField(blank=True, default='RU', max_length=10, verbose_name='язык'),
        ),
    ]
