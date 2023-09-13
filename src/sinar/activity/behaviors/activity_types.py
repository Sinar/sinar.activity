# -*- coding: utf-8 -*-

from sinar.activity import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IActivityTypesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IActivityTypes(model.Schema):
    """
    """

    directives.widget(activity_types=SelectFieldWidget)
    activity_types = schema.List(
        title=_('Activity Type'),
        description=_('''Project activity types that best describes this
                      activity'''),
        required=False,
        value_type=schema.Choice(
            vocabulary="sinar.activity.ActivityTypes"
        ),
    )


@implementer(IActivityTypes)
@adapter(IActivityTypesMarker)
class ActivityTypes(object):
    def __init__(self, context):
        self.context = context

    @property
    def activity_types(self):
        if safe_hasattr(self.context, 'activity_types'):
            return self.context.activity_types
        return None

    @activity_types.setter
    def activity_types(self, value):
        self.context.activity_types = value
