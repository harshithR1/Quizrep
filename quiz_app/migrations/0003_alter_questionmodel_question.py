# Generated by Django 4.1.5 on 2023-02-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_remove_questionmodel_hint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='question',
            field=models.CharField(max_length=260),
        ),
    ]
