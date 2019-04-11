## Hive Pre Exercise

### 1. Which customer did your query identify as the winner of the $5,000 prize?
```
SELECT *
  FROM customers
 WHERE fname LIKE 'Bridget%'
   AND city = 'Kansas City'
```
![Image of Hive Exercise 1](hive-exercise-1-1.png)

### 2. Execute a query that displays the three most expensive products.
```
[localhost.localdomain:21000] > SELECT * FROM products ORDER BY price DESC LIMIT 3;
Query: select * FROM products ORDER BY price DESC LIMIT 3
+---------+------------+-----------------------------------------------+--------+--------+-------------+
| prod_id | brand      | name                                          | price  | cost   | shipping_wt |
+---------+------------+-----------------------------------------------+--------+--------+-------------+
| 1274321 | Byteweasel | Hadoop Cluster, Economy (4-node)              | 975149 | 952934 | 570         |
| 1274308 | Gigabux    | Server (2U rackmount, eight-core, 64GB, 12TB) | 614559 | 556183 | 121         |
| 1274307 | Krustybitz | Server (2U rackmount, eight-core, 64GB, 12TB) | 599319 | 542497 | 121         |
+---------+------------+-----------------------------------------------+--------+--------+-------------+
Fetched 3 row(s) in 0.56s
```

### 3. Execute the script using the shell's -f option.
```
[training@localhost queries]$ impala-shell -f verify_tablet_order.sql
Starting Impala Shell without Kerberos authentication
Connected to localhost.localdomain:21000
Server version: impalad version 2.6.0-cdh5.8.0 RELEASE (build 8d8652f69461f0dd8d5f474573fb5de7ceb0ee6b)
Query: -- Query to find the order for the
-- tablet (product ID 1274348) from the
-- contest winner (customer ID 1139477)
SELECT o.order_id, fname, lname, o.order_date
FROM customers c
JOIN orders o
   ON (c.cust_id = o.cust_id)
JOIN order_details d
   ON (o.order_id = d.order_id)
WHERE d.prod_id=1274348
  AND c.cust_id=1139477
+----------+---------+-------+---------------------+
| order_id | fname   | lname | order_date          |
+----------+---------+-------+---------------------+
| 6662689  | Bridget | Burch | 2013-05-31 17:31:11 |
| 6621368  | Bridget | Burch | 2013-05-20 21:17:03 |
+----------+---------+-------+---------------------+
Fetched 2 row(s) in 10.37s
```
Did Bridget order the advertised tablet in May? **Yes**

### 4. Execute a query to find all the Gigabux brand products whose price is less than 1000(less than $10)
```
0: jdbc:hive2://localhost:10000> SELECT * FROM products WHERE brand = 'Gigabux' and price < 1000;
INFO  : Compiling command(queryId=hive_20190410214343_8c41378a-8d3f-4b50-9423-2b27ee136647): SELECT * FROM products WHERE brand = 'Gigabux' and price < 1000
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:products.prod_id, type:int, comment:null), FieldSchema(name:products.brand, type:string, comment:null), FieldSchema(name:products.name, type:string, comment:null), FieldSchema(name:products.price, type:int, comment:null), FieldSchema(name:products.cost, type:int, comment:null), FieldSchema(name:products.shipping_wt, type:int, comment:null)], properties:null)
INFO  : Completed compiling command(queryId=hive_20190410214343_8c41378a-8d3f-4b50-9423-2b27ee136647); Time taken: 0.084 seconds
INFO  : Executing command(queryId=hive_20190410214343_8c41378a-8d3f-4b50-9423-2b27ee136647): SELECT * FROM products WHERE brand = 'Gigabux' and price < 1000
INFO  : Completed executing command(queryId=hive_20190410214343_8c41378a-8d3f-4b50-9423-2b27ee136647); Time taken: 0.001 seconds
INFO  : OK
+-------------------+-----------------+----------------------------------------------------------+-----------------+----------------+-----------------------+--+
| products.prod_id  | products.brand  |                      products.name                       | products.price  | products.cost  | products.shipping_wt  |
+-------------------+-----------------+----------------------------------------------------------+-----------------+----------------+-----------------------+--+
| 1273740           | Gigabux         | Batteries (AA, 4 pack)                                   | 669             | 481            | 2                     |
| 1273759           | Gigabux         | Batteries (D, 2 pack)                                    | 959             | 353            | 2                     |
| 1273904           | Gigabux         | 1/4 in. Standard Phone Female to Female Adapter          | 399             | 397            | 1                     |
| 1273906           | Gigabux         | 1/4 in. Standard Phone Female to Female Adapter          | 399             | 229            | 1                     |
| 1273918           | Gigabux         | RCA Phono Male to Mini Female Adapter                    | 419             | 198            | 1                     |
| 1273920           | Gigabux         | RCA Phono Male to Mini Female Adapter                    | 409             | 404            | 1                     |
| 1273932           | Gigabux         | RCA Phono Male to 1/4 in. Standard Phone Female Adapter  | 629             | 579            | 1                     |
| 1273941           | Gigabux         | 3-Pin XLR Male to Male, Barrel Adapter                   | 749             | 551            | 1                     |
| 1273994           | Gigabux         | Phono Jack to UHF Plug                                   | 619             | 316            | 1                     |
| 1273996           | Gigabux         | Phono Jack to F Plug                                     | 509             | 470            | 1                     |
+-------------------+-----------------+----------------------------------------------------------+-----------------+----------------+-----------------------+--+
10 rows selected (0.159 seconds)
```
