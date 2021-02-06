# Generated by Django 3.1.6 on 2021-02-06 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('payment_method', models.CharField(default='Credit card', max_length=100)),
                ('delivery_address', models.CharField(max_length=100)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.good')),
            ],
        ),
    ]
