# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import sinar.activity


class SinarActivityLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.activity)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.activity:default')


SINAR_ACTIVITY_FIXTURE = SinarActivityLayer()


SINAR_ACTIVITY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_ACTIVITY_FIXTURE,),
    name='SinarActivityLayer:IntegrationTesting',
)


SINAR_ACTIVITY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_ACTIVITY_FIXTURE,),
    name='SinarActivityLayer:FunctionalTesting',
)


SINAR_ACTIVITY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_ACTIVITY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarActivityLayer:AcceptanceTesting',
)
