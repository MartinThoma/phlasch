from phlasch.core.tables import link


async def create_link(conn, address):
    insert = link.insert().values(address=address)
    cursor = await conn.execute(insert)
    row = await cursor.fetchone()
    return dict(row)


async def list_links(conn, id):
    select = link.select()
    cursor = await conn.execute(select)
    return cursor


async def retrieve_link(conn, id):
    select = link.select().where(link.c.id == id)
    cursor = await conn.execute(select)
    return cursor


async def update_link_shortcut(conn, pk, shortcut):
    update = link.update().values(
        shortcut=shortcut,
    ).where(link.c.id == pk)
    await conn.execute(update)


async def update_link_visits(conn, pk):
    update = link.update().values(
        visits=link.c.visits + 1,
    ).where(link.c.id == pk)
    await conn.execute(update)
