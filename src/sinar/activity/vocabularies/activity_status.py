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
class ActivityStatus(object):
    """
    """

    def __call__(self, context):
        # Activity Status based on IATI Codelist
        # https://iatistandard.org/en/iati-standard/203/codelists/activitystatus
        items = [
            VocabItem('1',
                    _('''Pipeline/identification''')),
            VocabItem('2',
                    _('''Implementation''')),
            VocabItem('3',
                    _('''Finalisation''')),
            VocabItem('4',
                    _('''Closed''')),
            VocabItem('5',
                    _('''Cancelled''')),
            VocabItem('6',
                    _('''Suspended''')),
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


ActivityStatusFactory = ActivityStatus()
