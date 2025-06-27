# db.py
from sqlalchemy import create_engine

# SQLite
engine = create_engine("sqlite:///users.db", echo=False)

# Agar PostgreSQL ishlatsangiz (masalan):
# engine = create_engine("postgresql+psycopg2://user:password@localhost/dbname")

# Agar MySQL ishlatsangiz:
# engine = create_engine("mysql+pymysql://user:password@localhost/dbname")
