# Generated by Django 3.0.8 on 2021-06-16 09:14

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=15, null=True, unique=True, verbose_name='username')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(default=' ', max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=50)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pub_date', models.DateField(default=datetime.datetime(2021, 6, 16, 9, 14, 8, 993091, tzinfo=utc))),
                ('header_image', models.ImageField(blank=True, default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DXDKlzbgFcG8&psig=AOvVaw3YCne2m5xc2ipBxTzQSlSn&ust=1604999979875000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJC-_oCR9ewCFQAAAAAdAAAAABAD', upload_to='blog/images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Category')),
                ('likes', models.ManyToManyField(related_name='blogpost', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]