# Generated by Django 2.0.8 on 2018-09-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180916_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Femail'), ('not-specified', 'Not specified')], max_length=80, null=True),
        ),
    ]
