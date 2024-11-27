# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Voterid(Document):
    def validate(self):
        if self.age > 18:
            frappe.msgprint("You can vote")
           
        else:
             frappe.throw("Person's age must be at least 18")
            
