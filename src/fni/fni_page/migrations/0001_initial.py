# Generated by Django 3.2.15 on 2022-08-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_res', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200, null=True)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
