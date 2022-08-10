# Generated by Django 3.2.4 on 2022-06-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("node_man", "0059_auto_20220415_2150"),
    ]

    operations = [
        migrations.AddField(
            model_name="host",
            name="os_version",
            field=models.CharField(
                blank=True, default="", max_length=32, null=True, db_index=True, verbose_name="操作系统版本"
            ),
        ),
    ]