# Generated by Django 5.1.3 on 2024-11-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pipeline_CICD', '0002_remove_pipeline_created_at_pipeline_last_run_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
