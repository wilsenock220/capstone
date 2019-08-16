# Generated by Django 2.2.4 on 2019-08-16 06:23

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentunit',
            name='deposit',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='IDR', max_digits=14),
        ),
        migrations.AlterField(
            model_name='apartmentunit',
            name='rent_per_month',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='IDR', max_digits=14),
        ),
        migrations.AlterField(
            model_name='apartmentunit',
            name='rent_per_year',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='IDR', max_digits=14),
        ),
        migrations.AlterField(
            model_name='house',
            name='deposit',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='IDR', max_digits=14),
        ),
        migrations.AlterField(
            model_name='house',
            name='rent_per_month',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='IDR', max_digits=14),
        ),
        migrations.AlterField(
            model_name='house',
            name='rent_per_year',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='IDR', max_digits=14),
        ),
    ]