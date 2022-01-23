# Generated by Django 4.0 on 2022-01-16 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='x', to='products.categoryname'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category_sub_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='y', to='products.categorysubname'),
        ),
    ]
