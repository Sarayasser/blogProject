# Generated by Django 3.0.3 on 2020-02-25 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200225_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tagName',
            field=models.CharField(max_length=30, null=True),
        ),
    ]