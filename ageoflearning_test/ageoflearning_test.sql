select running_level,round(avg(score),2) as avg_score from (
select user_id, title, CAST(score as DECIMAL(6,2)) as score, sum(level_change) over(partition by user_id order by timestamp) as running_level from
(
	select timestamp,user_id, JSON_EXTRACT(info, '$.title') as title,  JSON_EXTRACT(info, '$.score') as score,
	case
	when event_name='level_change'
	THEN JSON_EXTRACT(info, '$.level_change')
	ELSE 0
	END as level_change
	from eol_events
) t
) ttt
where score is not NULL and title='terror_turtles'
group by running_level
;

with user_level3 as (
		select user_id from (
		select user_id, title, CAST(score as DECIMAL(6,2)) as score, sum(level_change) over(partition by user_id order by timestamp) as running_level from
		(
			select timestamp,user_id, JSON_EXTRACT(info, '$.title') as title,  JSON_EXTRACT(info, '$.score') as score,
			case
			when event_name='level_change'
			THEN JSON_EXTRACT(info, '$.level_change')
			ELSE 0
			END as level_change
			from eol_events
		) t
		) tt
		where running_level=3
		group by user_id
)
select game from (
	select JSON_EXTRACT(info, '$.title') as game, count(event_id) as count from eol_events e
	join user_level3 u on e.user_id=u.user_id
	group by JSON_EXTRACT(info, '$.title')
) t
order by t.count desc
LIMIT 1
;


with game_user_level3_pair as
      (
      	-- solution from 1.:  added the column with current user level to each record
		select user_id, title from (
		select user_id, title, CAST(score as DECIMAL(6,2)) as score, sum(level_change) over(partition by user_id order by timestamp) as running_level from
		(
			select timestamp,user_id, JSON_EXTRACT(info, '$.title') as title,  JSON_EXTRACT(info, '$.score') as score,
			case
			when event_name='level_change'
			THEN JSON_EXTRACT(info, '$.level_change')
			ELSE 0
			END as level_change
			from eol_events
		) t
		) tt
		where running_level=3
		group by user_id, title

      ),
    games_count as
    (
		select JSON_EXTRACT(info, '$.title') as title, count(event_id) count from eol_events e
		  join game_user_level3_pair g on title=JSON_EXTRACT(info, '$.title') and e.user_id=g.user_id
		group by JSON_EXTRACT(info, '$.title')
    )
    select title from games_count
    order by count desc
    LIMIT 1;