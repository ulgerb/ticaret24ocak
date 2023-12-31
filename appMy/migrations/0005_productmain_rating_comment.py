# Generated by Django 4.2 on 2023-11-02 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0004_auto_20231026_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmain',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Ürün Puanı'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Yorum')),
                ('rating', models.IntegerField(verbose_name='Yorum Puanı')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.productmain', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
