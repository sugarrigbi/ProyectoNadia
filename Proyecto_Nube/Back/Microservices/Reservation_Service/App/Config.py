import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:password@localhost:3306/biblioteca"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False