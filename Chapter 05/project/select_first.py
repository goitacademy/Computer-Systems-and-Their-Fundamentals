import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("salary.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(p.total), 2), e.post
FROM payments as p
LEFT JOIN employees as e ON p.employee_id = e.id
GROUP BY e.post;
"""

print(execute_query(sql))
