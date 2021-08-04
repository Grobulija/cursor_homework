# Generated by Django 3.2.5 on 2021-08-03 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('metadata', models.TextField(blank=True, null=True)),
                ('url', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('passenger', 'Passenger'), ('truck', 'Truck'), ('special', 'Special')], max_length=20)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.brand', verbose_name='models')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(choices=[('straight', 'Straight engine'), ('inline', 'Inline engine'), ('v', 'V engine'), ('flat', 'Flat engine')], default='straight', max_length=30)),
                ('pollutant_class', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G')], default='a', max_length=5)),
                ('price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('fuel_type', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('gasoline', 'Gasoline')], default='petrol', max_length=20)),
                ('status', models.CharField(choices=[('for sale', 'For sale'), ('sold', 'Sold'), ('archived', 'Archived')], default='for sale', max_length=10)),
                ('doors', models.PositiveSmallIntegerField(default=4)),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=3)),
                ('gear_case', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic'), ('variable', 'Variable'), ('semi-automatic', 'Semi-automatic')], default='manual', max_length=20)),
                ('number', models.CharField(max_length=15)),
                ('slug', models.SlugField(max_length=60)),
                ('sitting_place', models.PositiveSmallIntegerField(default=5)),
                ('first_registration_date', models.DateTimeField(auto_now_add=True)),
                ('engine_power', models.PositiveSmallIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.color')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='dealers.dealer')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.model')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.picture')),
                ('property', models.ManyToManyField(to='cars.Property')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]