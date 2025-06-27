from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from db import engine
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    all_score = Column(Integer, nullable=True, default=0)

Base.metadata.create_all(engine)

# new_user = User(name="John Doe", email="john@example.com")
# session = Session()
# session.add(new_user)
# session.commit()
# session.close()
