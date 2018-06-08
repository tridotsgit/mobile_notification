# -*- coding: utf-8 -*-
# Copyright (c) 2018, Tridots Tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AppNotificationCenter(Document):
	pass


@frappe.whitelist()
def insert_notification(name,message):
	frappe.get_doc({
		"doctype": "Notification",
        "name": get_random(),
        "notification_name":name,
        "message":message,
        "status":"Not visited"
		}).insert()


@frappe.whitelist()
def get_random():
	import random 
	import string
	random = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(6)])
	Name=frappe.db.get_all('Notification',fields=['name'])
	for x in Name:
		if x.name==random:
			random=get_random()
	return random

