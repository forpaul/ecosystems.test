# Generated by Django 2.1.7 on 2019-02-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0004_auto_20190217_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesses',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
