from phlasch.core.tables import link


async def create_link(engine, address):
    async with engine.acquire() as conn:
        insert = link.insert().values(address=address)
        cursor = await conn.execute(insert)
        return cursor


async def list_links(engine, id):
    async with engine.acquire() as conn:
        select = link.select()
        cursor = await conn.execute(select)
        return cursor


async def retrieve_link(engine, id):
    async with engine.acquire() as conn:
        select = link.select().where(link.c.id == id)
        cursor = await conn.execute(select)
        return cursor


async def update_link_shortcut(engine, id, shortcut):
    async with engine.acquire() as conn:
        update = link.update().values(
            shortcut=shortcut,
        ).where(link.c.id == id)
        cursor = await conn.execute(update)
        return cursor


async def update_link_visits(engine, id):
    async with engine.acquire() as conn:
        update = link.update().values(
            visits=link.c.visits + 1,
        ).where(link.c.id == id)
        cursor = await conn.execute(update)
        return cursor
