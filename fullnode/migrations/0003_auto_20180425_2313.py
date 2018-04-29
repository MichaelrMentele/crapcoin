# Generated by Django 2.0.4 on 2018-04-25 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullnode', '0002_remove_peer_last_heard_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='hash_id',
            field=models.CharField(db_index=True, max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='number',
            field=models.IntegerField(db_index=True),
        ),
    ]
