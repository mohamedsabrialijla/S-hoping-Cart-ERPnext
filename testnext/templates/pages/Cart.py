from __future__ import unicode_literals
import frappe
from frappe.website.utils import get_full_index

def get_context(context):
	context.items = frappe.get_list("Sales Orderr",fields = ["name_product","price_product","quentity_product","description_product"])




