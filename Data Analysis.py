import pandas as pd
import sqlite3

USERS = list()


class Users:
    def __init__(self):
        self.users = list()

    def add_user(self, user):
        # функция добавляет нового пользователя
        self.users.append(user)

    def delete_user(self, user_id):
        # функция находит и удаляет пользователя по индексу
        self.users.pop(self.users.index(self.find_user(user_id)))

    def find_user(self, user_id):
        # функция ищет пользоватя среди зарегестрированных (В данном случае в массиве USERS)

        for user in self.users:
            if user.get_user_id() == user_id:
                return user
        return None

    def update_score(self, user_id: int, test_id: int, question_id: int, answer, score=1):
        # Функция принимает в себя несколько значений:
        # user_id - id пользователя
        # test_id - id теста
        # question_id - id вопроса
        # answer - ответ пользователя на вопрос
        # score - количество очков, которые будут добавлены
        # Если всё введено корректо то у пользователя изменится количество очков, если ответ верен

        db = sqlite3.connect('app/database/tests.db')
        df = pd.read_sql_query(f'SELECT * FROM quest WHERE test_id = {test_id} AND id = {question_id}', db)
        if answer == int(df['correct_answer'][0]):
            user = self.find_user(self, user_id)

            if not (user is None):
                user.update_personal_score(1)
            else:
                return None
        db.close()

    def write_user_result_to_data_base(self, user_id):
        pass


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.personal_score = 0

    def get_user_id(self):
        return self.user_id

    def get_user_personal_score(self):
        return self.personal_score

    def update_personal_score(self, point: int):
        self.personal_score += point
