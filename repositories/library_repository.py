from models.library import Library
from db.run_sql import run_sql


def save(library):
    sql = """
        INSERT INTO libraries (name)
        VALUES (%s)
        RETURNING id
    """
    values = [library.name]
    results = run_sql(sql, values)

    id = results[0]["id"]
    library.id = id


def select(id):
    sql = """
        SELECT * FROM libraries
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)[0]

    name = result["name"]
    id = result["id"]
    library = Library(name, id)

    return library


def select_all():
    libraries = []
    sql = "SELECT * FROM libraries"
    results = run_sql(sql)

    for result in results:
        name = result["name"]
        id = result["id"]
        library = Library(name, id)
        libraries.append(library)

    return libraries


def update(library):
    sql = """
        UPDATE libraries
        SET name = %s
        WHERE id = %s
    """
    values = [library.name, library.id]
    run_sql(sql, values)


def delete(library):
    sql = """
        DELETE FROM libraries
        WHERE id = %s
    """
    values = [library.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM libraries"
    run_sql(sql)
