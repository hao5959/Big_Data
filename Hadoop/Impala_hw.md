## Impala Assignments

### Banklist
- Top 5 states with most banks.
- How many banks close each year.
```sql
select year(closing_date) yr, count(closing_date) cnt from hao_db.banklist_parquet
group by yr
order by yr;
```

### Chicago Crime Dataset:
- create a partitioned table (partition by year)
- insert values from 2016 to 2020.
```sql
insert into table hao_db.crime_parquet_16_20_impala partition (yr) select 
    id,
    case_number,
    `date`,
    block ,
    IUCR,
    primary_type,
    description,
    loc_desc,
    arrest,
    domestic,
    beat,
    district,
    ward,
    community_area,
    FBI_code,
    x_coordinate,
    y_coordinate,
    updated_on,
    latitude,
    longitude,
    loc,
    yr
from chicago.crime_parquet where yr between 2016 and 2020;
```

- 3. Write queries to answer following questions:
  - a. Which type of crime is most occurring for each year?
  - b. Which locations are most likely for a crime to happen?
  - c. Are there certain high crime rate locations for certain crime types?

### Retail_DB
-1. List all orders with total order_items = 5.