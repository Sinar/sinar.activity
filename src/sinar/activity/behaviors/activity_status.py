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


class IActivityStatusMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IActivityStatus(model.Schema):
    """
    """

    directives.widget(activity_status=SelectFieldWidget)
    activity_status = schema.Choice(
        title=_('Activity Status'),
        description=_('Current activity implementation status'),
        vocabulary="sinar.activity.ActivityStatus",
        required=False,
    )


@implementer(IActivityStatus)
@adapter(IActivityStatusMarker)
class ActivityStatus(object):
    def __init__(self, context):
        self.context = context

    @property
    def activity_status(self):
        if safe_hasattr(self.context, 'activity_status'):
            return self.context.activity_status
        return None

    @activity_status.setter
    def activity_status(self, value):
        self.context.activity_status = value
