# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles, TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from sinar.activity.content.activity import IActivity  # NOQA E501
from sinar.activity.testing import SINAR_ACTIVITY_INTEGRATION_TESTING  # noqa
from zope.component import createObject, queryUtility

import unittest


class ActivityIntegrationTest(unittest.TestCase):

    layer = SINAR_ACTIVITY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_activity_schema(self):
        fti = queryUtility(IDexterityFTI, name='Activity')
        schema = fti.lookupSchema()
        self.assertEqual(IActivity, schema)

    def test_ct_activity_fti(self):
        fti = queryUtility(IDexterityFTI, name='Activity')
        self.assertTrue(fti)

    def test_ct_activity_factory(self):
        fti = queryUtility(IDexterityFTI, name='Activity')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IActivity.providedBy(obj),
            u'IActivity not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_activity_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Activity',
            id='activity',
        )

        self.assertTrue(
            IActivity.providedBy(obj),
            u'IActivity not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('activity', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('activity', parent.objectIds())

    def test_ct_activity_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Activity')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_activity_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Activity')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'activity_id',
            title='Activity container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
