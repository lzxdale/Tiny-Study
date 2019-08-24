# Generated by Django 2.2.4 on 2019-08-24 03:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyIPTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=64)),
                ('port', models.CharField(max_length=8)),
                ('valid', models.BooleanField(max_length=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('other', models.CharField(max_length=256)),
            ],
        ),
    ]
