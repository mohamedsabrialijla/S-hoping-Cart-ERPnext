import frappe



@frappe.whitelist(allow_guest=True)
def insert_issu(email,subject,name,mssage,phone):
    frappe.get_doc({
        "doctype":"Issue",
        "raised_by":email,
        "subject":subject
    }).insert(ignore_permissions=True)
    frappe.get_doc({
        "doctype": "Lead",
        "lead_name": name,
        "website": mssage,
        "phone": phone
    }).insert(ignore_permissions=True)