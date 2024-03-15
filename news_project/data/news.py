import datetime
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'news'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=True)
    content = sa.Column(sa.String, nullable=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    is_private = sa.Column(sa.Boolean, default=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    user = orm.relationship("User")
    categories = orm.relationship("Category",
                                  secondary="association",
                                  backref="news")

