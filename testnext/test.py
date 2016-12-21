import frappe


@frappe.whitelist(allow_guest=True)
def view_data():


