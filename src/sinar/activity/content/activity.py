# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
# from zope import schema
from zope.interface import implementer
from zope.component import adapter
from Products.ZCatalog.interfaces import IZCatalog
from DateTime import DateTime
from plone.indexer import indexer


# from sinar.activity import _


class IActivity(model.Schema):
    """ Marker interface and Dexterity Python Schema for Activity
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('activity.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@indexer(IActivity)
def startIndexer(obj):
    if obj.start is None:
        return None
    return DateTime(obj.start.isoformat())


@indexer(IActivity)
def endIndexer(obj):
    if obj.end is None:
        return None
    return DateTime(obj.end.isoformat())


@implementer(IActivity)
class Activity(Container):
    """
    """
