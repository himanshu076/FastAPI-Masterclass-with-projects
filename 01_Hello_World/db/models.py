# from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy import Integer, String, Boolean, ForeignKey, Column
from sqlalchemy.orm import relationship

from db.database import Base

class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = relationship('DbUser', back_populates='articles')

class DbArticle(Base):
  __tablename__ = 'articles'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  Content = Column(String)
  published = Column(Boolean)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship('DbUser', back_populates='items')