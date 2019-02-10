import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from besttags.util.db.models import Base, Tag, Related
from besttags.defaults import SAMPLE_DB


class Manager(object):

    def __init__(self, filename=SAMPLE_DB):
        super(Manager, self).__init__()
        self.filename = filename
        self.engine = create_engine('sqlite:///{}'.format(filename))
        self.Session = sessionmaker(bind=self.engine)

    def _add_related(self, tag_id, tag, ratio=0):
        session = self.Session()
        related = session.query(Related).filter(
            Related.tag_id == tag_id, Related.tag == tag).first()

        if not related:
            session.add(Related(tag_id=tag_id, tag=tag, ratio=ratio))
            session.commit()

    def setup(self):
        """
        create a database
        """
        Base.metadata.create_all(self.engine)

    def delete(self):
        """
        delete the db file
        """
        os.remove(self.filename)

    def add(self, name, related):
        """
        add a tag with the related tags
        """
        session = self.Session()

        tag = session.query(Tag).filter(Tag.name == name).first()
        if not tag:
            tag = Tag(name=name)
            session.add(tag)
            session.commit()

        if isinstance(related, list):
            for r in related:
                self._add_related(tag.id, r)

        elif isinstance(related, dict):
            for r, ratio in related.items():
                self._add_related(tag_id=tag.id, tag=r, ratio=ratio)

        elif isinstance(related, str):
            self._add_related(tag_id=tag.id, tag=related)

    def get(self, tag):
        """
        get the related tags
        """
        session = self.Session()
        result = session.query(Tag).filter(Tag.name == tag).first()
        return {t.tag: t.ratio for t in result.related}

    def all(self):
        """
        return all tags
        """
        session = self.Session()
        result = {}
        for instance in session.query(Tag).order_by(Tag.id):
            result[instance.name] = {r.tag: r.ratio for r in instance.related}
        return result
