from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField(verbose_name='action time')),
                ('object_id', models.TextField(verbose_name='object id', blank=True, null=True)),
                ('object_repr', models.CharField(verbose_name='object repr', max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField(verbose_name='action flag')),
                ('change_message', models.TextField(verbose_name='change message', blank=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, to='contenttypes.contenttype', verbose_name='content type')),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to='auth.user', verbose_name='user')),
            ],
            options={
                'verbose_name': 'log entry',
                'verbose_name_plural': 'log entries',
                'db_table': 'django_admin_log',
                'ordering': ('-action_time',),
            },
        ),
    ]
