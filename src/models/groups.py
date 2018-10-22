from models.base import BaseModel, db


class Group(BaseModel):
    __tablename__ = 'groups'

    title = db.Column(db.String)
    parent_group_id = db.Column(None, db.ForeignKey('groups.id'))
    is_set = db.Column(db.Boolean, default=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._subgroups = set()
        self._features = set()

    @property
    def subgroups(self):
        return self._subgroups

    @subgroups.setter
    def add_subgroup(self, group):
        self._subgroups.add(group)

    @property
    def features(self):
        return self._features

    @features.setter
    def add_feature(self, features):
        self._features.add(features)


class Feature(BaseModel):
    __tablename__ = 'features'

    title = db.Column(db.String)
    group_id = db.Column(None, db.ForeignKey('groups.id'), nullable=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._functions = set()

    @property
    def functions(self):
        return self._functions

    @functions.setter
    def add_function(self, group):
        self._functions.add(group)


class Function(BaseModel):
    __tablename__ = 'functions'

    title = db.Column(db.String)
    feature_id = db.Column(None, db.ForeignKey('features.id'), nullable=False)
