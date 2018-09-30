# Generated by Django 2.1.1 on 2018-09-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название супа')),
                ('photo', models.ImageField(blank=True, default='', upload_to='soups/photo', verbose_name='фото')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='адрес url')),
            ],
            options={
                'verbose_name': 'меню на главной',
                'verbose_name_plural': 'меню на главной',
            },
        ),
        migrations.CreateModel(
            name='Rolls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название ролла')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('photo', models.ImageField(blank=True, default='', upload_to='rolls/photo', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'ролл',
                'verbose_name_plural': 'роллы',
            },
        ),
        migrations.CreateModel(
            name='Sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название сета')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('photo', models.ImageField(blank=True, default='', upload_to='sets/photo', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'сет',
                'verbose_name_plural': 'сеты',
            },
        ),
        migrations.CreateModel(
            name='Soups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название супа')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('photo', models.ImageField(blank=True, default='', upload_to='soups/photo', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'суп',
                'verbose_name_plural': 'супы',
            },
        ),
        migrations.CreateModel(
            name='Sushi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название суши')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('photo', models.ImageField(blank=True, default='', upload_to='sushi/photo', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'суши',
                'verbose_name_plural': 'суши',
            },
        ),
    ]
