# Generated by Django 3.0.5 on 2020-04-26 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_set', models.DateTimeField(verbose_name='date set')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]