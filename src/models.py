import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    id_admin = Column(Integer, ForeignKey('admin.id'))
    admin = relationship('Admin', backref=backref('users', uselist=True))
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    numero_de_documento = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)
    age = Column(String(250), nullable=False)
    
    

class Admin(Base):
    __tablename__ = 'admin'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('admin', uselist=True))
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(10), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(Integer, nullable=False)

class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True ,nullable=False)
    id_admin = Column(Integer, ForeignKey('admin.id'))
    admin = relationship('Admin', backref=backref('teacher', uselist=True))
    name = Column(String(250) ,nullable=False)
    last_name = Column(String(250) ,nullable=False)
    email = Column(String(250) ,nullable=False)
    password = Column(String(250) ,nullable=False)
    username = Column(String(250) ,nullable=False)
    phone = Column(Integer ,nullable=False)
    age = Column(Integer ,nullable=False)

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(250), nullable=False)
    id_User = Column(Integer, ForeignKey('user.id_User'), nullable=False)
    user = relationship('User', backref=backref('course', uselist=True))
    id_teacher = Column(Integer, ForeignKey('user.id_teacher'), nullable=False)
    teacher = relationship('Teacher', backref=backref('course'), uselist=True)
    category = Column(String(250), nullable=False)
    modules_lenght = Column(Integer, nullable=False)
    certificado = Column(String(250), nullable=False)

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, nullable=False)
    id_course = Column(Integer, ForeignKey('course.id_course'), nullable=False)
    course = relationship('Course', backref=backref('category'), uselist=True)
    id_teacher = Column(Integer, ForeignKey('teacher.id_teacher'), nullable=False)
    teacher = relationship('Teacher', backref=backref('category'), uselist=True)
    title_category = Column(String(250), nullable=False)
    title_course = Column(String(250), nullable=False)

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_payment = Column(Integer, ForeignKey('payment.id_payment)'), nullable=False)
    title_order = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)

class Payment(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_admin = Column(Integer, ForeignKey('admin.id_admin'), nullable=False)
    id_orden = Column(Integer, ForeignKey('orders.id_orden'), nullable=False)


class Modules(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True, nullable=False)
    id_course = Column(Integer, ForeignKey('course.id_course'), nullable=False)
    type_file = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)
    id_video = Column(Integer, nullable=False)
    type_video = Column(String(250), nullable=False)
    id_text = Column(Integer, nullable=False)
    type_text = Column(String(250), nullable=False)
    id_image = Column(Integer, nullable=False)
    type_image = Column(String(250), nullable=False)

class Request(Base):
    __tablename__ = 'request'

    id = Column(Integer, primary_key=True, nullable=True)
    id_course = Column(Integer, ForeignKey('course.id_course'), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)


    



""" class Teacher(Base):
    __tablename__ = 'Teacher'
    favorite_id  = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(String(250), nullable=True)
    vehicles_id = Column(String(250), nullable=True)
    planets_id = Column(String(250), nullable=True) """


""" class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, nullable=False)
    character_id = Column(Integer, ForeignKey('favorite.character_id'), nullable=False)
    name = Column(String(250), nullable=False)
    description= Column(String(250), nullable=True)
    height= Column(Integer, nullable=True)
    age= Column(Integer, nullable=True)
    weight= Column(Integer, nullable=True)
 """


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
