# Generated by Django 4.1.4 on 2023-05-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('stock', models.IntegerField(verbose_name='Quantidade em estoque')),
            ],
        ),
    ]
