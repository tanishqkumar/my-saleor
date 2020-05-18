# Generated by Django 2.2.6 on 2020-04-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('type', models.CharField(max_length=256, null=True)),
                ('bio', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
