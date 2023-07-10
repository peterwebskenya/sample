from peewee import *
from os import path
#creating my first database
connection  = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Students.db"))

#creating table inside db
class Students(Model):
    name = CharField()
    phone no = float(unique=True)
    age = int()
user.create_table(fail_silently=True)

    class Meta:
        database =