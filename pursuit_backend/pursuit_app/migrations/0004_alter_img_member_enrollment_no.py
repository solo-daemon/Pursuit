# Generated by Django 4.1.1 on 2022-09-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pursuit_app', '0003_alter_img_member_options_alter_img_member_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img_member',
            name='enrollment_no',
            field=models.PositiveIntegerField(unique=True, verbose_name='enrollemnt no'),
        ),
    ]
