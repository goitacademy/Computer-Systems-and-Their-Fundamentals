from sqlite3 import Error

from connect import create_connection, database


def select_projects(conn):
    """
    Query all rows in the projects table with its tasks
    :param conn: the Connection object
    :return: rows projects or None
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM projects JOIN tasks ON tasks.project_id = projects.id;"
        )
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


if __name__ == "__main__":
    with create_connection(database) as conn:
        print("Projects:")
        projects = select_projects(conn)
        print(projects)
