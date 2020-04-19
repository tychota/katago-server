# Generated by Django 3.0.1 on 2020-04-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='creation date')),
                ('result', models.CharField(choices=[('Active', 'Active')], db_index=True, max_length=15, verbose_name='run status')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('data_board_len', models.IntegerField(default=19, verbose_name='data board len')),
                ('inputs_version', models.IntegerField(default=7, verbose_name='inputs version for model features')),
                ('max_search_threads_allowed', models.IntegerField(default=8, verbose_name='max search threads server promises to never exceed')),
            ],
        ),
    ]