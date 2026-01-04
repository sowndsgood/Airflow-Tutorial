1. Airflow Config File
- Has DAG path
- Has plugins folder
- Has executor type
- Has database connection info

2. DAG
- Import DAG class, Airflow Operators, Functions - Built-in or User Defined in Plugin Folder
- Create DAG object with start date, end date, schedule interval, and default arguments
- Define tasks using Airflow Operators
- Set task dependencies: Bitshift, SetUpstream and SetDownstream, Chain Function, TaskflowAPI

UI execute and see logs

Operator - Class, Tasks - Instances of Operators (Objects)

Operator Categories:
- Action Operators: Bash, Python, ADF (Azure Data Factory), Github
- Transfer Operators: S3ToRedshiftOperator, GoogleCloudStorageToBigQueryOperator
- Sensor Operators: FileSensor, TimeDeltaSensor, S3KeySensor

Only some operators are installed with Airflow by default, while others may require additional installation steps.
Do it via Docker file or requirements.txt

Variables:
- Key-Value Pairs
- Types: Regular , JSON
- Airflow UI -> Admin -> Variables
- Can be used for multiple DAGs
- var.value.get function to get variable values
- Can be encrypted if required

Connections:
- Username, Password, Host, Port, Connection Type, Connection ID (Unique)
- Airflow UI -> Admin -> Connections
- If connection not found, install using package provider
