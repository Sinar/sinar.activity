# -*- coding: utf-8 -*-

# from plone import api
from sinar.activity import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class ActivityTypes(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem('advocacy', _('Advocacy')),
            VocabItem('capacity_building',
                    _('Capacity building and awareness raising ')),
            VocabItem('comms', _('Communications and campaigns')),
            VocabItem('crisis_suppport',
                    _('Crisis support and legal defense')),
            VocabItem('monitoring', _('Monitoring and documentation')),
            VocabItem('research', _('Research and knowledge generation')),
            VocabItem('mobilisation', _('Resource mobilisation')),
            VocabItem('solidarity', _('Solidarity Actions')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


ActivityTypesFactory = ActivityTypes()
