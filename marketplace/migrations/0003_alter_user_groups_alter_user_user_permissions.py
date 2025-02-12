# Generated by Django 5.0.7 on 2024-07-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('marketplace', '0002_user_alter_sale_buyer_alter_sale_seller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='유저의 그룹관리', related_name='marketplace_Users', related_query_name='User', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='유저 권한관리', related_name='marketplace_Users', related_query_name='User', to='auth.permission'),
        ),
    ]
