import psycopg2
"""                   List of relations
 Schema |            Name            | Type  |  Owner   
--------+----------------------------+-------+----------
 public | app_post                   | table | postgres
 public | auth_group                 | table | postgres
 public | auth_group_permissions     | table | postgres
 public | auth_permission            | table | postgres
 public | auth_user                  | table | postgres
 public | auth_user_groups           | table | postgres
 public | auth_user_user_permissions | table | postgres
 public | django_admin_log           | table | postgres
 public | django_content_type        | table | postgres
 public | django_migrations          | table | postgres
 public | django_session             | table | postgres
"""


class ClientDB:

    def __init__(self):
        self.dbname = 'postgres'
        self.user = 'postgres'
        self.password = 'postgres'
        self.host = 'localhost'
        self.db = psycopg2.connect(
                        dbname=self.dbname,
                        user=self.user,
                        password=self.password,
                        host=self.host)
        self.cur = self.db.cursor()

    def insert_auth_group(self, values_id="1", values_name="Test"):
        query = "insert into auth_group (id, name) values (%s, %s)"
        values = (values_id, values_name)
        self.cur.execute(query, values)
        self.db.commit()

    def trunc_table_auth_group(self):
        self.cur.execute(f"truncate auth_group cascade")
        self.db.commit()

    def table_view(self):
        self.cur.execute(f"select*from auth_user")
        print(self.cur.fetchall())

    def close_connect(self):
        self.db.close()

# db = ClientDB()
# db.trunc_table_auth_group()
