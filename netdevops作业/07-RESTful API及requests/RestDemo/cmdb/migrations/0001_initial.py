# Generated by Django 2.2.10 on 2020-02-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=128, verbose_name='IP')),
                ('mac', models.CharField(max_length=128, verbose_name='mac')),
                ('intf', models.CharField(max_length=128, verbose_name='端口')),
            ],
        ),
    ]
