import pytest
from asyncpgsa import pg

from db.tables import vehicles

HOST = 'localhost'
PORT = 5432
DB_NAME = 'vehicle_builder'
USER = 'postgres'
PASS = 'password'


async def init():
    await pg.init(
        host=HOST,
        port=PORT,
        database=DB_NAME,
        user=USER,
        # loop=loop,
        password=PASS,
        min_size=5,
        max_size=10
    )


@pytest.mark.skip
async def test_connection():
    await init()
    query = vehicles.select()
    async with pg.query(query) as cursor:
        async for row in cursor:
            print(row)
            assert 'title' in row
