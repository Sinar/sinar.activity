# -*- coding: utf-8 -*-
from sinar.activity.behaviors.activity_types import IActivityTypesMarker
from sinar.activity.testing import SINAR_ACTIVITY_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ActivityTypesIntegrationTest(unittest.TestCase):

    layer = SINAR_ACTIVITY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_activity_types(self):
        behavior = getUtility(IBehavior, 'sinar.activity.activity_types')
        self.assertEqual(
            behavior.marker,
            IActivityTypesMarker,
        )
