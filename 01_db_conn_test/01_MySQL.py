import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/crawl_data')

query = "SELECT * FROM test"
df = pd.read_sql(query, engine)
print(df)
