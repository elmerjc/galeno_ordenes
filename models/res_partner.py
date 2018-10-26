# -*- coding: utf-8 -*-

from odoo import models, fields, api

class res_partner(models.Model):
	_inherit = 'res.partner'

	tecnico = fields.Boolean(
		'Tecnico',
		help="Marca esta opcion si es Tecnico.")