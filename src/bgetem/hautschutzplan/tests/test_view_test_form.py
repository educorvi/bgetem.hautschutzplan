# -*- coding: utf-8 -*-
from bgetem.hautschutzplan.testing import BGETEM_HAUTSCHUTZPLAN_FUNCTIONAL_TESTING
from bgetem.hautschutzplan.testing import BGETEM_HAUTSCHUTZPLAN_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = BGETEM_HAUTSCHUTZPLAN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_test_form_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='test-form'
        )
        self.assertTrue(view.__name__ == 'test-form')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in test-form'
        # )

    def test_test_form_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='test-form'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = BGETEM_HAUTSCHUTZPLAN_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
