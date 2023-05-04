# Generated by Django 4.1.7 on 2023-05-04 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0001_initial'),
        ('statuses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authored_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executed_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(blank=True, default=None, to='labels.label'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.status'),
        ),
    ]