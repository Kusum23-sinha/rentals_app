# Copyright (c) 2024, BWH and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_full_name_correctly_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "Ram"
		test_driver.last_name = "lal"
		test_driver.license_number = "ABC123456"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Ram lal")


	def test_full_name_correctly_set_when_last_name_not_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "Ram"
		test_driver.license_number= "ABC123456"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Ram")
