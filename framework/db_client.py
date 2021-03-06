import psycopg2

# psql -U postgres -h localhost -d postgres
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
        """Добавляем тестовую группу"""
        query = "insert into auth_group (id, name) values (%s, %s)"
        values = (values_id, values_name)
        self.cur.execute(query, values)
        self.db.commit()

    def trunc_table_auth_group(self):
        """Транкаем таблицу с тестовой группой"""
        self.cur.execute(f"truncate auth_group cascade")
        self.db.commit()

    def delete_test_user(self, user_name='Testuser'):
        """Функция удаляет тестового пользователя из таблицы"""
        self.cur.execute(f"""delete from auth_user 
        where username = '{user_name}'""")
        self.db.commit()

    def close_connect(self):
        self.db.close()

    def check_add_user_in_group(self, group_id="1", user_name='Testuser'):
        """Функция проверяет созданную группу с группой пользователя"""
        self.cur.execute(f"""select id from auth_user 
        where username = '{user_name}'""")
        user_id = self.cur.fetchone()
        self.cur.execute(f"""select group_id from auth_user inner join
                                auth_user_groups on 
                                (auth_user.id = {user_id[0]})""")
        user_group_id = self.cur.fetchone()
        self.cur.execute(f"select id from auth_group "
                         f"where id = {group_id}")
        auth_group_id = self.cur.fetchone()
        assert user_group_id[0] == auth_group_id[0]
        print('user_add_in_group')

    def delete_users_not_admin_in_auth_user(self):
        """Метод удаляет всех тестовых пользователей в auth_user
           кроме суперпользователя admin"""
        self.cur.execute(f"""delete from auth_user 
        where username != 'admin'""")
        self.db.commit()
