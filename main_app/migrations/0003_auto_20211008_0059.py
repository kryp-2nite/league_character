# Generated by Django 3.2.7 on 2021-10-08 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20211008_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultimate', models.CharField(max_length=150)),
                ('skill1', models.CharField(max_length=150)),
                ('skill2', models.CharField(max_length=150)),
                ('health', models.IntegerField(default=0)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='champion', to='main_app.champion')),
            ],
        ),
        migrations.DeleteModel(
            name='Ability',
        ),
    ]
