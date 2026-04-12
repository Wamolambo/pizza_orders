
# Project Setup

This document describe the setup and commands used to run the project on a local machine.


# Prerequisites

The following requirements are needed to run this project:

1. Ensure that python 3.10 is installed in your machine. You can check your python version using:
```
python --version 
```

If python is not installed, run the following:

```
sudo apt update
sudo apt install python
```

2. Ensure Postgres is installed and configured to run database operations. The default database and schema will be used in this project.
   Note: The database credentials and schema are in the config.yaml file in the root path



# Setup Instructions
1. Clone the repository
```
cd /root
git clone https://github.com/Wamolambo/pizza_orders.git
cd pizza_orders
```

2. Create a virtual environment:
```
python -m venv etl_env
source etl_env/bin/activate 
```

3. Install dependencies
```
pip install -r requirements.txt
```
