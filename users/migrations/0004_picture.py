# Generated by Django 3.2.10 on 2021-12-30 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211218_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='defualt.jpa', upload_to='item_pics')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.item')),
            ],
        ),
    ]
