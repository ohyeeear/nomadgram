# Generated by Django 2.0.8 on 2018-09-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180919_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('not-specified', 'Not specified'), ('female', 'Femail')], max_length=80, null=True),
        ),
    ]
