# Generated by Django 5.1.3 on 2024-11-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_acno', models.IntegerField()),
                ('cust_name', models.CharField(max_length=100)),
                ('loan_amt', models.FloatField()),
                ('loan_type', models.CharField(max_length=100)),
            ],
        ),
    ]
