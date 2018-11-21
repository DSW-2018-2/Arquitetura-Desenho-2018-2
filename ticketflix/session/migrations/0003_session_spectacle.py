# Generated by Django 2.0.8 on 2018-11-19 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spectacle', '0001_initial'),
        ('session', '0002_auto_20181119_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='spectacle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sessions', related_query_name='session', to='spectacle.Spectacle'),
        ),
    ]
