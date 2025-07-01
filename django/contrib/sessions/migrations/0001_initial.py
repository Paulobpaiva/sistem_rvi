from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
                'db_table': 'django_session',
                'ordering': ('expire_date',),
            },
        ),
    ]
