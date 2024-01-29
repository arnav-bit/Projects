select * from dbo.director_mapping
select * from dbo.genre
select * from dbo.movies
select * from dbo.[names]
select * from dbo.ratings
select * from dbo.role_mapping

select id from dbo.movies
group by id
having count(id) > 1

-- number of movies by years


SELECT count(distinct id), year from dbo.movies
group by [year]

select * from dbo.movies

-- tracking duration by years and duration by country--

select count(id) as NbOfFilms, avg(cast(duration as int)) as AvgDuration, year from dbo.movies
group by [year] 

-- number of films by country
select count(id), country from dbo.movies
group by country
order by count(id) desc

-- average duration by country
select count(id) as NbofFilms, avg(cast(duration as int)) as AvgDuration, country from dbo.movies
group by country
order by 1 desc

-- using genre now, also use worldwide income, duration, country, etc

select * from dbo.movies
select * from dbo.genre

-- duration by genre --
select count(mov.id) as NbFilms, avg(cast(mov.duration as int)) as AvgDuration, gen.genre from dbo.movies mov left join dbo.genre gen on mov.id = gen.movie_id 
where gen.movie_id is not null
group by gen.genre
order by 1 desc

-- income by year
select year, sum(cast(substring(worlwide_gross_income, 3, 20) as bigint)) from dbo.movies
where worlwide_gross_income is not null
group by year

-- income by genre --
select count(mov.id) as NbFilms, gen.genre, sum(cast(substring(worlwide_gross_income, 3, 20) as bigint)) as Revenue from dbo.movies mov inner join dbo.genre gen on mov.id = gen.movie_id
where mov.worlwide_gross_income is not null
group by gen.genre
order by 1 desc

-- names and role mappings --

select * from dbo.[names]
select * from dbo.role_mapping
select * from dbo.movies

-- select * from dbo.[names] names inner join dbo.role_mapping maps on names.id = maps.name_id inner join 

create view movie_actor_mapping as
select mov.id, mov.title, mov.[year], mov.duration, mov.country, mov.worlwide_gross_income, mov.languages, names.name, maps.category, names.date_of_birth from dbo.movies mov inner join dbo.role_mapping maps on mov.id = maps.movie_id inner join dbo.[names] names on names.id = maps.name_id
where mov.worlwide_gross_income is not null
;

drop view movie_actor_mapping

select * from movie_actor_mapping


-- actors with highest gross incomes --

select sum(cast(substring(worlwide_gross_income, 3, 20) as bigint)) as Revenue, name from movie_actor_mapping
where category in ('actor', 'actress')
group by name
order by 1 desc


-- actors/director split
select category, count(*) from movie_actor_mapping
group by

select a.country, b.name as Name , count(*) as count from movie_actor_mapping a join movie_actor_mapping b on a.id = b.id
group by a.country, b.name
order by 3 desc

-- rating and movies

select * from dbo.movies
select * from dbo.ratings

-- highest rating movies
select mov.title, rat.avg_rating, mov.country, mov.worlwide_gross_income from dbo.movies mov inner join dbo.ratings rat on mov.id = rat.movie_id
where mov.worlwide_gross_income is not NULL
order by 2 desc


-- average rating per year, per genre, per actor, per something too

select mov.[year], avg(cast(rat.avg_rating AS float)) as average from dbo.movies mov inner join dbo.ratings rat on mov.id = rat.movie_id
where mov.worlwide_gross_income is not NULL
group by mov.[year]

select avg(cast(rat.avg_rating AS float)) as average from dbo.movies mov inner join dbo.ratings rat on mov.id = rat.movie_id
where mov.worlwide_gross_income is not NULL
group by mov.[year]

--average rating by actors
select map.name, avg(cast(rat.avg_rating as float)) as AvgRatingActors from movie_actor_mapping map inner join dbo.ratings rat ON map.id = rat.movie_id
group by map.name
order by 2 desc
