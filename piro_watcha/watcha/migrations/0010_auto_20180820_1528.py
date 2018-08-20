# Generated by Django 2.1 on 2018-08-20 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watcha', '0009_comment_star'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='평점')),
                ('star', models.IntegerField(blank=True, null=True, verbose_name='별점 매기기')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='star',
            field=models.IntegerField(blank=True, null=True, verbose_name='별점 매기기'),
        ),
    ]
