from __future__ import unicode_literals
import frappe
from frappe.website.utils import get_full_index

def get_context(context):
#	context.items = frappe.get_list("Item",fields = ["thumbnail","item_name","description","standard_rate"])



	raw = frappe.db.sql("""SELECT tabItem.item_code, tabItem.item_name, tabItem.thumbnail, tabItem.standard_rate,
	`tabItem Price`.price_list_rate, tabItem.description, tabItem.name from tabItem
					 INNER JOIN `tabItem Price` ON tabItem.item_code = `tabItem Price`.item_code""")
	context.items = list(raw)




@frappe.whitelist(allow_guest=True)
def insert_OrderSales(item_name,price,descriptin,quantity,ItemName,quent):
    frappe.get_doc({
        "doctype":"Sales Orderr",
        "name_product":item_name,
        "price_product":price,
        "description_product": descriptin,
        "quentity_product": quantity
    }).insert(ignore_permissions=True)
    # frappe.get_doc({
    #     "doctype": "Item",
    #     "standard_rate": quent
    # }).insert(ignore_permissions=True)

    sq = " update tabItem set standard_rate=standard_rate-{0} where name='{1}' ".format(quantity,ItemName)
    frappe.db.sql(sq)
    frappe.db.commit()
