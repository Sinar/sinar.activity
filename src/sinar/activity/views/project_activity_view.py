# -*- coding: utf-8 -*-

# from sinar.activity import _
from plone.dexterity.browser.view import DefaultView
from zope.interface import implementer
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IProjectActivityView(Interface):
    """ Marker Interface for IProjectActivityView"""


@implementer(IProjectActivityView)
class ProjectActivityView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('project_activity_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(ProjectActivityView, self).__call__()
