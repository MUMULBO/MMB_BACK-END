# Generated by Django 4.0.3 on 2022-07-10 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Postsapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('is_anony', models.BooleanField(default=False)),
                ('post_id', models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, related_name='fk_comment_post', to='Postsapp.posts')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='fk_comment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
