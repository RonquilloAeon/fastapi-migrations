import json
from typing import Generator, TextIO


def get_quotes(f: TextIO) -> Generator[dict, None, None]:
    data = json.load(f)

    for quote in data:
        yield {
            "author": quote["Author"],
            "category": quote["Category"],
            "content": quote["Quote"],
        }


sources = {}
categories = {}


async def get_or_create_source_id(conn, author: str) -> int:
    source_id = sources.get(author)

    if not source_id:
        await conn.execute("INSERT INTO source (author) VALUES ($1)", author)
        entry = await conn.fetchrow(
            "SELECT id from source WHERE author = $1", author
        )
        source_id = entry["id"]
        sources[author] = source_id

    return source_id


async def get_or_create_category_id(conn, name: str) -> int:
    category_id = categories.get(name)

    if not category_id:
        await conn.execute("INSERT INTO category (name) VALUES ($1)", name)
        entry = await conn.fetchrow(
            "SELECT id from category WHERE name = $1", name
        )
        category_id = entry["id"]
        categories[name] = category_id

    return category_id


async def migrate(conn) -> bool:
    with open("migrations/data/quotes.json", "r") as f:
        for quote in get_quotes(f):
            source_id = await get_or_create_source_id(conn, quote["author"])
            category_id = await get_or_create_category_id(conn, quote["category"])

            await conn.execute(
                "INSERT INTO quote (category, source, content) VALUES ($1, $2, $3)",
                category_id,
                source_id,
                quote["content"]
            )

    return True
