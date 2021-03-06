# Generated by Django 3.0 on 2020-01-17 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('RN', 'RANDOM'), ('SC', 'SCIENCE'), ('TG', 'TECHNOLOGY'), ('FD', 'FOOD'), ('AR', 'ART'), ('LT', 'LITERATURE'), ('PH', 'PHILOSOPHY'), ('MM', 'MUSIC&MOVIES'), ('TS', 'TVSERIES'), ('GM', 'GAMES')], default='RN', max_length=2),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('is_upvote', models.BooleanField(default=True)),
                ('voted_at', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
