# Generated by Django 4.2.6 on 2023-10-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0003_alter_userinfo_emailactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='emailactive',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email Active'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='user', verbose_name='Profile'),
        ),
    ]
