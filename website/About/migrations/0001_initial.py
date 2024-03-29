# Generated by Django 2.2.5 on 2019-09-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('organisation_structure', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
            options={
                'verbose_name_plural': 'About Company',
                'ordering': ['-created_on'],
            },
        ),
    ]
