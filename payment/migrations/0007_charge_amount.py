# Generated by Django 2.2.7 on 2019-11-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_invoiceitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='amount',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
