import sqlalchemy
from sqlalchemy import ForeignKey
metadata = sqlalchemy.MetaData()

#Start and Configuration


#1 Table App Admins
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String, unique=True),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    sqlalchemy.Column("first_name"  , sqlalchemy.String),
    sqlalchemy.Column("last_name"  , sqlalchemy.String),


    sqlalchemy.Column("email"     , sqlalchemy.String, unique=True),
    sqlalchemy.Column("type"     , sqlalchemy.String),
    sqlalchemy.Column("role"     , sqlalchemy.String),

    sqlalchemy.Column("company"     , sqlalchemy.String),
    sqlalchemy.Column("phone"     , sqlalchemy.String, unique=True),
    sqlalchemy.Column("living_home"     , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)


#2 Table Customers
customer  = sqlalchemy.Table(
    "customer",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("country"  , sqlalchemy.String),
    sqlalchemy.Column("code"  , sqlalchemy.String),
    sqlalchemy.Column("ip_address"  , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
)



# 3 Table Movies

movie  = sqlalchemy.Table(
    "movie",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),

    sqlalchemy.Column("title"  , sqlalchemy.String),
    sqlalchemy.Column("summary_description"  , sqlalchemy.String),

    sqlalchemy.Column("movie_year"  , sqlalchemy.String),
    sqlalchemy.Column("movie_month"  , sqlalchemy.String),
    sqlalchemy.Column("movie_day"  , sqlalchemy.String),
    sqlalchemy.Column("poster_path"  , sqlalchemy.String),
    sqlalchemy.Column("type"    , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)

# 4 Table Movie languages
movie_language  = sqlalchemy.Table(
    "movie_language",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),

    sqlalchemy.Column("movie_language"  , sqlalchemy.String),
    sqlalchemy.Column("language_description"  , sqlalchemy.String),


    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)

# 5 Table Movie Genres
movie_genre  = sqlalchemy.Table(
    "movie_genre",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),

    sqlalchemy.Column("movie_genre"  , sqlalchemy.String),
    sqlalchemy.Column("movie_admitted_age"  , sqlalchemy.String),
    sqlalchemy.Column("movie_genre_description"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)


# 6 Table Movie Countries
movie_country  = sqlalchemy.Table(
    "movie_country",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),

    sqlalchemy.Column("movie_country"  , sqlalchemy.String),
    sqlalchemy.Column("movie_country_continent"  , sqlalchemy.String),
    sqlalchemy.Column("movie_country_language"  , sqlalchemy.String),
    sqlalchemy.Column("movie_country_code"  , sqlalchemy.String),
    sqlalchemy.Column("movie_country_description"  , sqlalchemy.String),
    
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)

# 7 Table Movie Actors
movie_actor  = sqlalchemy.Table(
    "movie_actor",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),

    sqlalchemy.Column("actor_name"  , sqlalchemy.String),
    sqlalchemy.Column("actor_birthday"  , sqlalchemy.String),
    sqlalchemy.Column("actor_birthplace"  , sqlalchemy.String),
    sqlalchemy.Column("actor_biography"  , sqlalchemy.String),
    sqlalchemy.Column("actor_image"  , sqlalchemy.String),
    sqlalchemy.Column("actor_role"  , sqlalchemy.String),
    sqlalchemy.Column("actor_status"  , sqlalchemy.String),

    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)

# 8 Table Movie Directors
movie_director  = sqlalchemy.Table(
    "movie_director",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),

    sqlalchemy.Column("director_name"  , sqlalchemy.String),
    sqlalchemy.Column("director_birthday"  , sqlalchemy.String),
    sqlalchemy.Column("director_birthplace"  , sqlalchemy.String),
    sqlalchemy.Column("director_biography"  , sqlalchemy.String),
    sqlalchemy.Column("director_image"  , sqlalchemy.String),
    sqlalchemy.Column("director_role"  , sqlalchemy.String),
    sqlalchemy.Column("director_status"  , sqlalchemy.String),

    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)



# 9 Table Movie streaming
movie_streaming_service  = sqlalchemy.Table(
    "movie_streaming_service",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),

    sqlalchemy.Column("streaming_service_name"  , sqlalchemy.String),
    sqlalchemy.Column("streaming_service_link"  , sqlalchemy.String),
    sqlalchemy.Column("streaming_time"  , sqlalchemy.String),
    sqlalchemy.Column("streaming_quality"  , sqlalchemy.String),

    sqlalchemy.Column("streaming_service_description"  , sqlalchemy.String),
    sqlalchemy.Column("streaming_service_status"  , sqlalchemy.String),

    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)


# 10 Table Movie seasons
season_movie  = sqlalchemy.Table(
    "season_movie",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),

    sqlalchemy.Column("season_name"  , sqlalchemy.String),
    sqlalchemy.Column("season_number"  , sqlalchemy.String),
    sqlalchemy.Column("season_description"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)


# 11 Table Movie seasons episodes
movie_season_episode  = sqlalchemy.Table(
    "movie_season_episode",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),
    sqlalchemy.Column("season_movie_id", sqlalchemy.String, ForeignKey(season_movie.c.id), nullable=False),

    sqlalchemy.Column("episode_name"  , sqlalchemy.String),
    sqlalchemy.Column("episode_number"  , sqlalchemy.String),
    sqlalchemy.Column("episode_description"  , sqlalchemy.String),
    
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)


# 12 Table Movie seasons episodes streaming
movie_season_streaming_service  = sqlalchemy.Table(
    "movie_streaming_service",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("movie_id", sqlalchemy.String, ForeignKey(movie.c.id), nullable=False),
    sqlalchemy.Column("season_movie_id", sqlalchemy.String, ForeignKey(season_movie.c.id), nullable=False),
    sqlalchemy.Column("movie_season_episode_id", sqlalchemy.String, ForeignKey(movie_season_episode.c.id), nullable=False),

    sqlalchemy.Column("streaming_service_name"  , sqlalchemy.String),
    sqlalchemy.Column("streaming_service_link"  , sqlalchemy.String),
    sqlalchemy.Column("streaming_time"  , sqlalchemy.String),
    sqlalchemy.Column("streaming_quality"  , sqlalchemy.String),

    sqlalchemy.Column("streaming_service_description"  , sqlalchemy.String),
    sqlalchemy.Column("streaming_service_status"  , sqlalchemy.String),

    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("updated_at", sqlalchemy.String),
)