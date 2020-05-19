from app import db
from datetime import datetime
from sqlalchemy import ForeignKey
from pytz import utc

user_identifier = db.Table('user_identifier',
    db.Column('user_index', db.Integer, db.ForeignKey('users.index')),
    db.Column('match_index', db.Integer, db.ForeignKey('matches.index'))
)


class User(db.Model):
    __tablename__ = 'users'

    index = db.Column(db.Integer, primary_key=True)
    slack_id = db.Column(db.String(80), unique=True)
    intra_id = db.Column(db.String(80), unique=True)
    register = db.Column(db.Boolean)
    joined = db.Column(db.Boolean)
    match_count = db.Column(db.Integer, default=0)

    def __init__(self, slack_id, intra_id):
        self.slack_id = slack_id
        self.intra_id = intra_id
        self.register = True
        self.joined = False

    def __repr__(self):
        return '<index: {}, slack_id: {}, intra_id: {}, register: {}, joined: {}>'.format(self.index, self.slack_id, self.intra_id, self.register, self.joined)

    def serialize(self):
        return {
            'index': self.index,
            'slack_id': self.slack_id,
            'intra_id': self.intra_id,
            'register': self.register,
            'joined': self.joined
        }


class Match(db.Model):
    __tablename__ = 'matches'

    index = db.Column(db.Integer, primary_key=True)
    match_day = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    users = db.relationship(User, secondary=user_identifier, backref='matches')
    activity_index = db.Column(db.Integer, db.ForeignKey('activities.index'))
    activity = db.relationship("Activity")

    def __init__(self, user1, user2, activity):
        self.users.append(user1)
        self.users.append(user2)
        self.activity = activity

    def __repr__(self):
        return '<index: {}, match_day: {}, user1_intra_id: {}, user2_intra_id: {}, activity: {}>'\
            .format(self.index, self.match_day, self.users[0].intra_id, self.users[1].intra_id, self.activity)

    def serialize(self):
        return {
            'match_day': self.match_day,
            'user1_intra_id': self.users[0].intra_id,
            'user2_intra_id': self.uesrs[1].intra_id
        }


class Evaluation(db.Model):
    __tablename__ = 'evaluations'

    index = db.Column(db.Integer, primary_key=True)
    send_time = db.Column(db.DateTime, nullable=True)
    react_time = db.Column(db.DateTime, nullable=True)
    match_index = db.Column(db.Integer, ForeignKey('matches.index'))
    match = db.relationship(Match, foreign_keys=[match_index], backref='evaluations')
    user_index = db.Column(db.Integer, ForeignKey('users.index'))
    user = db.relationship(User, foreign_keys=[user_index], backref='active_evaluations')
    mate_index = db.Column(db.Integer, ForeignKey('users.index'))
    mate = db.relationship(User, foreign_keys=[mate_index], backref='passive_evaluations')
    satisfaction = db.Column(db.Integer, nullable=True)

    def __init__(self, match, user, mate):
        self.react_time = None
        self.match = match
        self.user = user
        self.mate = mate
        self.satisfaction = None

    def __repr__(self):
        return '<react_time: {}, match: {}, user: {}, mate: {}>'.format(self.react_time, self.match.match_day, self.user.intra_id, self.mate.intra_id)

    def serialize(self):
        return {
            'react_time': self.react_time,
            'match': self.match.match_day,
            'user': self.user.intra_id,
            'mate': self.mate.intra_id,
        }


class Activity(db.Model):
    __tablename__ = 'activities'
    index = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)
    content = db.Column(db.String)
    url = db.Column(db.String, nullable=True)

    def __init__(self, subject, content, url=None):
        self.subject = subject
        self.content = content
        self.url = url

    def __repr__(self):
        return '<index: {}, subject: {}, content: {}, url: {}>'.format(self.index, self.subject, self.content, self.url)

    def serialize(self):
        return {
            'subject': self.subject,
            'content': self.content,
            'url': self.url
        }