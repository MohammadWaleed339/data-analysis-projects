# Online Store Data Analysis Project 📊

This is a data analysis project based on an online store dataset, which includes several CSV files. The analysis is performed using SQL, Python, and Power BI, with proper logging and clean code practices.

## Introduction ℹ️

This project dives deep into the data provided by an online store to extract insights about customers, products, delivery partners, and suppliers. The data is first extracted from a MySQL server using SQLAlchemy. Relevant tables are queried to gather topic-specific information, and a final SQL query combines all data into a single table called `final_table`. This consolidated table is then used for exploratory data analysis (EDA) and visualization. Power BI is used to showcase key findings through an interactive dashboard.

## Data 📅

The dataset includes the following files:

- `customer.csv`
- `order_items.csv`
- `orders.csv`
- `payment.csv`
- `products.csv`
- `reviews.csv`
- `shipments.csv`
- `suppliers.csv`
- `final_table.csv`  
  *(An aggregated table containing relevant information used for EDA and visualization.)*

## Project Structure 🗂️

The project is organized as follows:

store-data-analysis/
├── datasets/                         # Raw or processed data files
├── logs/                             # Contains only log files
│   ├── LoadingToSql.log              # Log file for SQL loading process
│   ├── SummaryTable.log              # Log file for summary table generation
├── Dashboard-store-analysis.pbix     # Power BI dashboard file
├── EDA.ipynb                         # Exploratory Data Analysis notebook
├── LoadingToSql.ipynb                # Notebook for loading data into SQL
├── README.md                         # Project overview and instructions
├── VisualisationAndTesting.ipynb     # Notebook for visualization and testing
├── ingestion.py                      # Python script for data ingestion
├── summary_table.py                  # Script for generating summary tables


## Tools & Libraries Used 🧰

The following technologies and libraries were used:

- **SQL**: Data extraction and transformation
- **Python**:
  - `SQLAlchemy` for database connection
  - `pandas` for data manipulation
  - `matplotlib` & `seaborn` for visualization
  - `logging` for tracking execution
- **Power BI**: Dashboard creation and data storytelling
- **MySQL**: Source database

## Objective 🎯

The objective of this analysis is to:

- Identify the best and worst performing suppliers
- Highlight customers who contribute most to revenue
- Determine the most reliable and efficient delivery partners
- Discover products that generate significant revenue

The intent is to uncover bottlenecks and inefficiencies in the store's operations and provide actionable suggestions to increase revenue and minimize losses.

## Results Summary 📈

Key insights from the analysis include:

- 🏆 **Top Suppliers**: A few suppliers consistently deliver high-quality products with minimal delays.
- 🚫 **Underperforming Suppliers**: Certain suppliers have high return rates and poor customer reviews.
- 💰 **High-Value Customers**: A small segment of customers contributes disproportionately to total revenue.
- 🚚 **Reliable Delivery Partners**: One delivery partner stands out with the fastest and most consistent delivery times.
- 📦 **Revenue-Generating Products**: A handful of products account for a large portion of sales, suggesting potential for focused marketing.

## Next Steps 🔄

- Automate data refresh and dashboard updates
- Integrate predictive analytics for demand forecasting
- Expand analysis to include seasonal trends and regional performance



