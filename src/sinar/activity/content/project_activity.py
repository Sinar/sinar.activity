# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
# from zope import schema
from zope.interface import implementer


from sinar.activity import _


class IProjectActivity(model.Schema):
    """ Marker interface and Dexterity Python Schema for ProjectActivity
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:
    # model.load('project_activity.xml')

    text = RichText(
        title=_('Project Details'),
        required=False
    )

@implementer(IProjectActivity)
class ProjectActivity(Container):
    """ Content-type class for IProjectActivity
    """
