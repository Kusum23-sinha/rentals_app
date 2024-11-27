# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Invoice(Document):
	def validate(self):
		total_price = 0
		for item in self.invoice_items:
			total = item.quantity * item.price
			total_price += total

		self.total_amount = total_price
		discount = self.discount
		discount_amount = (self.total_amount/100)*discount
		self.payable_amount = self.total_amount - discount_amount		