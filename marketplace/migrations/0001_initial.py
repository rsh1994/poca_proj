# Generated by Django 5.0.7 on 2024-07-17 05:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.DecimalField(decimal_places=2, default=10000.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.CharField(choices=[('sale', '판매중'), ('sold', '판매완료')], default='sale', max_length=10)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('renewal_date', models.DateTimeField(auto_now=True)),
                ('sold_date', models.DateTimeField(blank=True, null=True)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='marketplace.customer')),
                ('photo_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.photocard')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='marketplace.customer')),
            ],
        ),
    ]
