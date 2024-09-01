from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    id = fields.IntField(pk=True)  # Инкрементируемый первичный ключ
    tg_user_id = fields.CharField(max_length=15, unique=True)  # Уникальный идентификатор пользователя Telegram
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    username = fields.CharField(max_length=50, null=True)  # Опциональное поле, если username может отсутствовать
    birthday = fields.DateField(null=True)

    class Meta:
        table = "users"  # Название таблицы в базе данных

    def __str__(self):
        return f"{self.id} {self.tg_user_id} {self.first_name} {self.last_name} {self.username} {self.birthday}"


UserSchema = pydantic_model_creator(User)
UserCreateSchema = pydantic_model_creator(User, name="UserCreate", exclude_readonly=True)
