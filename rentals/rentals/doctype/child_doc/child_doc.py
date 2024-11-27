# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ChildDoc(Document):
	def validate(self):
		self.new_document()

	def new_document(self):
		doc = frappe.new_doc('Parent Doc')
		doc.first_name = 'Laya'
		doc.last_name = 'Das'
		doc.age = 23
		doc.insert()

	def new_document(self):
		doc = frappe.new_doc('Parent Doc')
		doc.first_name = 'Kunj'
		doc.last_name = 'Sahu'
		doc.age = 23
		doc.insert()		