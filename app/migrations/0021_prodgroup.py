# Generated by Django 4.0.4 on 2022-10-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_delete_p_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_group_code', models.IntegerField()),
                ('p_group_name', models.CharField(max_length=70)),
                ('p_group_description', models.CharField(max_length=200)),
            ],
        ),
    ]