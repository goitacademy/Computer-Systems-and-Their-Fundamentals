from sqlite3 import Error

from connect import create_connection, database


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """
    INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?);
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, project)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = """
    INSERT INTO tasks(name,priority,status,project_id,begin_date,end_date) VALUES(?,?,?,?,?,?);
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


if __name__ == "__main__":
    with create_connection(database) as conn:
        # create a new project
        project = ("Cool App with SQLite & Python", "2022-01-01", "2022-01-30")
        project_id = create_project(conn, project)
        print(project_id)

        # tasks
        task_1 = (
            "Analyze the requirements of the app",
            1,
            True,
            project_id,
            "2022-01-01",
            "2022-01-02",
        )
        task_2 = (
            "Confirm with user about the top requirements",
            1,
            False,
            project_id,
            "2022-01-03",
            "2022-01-05",
        )

        # create tasks
        print(create_task(conn, task_1))
        print(create_task(conn, task_2))
