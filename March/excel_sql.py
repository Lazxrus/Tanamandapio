import pandas as pd
from sqlalchemy import create_engine

# Archivo excel
excel = pd.read_excel("data.xlsx")

# Conexion a SQL
conexion = create_engine("mysql+pymysql://user:password@host/database")

# Exportacion a SQL
excel.to_sql("nombre de tabla", con=engine, if_exists="replace", index=False)
