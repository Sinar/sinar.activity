# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase


class ActivityOutputViewlet(ViewletBase):

    def activities(self):
        relations = api.relation.get(source=self.context,
                                     relationship="output_of")
        return [relation.to_object for relation in relations]

    def index(self):
        return super(ActivityOutputViewlet, self).render()
