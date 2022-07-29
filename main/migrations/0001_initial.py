# Generated by Django 4.0.5 on 2022-07-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qaydlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qayd_name', models.CharField(max_length=11)),
                ('reg_Time', models.TimeField()),
                ('maqsad', models.CharField(max_length=40)),
                ('muhim', models.CharField(choices=[('Zarur', 'zarur'), ('Zaruremas', 'zaruremas'), ('Majburi', 'majburi')], max_length=15)),
            ],
        ),
    ]