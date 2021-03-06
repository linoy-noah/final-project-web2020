# Generated by Django 3.0.4 on 2020-07-14 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('GD', 'Gush Dan'), ('RH', 'Ramat Hagolan'), ('HS', 'Hashfela'), ('DR', 'Darom'), ('GL', 'Galil')], default='GD', max_length=2)),
                ('delType', models.CharField(choices=[('MA', 'Mail'), ('FO', 'Food'), ('FL', 'Flowers'), ('GF', 'Gift'), ('MB', 'Mystery Box')], default='MA', max_length=11)),
                ('status', models.IntegerField(choices=[(0, 'I Will Take It'), (1, 'Im On My Way'), (2, 'Delivery Has Arrieved'), (3, 'Finish Delivery')], default=0)),
                ('deliveryman', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('title', models.CharField(max_length=80)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
