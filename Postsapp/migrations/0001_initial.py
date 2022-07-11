# Generated by Django 4.0.6 on 2022-07-11 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Majors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('post_point', models.IntegerField()),
                ('is_selcted', models.BooleanField(default=False)),
                ('is_anony', models.BooleanField(default=True)),
                ('show_nickname', models.CharField(max_length=20, null=True)),
                ('image_src', models.CharField(max_length=30, null=True)),
                ('token', models.CharField(max_length=30, null=True)),
                ('major_id', models.ForeignKey(db_column='major_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='majors', to='Postsapp.majors')),
                ('user_id', models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('is_anony', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=30, null=True)),
                ('post_id', models.ForeignKey(db_column='post_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_comment_post', to='Postsapp.posts')),
                ('user_id', models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_comment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
