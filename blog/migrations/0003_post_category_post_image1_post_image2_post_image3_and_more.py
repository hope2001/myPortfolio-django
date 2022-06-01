# Generated by Django 4.0.2 on 2022-04-08 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0006_portfolio_youtube_video_link_and_more'),
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='showcase.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploaded/blog/img'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploaded/blog/img'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploaded/blog/img'),
        ),
        migrations.AddField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploaded/blog/img'),
        ),
        migrations.AddField(
            model_name='post',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploaded/blog/img'),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url3',
            field=models.URLField(blank=True, null=True),
        ),
    ]
