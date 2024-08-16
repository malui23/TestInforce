Select Date, count(*)
from sample_data
group by Date;

select distinct Domain
from sample_data;

select *
from sample_data
where Date >= now() - interval '7 days';

with topDomain as (
	select Domain as top, 
			count(*) as dc
	from sample_data
	group by Domain
	order by dc desc
	limit 1
)
select *
from sample_data
where Domain = (select top from topDomain);

delete from sample_data
where domain not in ('@gmail.com', '@icloud.com', '@yahoo.com')
