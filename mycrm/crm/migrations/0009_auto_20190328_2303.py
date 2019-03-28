# Generated by Django 2.1.7 on 2019-03-28 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20190324_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='所报课程'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='缴费人'),
        ),
    ]
