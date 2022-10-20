# Generated by Django 4.0.8 on 2022-10-20 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0050_delete_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name1', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(default=0, upload_to='img')),
                ('Sku', models.CharField(default=0, max_length=30, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('Category_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.category')),
            ],
        ),
    ]