# Generated by Django 3.0.5 on 2020-06-03 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0003_auto_20200602_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='virtual_draw_strength',
            field=models.FloatField(default=4.0, help_text='Between networks and parent networks, add a prior of equal Elo with strength equal to this many virtual draws', verbose_name='Virtual draw strength'),
        ),
    ]