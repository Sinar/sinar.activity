# -*- coding: utf-8 -*-

# from sinar.activity import _
from plone.dexterity.browser.view import DefaultView
from zope.interface import implementer
from zope.interface import Interface
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IProjectActivityView(Interface):
    """ Marker Interface for IProjectActivityView"""


@implementer(IProjectActivityView)
class ProjectActivityView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('project_activity_view.pt')

    def activity_status_title(self):

        factory = getUtility(IVocabularyFactory,
                             'sinar.activity.ActivityStatus')

        vocabulary = factory(self)
        if self.context.activity_status:
            term = vocabulary.getTerm(self.context.activity_status)
            return term.title
        else:
            return None

    def activity_types_titles(self):

        factory = getUtility(IVocabularyFactory,
                             'sinar.activity.ActivityTypes')

        vocabulary = factory(self)

        if self.context.activity_types:
            types = []
            for title in self.context.activity_types:
                types.append(vocabulary.getTerm(title).title)

            return types

    def __call__(self):
        # Implement your own actions:
        return super(ProjectActivityView, self).__call__()
