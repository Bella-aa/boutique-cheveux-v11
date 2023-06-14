# Generated by Django 3.2.19 on 2023-06-14 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('content', models.CharField(max_length=500, null=True)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_reviewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviewed', to='products.product')),
                ('user_reviewing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviewing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
