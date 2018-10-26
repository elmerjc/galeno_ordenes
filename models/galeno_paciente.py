# -*- coding: utf-8 -*-

from odoo import models, fields, api

class galeno_paciente(models.Model):
	_name = "galeno.paciente"
	_description = "Paciente"
	_order = "name, id desc"

	name = fields.Char(
		string='Nombre',
		copy=False,
		help='Nombre completo')
	lastname = fields.Char(
		string='Apellidos',
		copy=False,
		required=True,
		help='Apellidos del paciente')
	firstname = fields.Char(
		string='Nombres',
		copy=False,
		required=True,
		help='Nombres del paciente')
	dni = fields.Char(
		string='DNI',
		index=True,
		store=True,
		copy=False,
		help='DNI / RUT')
	phone = fields.Char(
		string='Telefono / Celular',
		copy=False,
		help='Telefono o celular del paciente')
	email = fields.Char(
		string='Email',
		copy=False,
		help='Email del paciente')
	datebd = fields.Date(
		string='Fecha de nacimiento',
		required=True,
		help='Fecha de nacimiento del paciente')
	edad = fields.Integer(
		string='Edad',
		readonly=True,
		help='Edad del paciente')
	sexo = fields.Selection([
			('M', 'M'),
			('F', 'F'),
		],
		string='Sexo',
		required=True,
		help='Sexo del paciente')

	_sql_constraints = [
		('dni_uniq', 'unique(dni)', 'El DNI del paciente debe ser unico'),
	]