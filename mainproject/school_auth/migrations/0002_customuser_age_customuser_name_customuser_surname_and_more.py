# Generated by Django 5.1.6 on 2025-02-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='customuser',
            name='surname',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
