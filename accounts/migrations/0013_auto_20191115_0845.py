# Generated by Django 2.2.7 on 2019-11-15 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_referralcodes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReferralCodes',
            new_name='ReferralCode',
        ),
    ]