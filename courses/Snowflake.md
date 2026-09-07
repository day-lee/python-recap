# Snowflake

- Data warehousing platform
- storing large amounts for historical data

### Benefit
- Self-Managed service 
- support connection with cloud providers 
- Least-privilege access (Governance control)

### Snowsight UI 
Market place: external data 

### Architecture
Cloud services: manager, optimizer, metadata manager, security 
Query processing: MPP(massive parallel processing) - distributes data and compute resources across a cluster of nodes
Database storage: compress and store columnar, optimised for analytical queries, aggregating and filtering on columns 

### Monitoring
- debug failures, query speed, copied 
- query details
- copy history: external sources, status 

### Load Data
- marketplace: external data
- load internal data 
- cloud provider: external stage points to clouds

### Role
- privilege management  

### Multiple warehouse
- large warehouse size needs 8 computers(nodes)
- DE: large warehouse to process raw data 
- DA: small warehouse for quick analysis 

Snowflake notebook 
- interactive env combine sql, python, markdown cells 
- 120 day free trial including $400 free usage. 
https://signup.snowflake.com/?trial=student&cloud=aws&region=us-west-2&utm_source=datacamp&utm_campaign=introtosnowflake 