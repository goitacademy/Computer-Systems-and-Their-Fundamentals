import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("salary.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT COUNT(*), c.company_name
FROM employees e
LEFT JOIN companies c ON e.company_id = c.id
GROUP BY c.id;
"""

print(execute_query(sql))
