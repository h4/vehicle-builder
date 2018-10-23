from dataclasses import dataclass


@dataclass
class Settings:
    db_dsn: str = 'postgresql://postgres:password@localhost/vehicle-builder'
    db_host: str = 'localhost'
    db_port: int = 5432
    db_name: str = 'vehicle-builder'
    db_user: str = 'postgres'
    db_pass: str = 'password'
