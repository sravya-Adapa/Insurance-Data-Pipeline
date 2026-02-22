# Insurance Data Pipeline & Business Dashboard

## Project Overview

This project builds an end-to-end insurance data pipeline using a modern analytics stack.
The workflow includes:
* Generating synthetic insurance data using Python and Faker
* Storing the data in MongoDB
* Ingesting raw data into Snowflake
* Transforming the data using dbt
* Building a business dashboard in Power BI

## Architecture

Python → MongoDB → Snowflake → dbt → Power BI

## Data Generation

Insurance customer and claim data is generated using Python and Faker.
Each record includes:
* Customer information
* Policy type
* Claim ID
* Claim date
* Claim amount
* Claim type
* Fraud flag
The script continuously inserts records into MongoDB to simulate streaming data.

## MongoDB
MongoDB is used as the operational data store. Two collections are created:
* customers
* claims
This layer simulates transactional insurance data storage.

## Snowflake

Data from MongoDB is loaded into Snowflake under a raw schema. Snowflake is used as the cloud data warehouse for analytical querying.

## dbt Transformations
dbt is used to:
* Create a staging model from the raw claims table
* Convert claim date to proper date format
* Cast amount to numeric type
* Cast fraud flag to boolean
* Create a monthly aggregated model grouped by month and claim type

## Power BI Dashboard

Power BI connects directly to Snowflake.The dashboard shows:
* Monthly claim count
* Total claim amount
* Total fraud count
* Claims grouped by type
* Fraud count by month

## Tech Stack

* Python
* Faker
* MongoDB
* Snowflake
* dbt
* Power BI

