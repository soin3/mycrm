# Generated by Django 2.1.7 on 2019-03-24 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20190324_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='合同名称')),
                ('template', models.TextField()),
            ],
            options={
                'verbose_name': ' Contract合同表',
                'verbose_name_plural': 'Contract合同表',
            },
        ),
        migrations.AlterModelOptions(
            name='classlist',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='classlist',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Contract'),
        ),
    ]
