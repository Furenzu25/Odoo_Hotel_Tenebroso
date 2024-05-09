# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hoteldocuments(models.Model):
    _name = 'hotel.hoteldocuments'
    _description = 'Hotel Documents'
    _order = "name"
    
    name = fields.Char("Document Name")
    description = fields.Char("Document Description")
