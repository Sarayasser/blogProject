# Generated by Django 3.0.3 on 2020-02-26 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0002_forbiddenword'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['Date']},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='userID',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='createTime',
        ),
        migrations.AddField(
            model_name='comments',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='comments',
            name='postID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='admin_page.Post'),
        ),
    ]
