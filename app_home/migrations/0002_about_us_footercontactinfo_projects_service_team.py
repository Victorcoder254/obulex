# Generated by Django 5.1 on 2024-08-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_1', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_heading_1', models.CharField(blank=True, max_length=100, null=True)),
                ('description_1', models.CharField(blank=True, max_length=350, null=True)),
                ('year_2', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_heading_2', models.CharField(blank=True, max_length=100, null=True)),
                ('description_2', models.CharField(blank=True, max_length=350, null=True)),
                ('year_3', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_heading_3', models.CharField(blank=True, max_length=100, null=True)),
                ('description_3', models.CharField(blank=True, max_length=350, null=True)),
                ('year_4', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_heading_4', models.CharField(blank=True, max_length=100, null=True)),
                ('description_4', models.CharField(blank=True, max_length=350, null=True)),
                ('last_edited', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FooterContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('twitter', models.URLField(blank=True, max_length=500, null=True)),
                ('facebook', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=500, null=True)),
                ('termsofservice', models.CharField(blank=True, max_length=1000, null=True)),
                ('privacypolicy', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name_1', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_1', models.CharField(blank=True, max_length=150, null=True)),
                ('description_1', models.CharField(blank=True, max_length=500, null=True)),
                ('project_name_2', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_2', models.CharField(blank=True, max_length=150, null=True)),
                ('description_2', models.CharField(blank=True, max_length=500, null=True)),
                ('project_name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_3', models.CharField(blank=True, max_length=150, null=True)),
                ('description_3', models.CharField(blank=True, max_length=500, null=True)),
                ('last_edited', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(blank=True, max_length=100, null=True)),
                ('description_1', models.CharField(blank=True, max_length=150, null=True)),
                ('name_2', models.CharField(blank=True, max_length=100, null=True)),
                ('description_2', models.CharField(blank=True, max_length=150, null=True)),
                ('name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('description_3', models.CharField(blank=True, max_length=150, null=True)),
                ('name_4', models.CharField(blank=True, max_length=100, null=True)),
                ('description_4', models.CharField(blank=True, max_length=150, null=True)),
                ('last_edited', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(blank=True, max_length=100, null=True)),
                ('title_1', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_1', models.URLField(blank=True, max_length=500, null=True)),
                ('facebook_1', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin_1', models.URLField(blank=True, max_length=500, null=True)),
                ('name_2', models.CharField(blank=True, max_length=100, null=True)),
                ('title_2', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_2', models.URLField(blank=True, max_length=500, null=True)),
                ('facebook_2', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin_2', models.URLField(blank=True, max_length=500, null=True)),
                ('name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('title_3', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_3', models.URLField(blank=True, max_length=500, null=True)),
                ('facebook_3', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin_3', models.URLField(blank=True, max_length=500, null=True)),
                ('last_edited', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
