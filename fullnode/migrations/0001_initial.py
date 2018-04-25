# Generated by Django 2.0.4 on 2018-04-25 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.CharField(max_length=1024)),
                ('payee', models.CharField(max_length=1024)),
                ('amount', models.IntegerField()),
                ('signature', models.CharField(max_length=1024)),
                ('number', models.IntegerField()),
                ('previous_hash', models.CharField(max_length=1024)),
                ('nonce', models.CharField(max_length=1024)),
                ('hash_id', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('host', models.CharField(max_length=80)),
                ('method', models.CharField(max_length=10)),
                ('uri', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('status_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
