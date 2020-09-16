## Hive Homework 3

### Banklist
- Top 5 states with most banks.
```sql
select b.st st, count(b.bank_name) count from banklist_parquet b
group by b.st
order by count desc
limit 5;
```
