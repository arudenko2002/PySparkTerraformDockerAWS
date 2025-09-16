a="""
a
id (1, 2, 3)
b
id (1,2,3, 5)

c id (1,1,1)
d id (1,1,1,1)

transaction table
#transaction_id
#customer_id

order table
#order_id
#customer id
#order date
#deliver date
#amount
#payment status

select order_id, count(order_id) as coun
from orders
group by order_id
having count(order_id) > 1

select order_id, number from (
select order_id, count(order_id) over(partition by order_id) as number
from orders
) t
where number>1

select a join
"""
b = """

select user_id --, count(user_id) as coun
from user_history
group by user_id
having count(user_id) > 1;

select distinct user_id from (
select user_id, date, count(user_id) over(partition by user_id) as number
from user_history
) t
where number>1;

insert into user_history (user_id, date, action) values (1, Convert(datetime, '2025-03-01 00:00:00',121), 'logged_on');

"""
