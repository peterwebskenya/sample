#from peewee import *
from peewee import *
from os import path
#creating my first database
connection  = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "peter.db"))

#creating table jnside db
class user(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
user.create_table(fail_silently=True)

     class Meta:
        database = db