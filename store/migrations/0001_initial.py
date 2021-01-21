# Generated by Django 3.1.5 on 2021-01-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('LAP', 'Laptop'), ('DESK', 'Desktop'), ('MOB', 'Mobile Phone'), ('TAB', 'Tablet Phone'), ('MTR', 'Monitor'), ('TV', 'Television')], max_length=5)),
                ('released_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
