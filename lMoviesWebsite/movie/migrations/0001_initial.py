# Generated by Django 4.2.6 on 2023-10-14 02:30

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('counrty', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2000)),
                ('alias', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=150)),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
                ('original_country', django_countries.fields.CountryField(max_length=2)),
                ('language', models.CharField(max_length=255)),
                ('trailer', models.URLField(max_length=1000)),
                ('poster_image', models.ImageField(upload_to='')),
                ('box_office', models.DecimalField(decimal_places=2, max_digits=6)),
                ('production_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movie.company')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=255)),
                ('born_in', django_countries.fields.CountryField(max_length=2)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('preffered_language', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2)),
                ('note', models.CharField(max_length=2000)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserPeopleFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.people')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserMovieFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserGenreFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.genre')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=100)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.user')),
            ],
        ),
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.genre')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('actor_name', models.CharField(max_length=255)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.people')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movie.companytype'),
        ),
    ]
