# Generated by Django 3.1.5 on 2022-06-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=10)),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.CharField(max_length=10)),
                ('bname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=5)),
                ('cname', models.CharField(max_length=75)),
                ('branch', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('pswrd', models.CharField(max_length=50)),
            ],
        ),
    ]
