## Hive Homework 3

### Banklist
- Top 5 states with most banks.
```sql
select b.st st, count(b.bank_name) count from banklist_parquet b
group by b.st
order by count desc
limit 5;
```
<img src="https://github.com/hao5959/python/blob/master/Hadoop/images/q1.1.png" width="50%">

- How many banks close each year.
```sql
select yr, count(closing_date) closing_count from (
    select year(b.closing_date) yr, b.closing_date 
    from banklist_parquet b) a
group by yr;
```
<img src="https://github.com/hao5959/python/blob/master/Hadoop/images/q1.2.png" width="50%">

### Chicago Crime Dataset
- create parquet table partiton by year
```sql
create table crime_parquet_16_20 (
	id bigint,
    case_number string,
    `date` bigint,
    block string,
    IUCR string,
    primary_type string,
    description string,
    loc_desc string,
    arrest boolean,
    domestic boolean,
    bead string,
    district string,
    ward int,
    community_area string,
    FBI_code string,
    x_coordinate int,
    y_coordinate int,
    update_on string,
    latitude float,
    longitude float,
    loc string
)
partitioned by (yr int)
stored as parquet;
```
- import data from 2016 to 2020
```sql
insert into table crime_parquet_16_20 partition (yr=2016) select 
    id,
    case_number,
    `date`,
    block,
    iucr,
    primary_type,
    description,
    loc_desc,
    arrest,
    domestic,
    beat,
    district,
    ward,
    community_area,
    fbi_code,
    x_coordinate,
    y_coordinate,
    updated_on,
    latitude,
    longitude,
    loc
from chicago.crime_parquet where yr = 2016;
```
- 3. Write queries to answer following questions:
  - a. Which type of crime is most occurring for each year?
  ```sql
  select t.primary_type, t.yr, cnt, r from (
	select s.primary_type, s.yr, s.cnt, rank() over(partition by yr order by cnt desc) r from (
		select primary_type, count(*) cnt, yr from crime_parquet_16_20 group by yr, primary_type) s
	) t
  where r <= 10;
  ```
  <img src="https://github.com/hao5959/python/blob/master/Hadoop/images/q2.3.a.png" width="50%">
  
  - b. Which locations are most likely for a crime to happen?  
  ```sql
  select loc_desc, count(*) cnt from crime_parquet_16_20
  group by loc_desc
  order by cnt desc
  limit 10;
  ```
  <img src="https://github.com/hao5959/python/blob/master/Hadoop/images/q2.3.b.png" width="50%">
  
  - c. Are there certain high crime rate locations for certain crime types?
  ```sql
  select loc_desc, ratio, primary_type from (
	select loc_desc, rank() over(partition by loc_desc order by ratio) rank, ratio, primary_type from (
		select x.cnt*100/y.total_cnt ratio, x.loc_desc, x.primary_type from 
			(select loc_desc, primary_type, count(*) cnt from crime_parquet_16_20 group by loc_desc, primary_type) x
		join 
			(select loc_desc, count(*) total_cnt from crime_parquet_16_20 group by loc_desc) y
		on (x.loc_desc = y.loc_desc) 
	) s 
  )t where rank = 1;
  ```
  ```sql
  select loc_desc, primary_type, cnt_rank from (
  select loc_desc, primary_type, rank() over(partition by loc_desc order by ratio) cnt_rank from (
	  select loc_desc, primary_type, round(type_cnt*100/loc_cnt, 2) ratio from (
		select 
			loc_desc, 
			primary_type, 
			count(*) over(partition by loc_desc) loc_cnt,
			count(*) over(partition by loc_desc, primary_type) type_cnt
		from crime_parquet_16_20) s 
	)t 
  ) f where cnt_rank = 1;
  ```
  <img src="https://github.com/hao5959/python/blob/master/Hadoop/images/q2.3.3.png" width="50%">
### Reatil_DB
-1. List all orders with total order_items = 5.
```sql
select o.order_id, sum(oi.order_item_quantity) cnt from orders o
left join order_items oi 
on o.order_id = oi.order_item_order_id
group by o.order_id
having sum(oi.order_item_quantity) = 5;
```
```
return 5806
```
-2/3. List customer_fname，customer_id, order_id, order item_count with total order_items = 5.
```sql
select 
    c.customer_fname customer_fname, 
    c.customer_id customer_id, 
    orders.order_id order_id, 
    oi.order_item_quantity item_count 
FROM 
    customers c
join orders on c.customer_id = orders.order_customer_id
join order_items oi on orders.order_id = oi.order_item_order_id
where orders.order_id in (
    select order_id
    from orders 
    join order_items on orders.order_id = order_items.order_item_order_id
    group by orders.order_id
    having sum(order_item_quantity) = 5
    );
 ```
 ```
 return 14665
 ```
-4. List top 10 most popular product categories.
```sql
select category_name, sum(oi.order_item_quantity) cnt 
from categories c
join products p on p.product_category_id = c.category_id
join order_items oi on oi.order_item_product_id = p.product_id
group by c.category_name
order by cnt desc
limit 10;
```
<img src="https://github.com/hao5959/python/blob/master/Hadoop/images/q3.4.png" width="50%">
-5. List top 10 revenue generating products.

```sql
select 
    sum(order_item_subtotal) revenue,
    p.product_name product_name
from 
    products p
join order_items oi on oi.order_item_product_id = p.product_id
join orders o on o.order_id = oi.order_item_order_id
group by p.product_name
order by revenue desc
limit 10;
```
<img src="https://github.com/hao5959/python/blob/master/Hadoop/images/q3.5.png" width="50%">
