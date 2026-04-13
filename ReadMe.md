
# Data Pipeline Project

## Overview

This project simulates an end-to-end data pipeline that ingests raw customer, order, and order item data, applies validation and transformation logic, and loads the cleaned data into a PostgreSQL database. Analytical and data quality views are created for downstream analysis.


##  Prerequisites

Ensure the following are installed on your local machine:

### 1. Python 3.10+

Check your version:

```
python --version
```

If not installed, install as follows:

#### Ubuntu/Linux

```
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

#### Windows
Download from: https://www.python.org/downloads/


### 2. PostgreSQL

Ensure PostgreSQL is installed and running.

The default postrgres database is used in this exercise and the credentials to the database aare stored in ```config.yaml`` file.


## Setup Instructions
1. Clone the repository
```
git clone https://github.com/Wamolambo/pizza_orders.git
cd pizza_orders
```

2. Create a virtual environment:

On Linux

```
python3 -m venv etl_env source etl_env/bin/activate
```

On Windows Powershell
```
py -3.10 -m venv etl_env
.\etl_env\Scripts\Activate.ps1
```

3. Install dependencies
```
pip install -r requirements.txt
```

## Configuration

Edit the config.yaml file to match your local database setup:

```
database:
  host: localhost
  port: 5432
  dbname: orders_db
  user: your_user
  password: your_password
```

## Running the Pipeline

### 1. Initialize database schema

```
python main.py init
```

### 2. Run the ETL pipeline

```
python main.py run
```


## Output
After running the pipeline:

- Data will be loaded into
   - customers
   - orders
   - order_items
- Logs will be available
   - In the terminal
