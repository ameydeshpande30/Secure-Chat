from peewee import *

db = SqliteDatabase('data.db')

class BaseModel(Model):
    class Meta:
        database = db

class PublicKey(BaseModel):
    uid = CharField(max_length=150, primary_key=True)
    key = CharField(max_length=51200)



db.connect()
db.create_tables([PublicKey])


def insertPublicKey(uid,key):
    try :
        PublicKey.create(uid=uid, key=key)
        db.commit()
        return 1
    except:
        return -1

def retrieve(uid):
    try:
        out = PublicKey.select().where(PublicKey.uid == uid).get()
    except: 
        return -1
    return out.key


