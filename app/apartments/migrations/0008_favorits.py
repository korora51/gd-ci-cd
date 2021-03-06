# Generated by Django 3.0.6 on 2020-06-15 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apartments', '0007_auto_20200608_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apartments.Apartments')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
