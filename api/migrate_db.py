import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

from api.db import Base

load_dotenv()

DB_URL = "%s://%s:%s@%s/%s" % (
    os.environ["DB_DRIVER"],
    os.environ["DB_USER"],
    os.environ["DB_PASSWORD"],
    os.environ["DB_HOST"],
    os.environ["DB_NAME"],
)
db_engine = create_engine(DB_URL, echo=True)


def reset_databse():
    Base.metadata.drop_all(bind=db_engine)
    Base.metadata.create_all(bind=db_engine)


if __name__ == "__main__":
    reset_databse()
