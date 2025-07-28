import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, text
import logging
from ingestion import ingest_db

logging.BasicConfig(
    filename = 'big_project_folder/logs/summary_table.log',
    level = logging.DEBUG,
    format = "%(asctime)s-%(levelname)s-%(message)s",
    filemode = 'a')

def get_summary(conn):
    final_table = pd.read_sql_query(''' WITH customer_table AS (SELECT 
                                                                 c.customer_id,
                                                                 c.first_name,
                                                                 c.last_name,
                                                                 c.email,
                                                                 SUM(o.total_price) as PricePaidPerCustomer,
                                                                 SUM(p.amount) as SumPriceAtPayment,
                                                                 AVG(r.rating) as AverageRating
                                                             FROM customers c
                                                             LEFT JOIN orders o
                                                             ON c.customer_id = o.customer_id
                                                             LEFT JOIN payment p
                                                             ON o.order_id = p.order_id
                                                             LEFT JOIN reviews r
                                                             ON r.customer_id = c.customer_id
                                                             GROUP BY c.customer_id, c.first_name, c.last_name, c.email
                                                             ORDER BY PricePaidPerCustomer  desc),
                                            
                                            order_table AS (SELECT 
                                                                pd.product_id,
                                                                pd.supplier_id,
                                                                r.customer_id,
                                                                AVG(r.rating) AS avg_rating,            
                                                                AVG(oi.price_at_purchase) AS AvgItemPriceAtPurchase,
                                                                oi.order_item_id,
                                                                SUM(oi.quantity) AS TotalQuantity,
                                                                pd.product_name,
                                                                pd.category,
                                                                pd.price
                                                            FROM order_items oi
                                                            RIGHT JOIN products pd ON oi.product_id = pd.product_id
                                                            RIGHT JOIN reviews r ON pd.product_id = r.product_id
                                                            WHERE oi.price_at_purchase > 0
                                                            GROUP BY r.customer_id, pd.product_id, pd.product_name, pd.category, pd.price,
                                                            pd.supplier_id,oi.order_item_id
                                                            ORDER BY AvgItemPriceAtPurchase DESC)
                                        SELECT 
                                            ct.customer_id,
                                            ct.PricePaidPerCustomer,
                                            ct.SumPriceAtPayment,
                                            ot.product_id,
                                            ot.supplier_id,
                                            ot.avg_rating,
                                            ot.AvgItemPriceAtPurchase,
                                            ot.order_item_id,
                                            ot.TotalQuantity,
                                            ot.product_name,
                                            ot.category,
                                            ot.price AS ProductPrice 
                                        FROM customer_table ct
                                        RIGHT JOIN order_table ot
                                        ON ot.customer_id = ct.customer_id
                                        
                                        
                                                            ''',conn)
    return final_table  

def main():
    conn = create_engine("mysql+mysqlconnector://root:Mysqlpswd%40123@localhost:3306/waleeddb")

    logging.info('---getting summary table---')
    table = tget_summary(conn)
    logging.info(get_summary(conn).head())

    logging.info('---Ingestion started---')
    ingest_db(table,'final_table',conn)
    
if __name__ == "__main__":
    main()
    
    
                                        