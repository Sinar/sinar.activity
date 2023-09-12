# -*- coding: utf-8 -*-
from sinar.activity.content.project_activity import IProjectActivity  # NOQA E501
from sinar.activity.testing import SINAR_ACTIVITY_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ProjectActivityIntegrationTest(unittest.TestCase):

    layer = SINAR_ACTIVITY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_project_activity_schema(self):
        fti = queryUtility(IDexterityFTI, name='ProjectActivity')
        schema = fti.lookupSchema()
        self.assertEqual(IProjectActivity, schema)

    def test_ct_project_activity_fti(self):
        fti = queryUtility(IDexterityFTI, name='ProjectActivity')
        self.assertTrue(fti)

    def test_ct_project_activity_factory(self):
        fti = queryUtility(IDexterityFTI, name='ProjectActivity')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IProjectActivity.providedBy(obj),
            u'IProjectActivity not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_project_activity_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='ProjectActivity',
            id='project_activity',
        )

        self.assertTrue(
            IProjectActivity.providedBy(obj),
            u'IProjectActivity not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('project_activity', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('project_activity', parent.objectIds())

    def test_ct_project_activity_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='ProjectActivity')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_project_activity_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='ProjectActivity')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'project_activity_id',
            title='ProjectActivity container',
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
