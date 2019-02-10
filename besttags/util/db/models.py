from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    related = relationship("Related")

    def __repr__(self):
        return "<Tag(id={} name='{}')>".format(self.id, self.name)


class Related(Base):
    __tablename__ = 'related'

    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'))
    tag = Column(String)
    ratio = Column(Float, default=1)
