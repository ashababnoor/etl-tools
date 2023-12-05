import os
import configparser


# Create a new configparser object
config = configparser.ConfigParser()

# Define the path to your project
project_path = os.path.dirname(os.path.abspath(__file__))

# Define the path to the config file
config_file_path = os.path.join(project_path, 'config.ini')

# Read the config file
config.read(config_file_path)

# Access the configuration values
database_host = config.get('database', 'host')
database_port = config.get('database', 'port')
database_username = config.get('database', 'username')
database_password = config.get('database', 'password')

# Use the configuration values in your code
# ...

# Update the configuration values
config.set('database', 'password', 'new_password')

# Save the updated configuration to file
with open('/Users/shabab/Documents/Projects/Personal/etl-tools/etl-tools/mysql-postgres-etl/src/config.ini', 'w') as config_file:
    config.write(config_file)
