# -*- coding: utf-8 -*-

from plone import api
from collective.relationhelpers import api
from plone.app.layout.viewlets import ViewletBase


class ActivityOutputViewlet(ViewletBase):

    def activities(self):

        return api.relations(self.context,
                             attribute="output_of")

    def index(self):
        return super(ActivityOutputViewlet, self).render()
