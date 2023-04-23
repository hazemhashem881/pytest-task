from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pandas as pd

drivername="4-db-1"
pg_user="odoo"
pg_pass="odoo"
database="newest"
pg_host="localhost"
pg_port=5432
pg_db="newest"

try:
    engine = create_engine(f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")
    con = engine.connect()
    print("Database connection successful")
except Exception as e:
    print("Database connection failed:", e)
    
Session = sessionmaker(bind=engine)
Session = Session()

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(255), nullable=False)
    joined = Column(DateTime(), default=datetime.now)

    articles = relationship('Article', backref='author')


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer(), primary_key=True)
    slug = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    content = Column(Text)
    author_id = Column(Integer(), ForeignKey('authors.id'))

Base.metadata.create_all(engine)
hazem = Author(
    firstname="hazem",
    lastname="hashem",
    email="hazem_email@gmail.com"
)

ali = Author(
    firstname="ali",
    lastname="khaled",
    email="ali_email@gmail.com"
)

ezz = Author(
    firstname="Ezzeddin",
    lastname="Abdullah",
    email="ezz_email@gmail.com"
)

ahmed = Author(
    firstname="Ahmed",
    lastname="Mohammed",
    email="ahmed_email@gmail.com"
)

Session.add(hazem)
Session.commit()

Session.add(ali)
Session.commit()

Session.add(ezz)
Session.commit()
Session.add(ahmed)
Session.commit()

article1 = Article(
    slug="clean-python",
    title="How to Write Clean Python",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    author=ezz
    )
Session.add(article1)
Session.commit()

article2 = Article(
    slug="postgresql-system-catalogs-metadata",
    title="How to Get Metadata from PostgreSQL System Catalogs",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    created_on = datetime(2022, 8, 29),
    author=ezz
    )

article3 = Article(
    slug="sqlalchemy-postgres",
    title="Interacting with Databases using SQLAlchemy with PostgreSQL",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    author=ahmed
    )

article4 = Article(
    slug="DevOps-postgrs",
    title="using tool is called docker to Interacting with Databases using SQLAlchemy with PostgreSQL",
    content="Create docker and docker-compose then create docker-compose pull image latest form postgres and pgadmin then create venv to run pythem",
    author=hazem
    )

Session.add(article2)
Session.commit()

Session.add(article3)
Session.commit()

Session.add(article4)
Session.commit()

#session.add_all([article1, article2, article3])




