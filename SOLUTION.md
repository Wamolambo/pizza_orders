# Data Engineering Assignment – Solution

## Overview

This project implements an end-to-end data pipeline that ingests raw data from .CSV and Json files. The ingested data is than transformed and validated before it is loaded into tables in a PostgreSQL database. Furthermore, views are used to gain analytic insight such as the top N customers and perform data quality checks such as flagging orders that are not tied to a customer.

The system is illustrated as follows:

<p align="center">
  <img src="img/etl.png" alt="ETL process" width="1000" height="600">
</p>

## Project structure

The pipeline code was written in a modular pattern so that it can be better maintain, exepended and debugged.

The file structure is illustrated below:

```
pipeline/
├── main.py                 # Entry point (init, run)
├── config.yaml             # Configuration (DB + file paths)
├── db/
│   └── schema.sql          # Table definitions
├── etl/
│   ├── extract.py          # Data ingestion
│   ├── transform.py        # Data cleaning and validation
│   └── load.py             # Data loading
├── utils/
│   ├── db.py               # Database connection
│   └── logger.py           # Logging setup
├── sql/
│   └── views.sql           # Analytics and data quality views      
├── pipeline.log          
└── README.md               # Runtime logs
```