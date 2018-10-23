import os
from dataclasses import dataclass


@dataclass
class Settings:
    db_host: str = os.environ.get('DB_HOST', 'localhost')
    db_port: int = os.environ.get('DB_PORT', '5432')
    db_name: str = os.environ.get('DB_NAME', 'vehicle-builder')
    db_user: str = os.environ.get('DB_USER', 'postgres')
    db_pass: str = os.environ.get('DB_PASS', 'password')

    @property
    def db_dsn(self):
        return f'postgresql://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}'
