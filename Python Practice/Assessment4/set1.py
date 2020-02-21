import mysql.connector
import csv

# Connecting Database
mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",db = "assessment4")
cursor = mydb.cursor()

# Inserting values into file
f = open("sale.csv")
rows = csv.reader(f)
for i in rows:
    print(i)
    cursor.execute("insert into sale values (%s,%s,%s,%s)", i)
mydb.commit()

f = open("product.csv")
rows = csv.reader(f)
for i in rows:
    print(i)
    cursor.execute("insert into product values (%s,%s,%s,%s)", i)
mydb.commit()

# To find a Maximum - sold product with product details fetched
cursor.execute("select product_name, product_code, price from (select product_name, product_code, price, dense_rank() over(order by product_quantity desc) as r from product p join sale s on p.id = s.id) as t where r = 1")
max_sold = cursor.fetchall()
print("Maximum - sold product with product details")
print(max_sold)

# To find a Minimum - sold product with product details fetched
cursor.execute("select product_name, product_code, price from (select product_name, product_code, price, dense_rank() over(order by product_quantity) as r from product p join sale s on p.id = s.id) as t where r = 1")
min_sold = cursor.fetchall()
print("Minimum - sold product with product details")
print(min_sold)

# To Get the billing date from user and print the product details and total amount of displaying products
date_inp = input("Enter a date : ")
cursor.execute("select product_name, product_code, price*product_quantity as total_amount from product p join sale s on p.id = s.id where bill_date = %s",(date_inp,))
bill_dates = cursor.fetchall()
print(bill_dates)

# To Get the product code from user and check it in product table
prod_code = input("Enter a product code : ")
cursor.execute("select product_name, product_code, price from product where product_code = %s",(prod_code,))
product_codes = cursor.fetchall()
print(product_codes)

# Add some products to product table
cursor.execute("insert into product values (4,'Lenovo', 'Idepad S145', 44500)")
mydb.commit()

f.close()
mydb.close()
