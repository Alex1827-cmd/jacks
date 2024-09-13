import pyodbc
import pandas as pd  # Assuming pandas is used for DataFrame handling

# Define your DSN
dsn = 'aws_rds_alex'

# Establish connection using DSN
conn = pyodbc.connect(f'DSN={dsn}')

# Insert data to MYSQL table
table_name = 'blake_park_data'
cursor = conn.cursor()

# Create table if it doesn't exist
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    `Season` VARCHAR(200),
    `Lg` VARCHAR(200),
    `Tm` VARCHAR(200),
    `W` VARCHAR(200),
    `L` VARCHAR(200),
    `Finish` VARCHAR(200),
    `Blank_Column_2` VARCHAR(200),
    `Age` VARCHAR(200),
    `Ht` VARCHAR(200),
    `Wt` VARCHAR(200),
    `Blank_Column_3` VARCHAR(200),
    `G` VARCHAR(200),
    `MP` VARCHAR(200),
    `FG` VARCHAR(200),
    `FGA` VARCHAR(200),
    `FG%` VARCHAR(200),
    `3P` VARCHAR(200),
    `3PA` VARCHAR(200),
    `3P%` VARCHAR(200),
    `2P` VARCHAR(200),
    `2PA` VARCHAR(200),
    `2P%` VARCHAR(200),
    `FT` VARCHAR(200),
    `FTA` VARCHAR(200),
    `FT%` VARCHAR(200),
    `ORB` VARCHAR(200),
    `DRB` VARCHAR(200),
    `TRB` VARCHAR(200),
    `AST` VARCHAR(200),
    `STL` VARCHAR(200),
    `BLK` VARCHAR(200),
    `TOV` VARCHAR(200),
    `PF` VARCHAR(200),
    `PTS` VARCHAR(200)
);
"""

cursor.execute(create_table_query)
conn.commit()

# Insert data into the table
for index, row in games.iterrows():

    insert_query = f"""
    INSERT INTO {table_name} (
         `Season`, `Lg`, `Tm`, `W`, `L`, `Finish`, `Blank_Column_2`, `Age`, `Ht`, `Wt`, `Blank_Column_3`,
        `G`, `MP`, `FG`, `FGA`, `FG%`, `3P`, `3PA`, `3P%`, `2P`, `2PA`, `2P%`, `FT`, `FTA`, `FT%`,
        `ORB`, `DRB`, `TRB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `PTS`
    ) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?,?,?
    );
    """
    values = tuple(row)
    cursor.execute(insert_query, values)

conn.commit()

# Close the connection
cursor.close()
conn.close()