# Generated by Django 2.2.7 on 2019-11-15 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20191115_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='referral_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ReferralCode'),
        ),
    ]