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

Sensors:
- Special type of operator that waits for a certain condition to be met at regular intervals
- Ex: S3KeySensor, Datetime, HTTP, ExternalTaskSensor, Bigquery
- Parameters:
 1. Poke Interval - Time to wait between each try
 2. Mode - Poke or Reschedule
 3. Timeout - Maximum time to wait for the condition to be met by Airflow
 4. softfail - If True, the task will not fail if the condition is not met

Deferrable Operators:
- Allow tasks to be paused and resumed later
- Efficient resource usage
- Triggerer: A separate process that wakes up and checks if the task can be run
- Cluster activity - Check Trigger running or not
- Can make sensor tasks as deferable with parameters
- Check for Deferrable / Async/ Trigger keyword in operators

Xcom:
- To exchange data as airflow tasks are isolated
- Xcom push and pull
- Xcoms are stored in the metadata database
- Smaller data only, for larger use customer database
- UI: Admin -> Xcoms

Hooks:
- Prebuild Python class
- Low Level Code -> Hooks -> Operators
- Use operators first, If not available, use Hooks, If not hooks, write custom code

Datasets:
- Data-aware Scheduling - Schedule tasks based on the availability of data
- Use dataset class
- Dataset: A logical representation of a collection of data
- Can be used to define dependencies between tasks
- UI: Admin -> Datasets
- Outlets parameter means the dataset that a task produces
- Inlets parameter means the dataset that a task requires
