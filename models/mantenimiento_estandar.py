# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class mantenimiento_estandar(models.Model):
	_name = "mantenimiento.estandar"
	_description = "Mantenimiento estandar"
	_order = "fecha desc, id desc"

	name = fields.Char(
		string='Código',
		index=True,
		readonly=True,
		copy=False,
		help='Código del mantenimiento',
		default=lambda self: 'Nuevo')
	fecha = fields.Date(
		string='Fecha',
		copy=False,
		help='Fecha del mantenimiento')
	semana_mes = fields.Selection([
			('SEMANA 1', 'SEMANA 1'),
			('SEMANA 2', 'SEMANA 2'),
			('SEMANA 3', 'SEMANA 3'),
			('SEMANA 4', 'SEMANA 4'),
			('SEMANA 5', 'SEMANA 5'),
			('MENSUAL', 'MENSUAL'),
		],
		string='Semanal / Mensual',
		required=True,
		help="Seleccione la semana que se realizo el mantenimiento")
	equipo_cliente_id = fields.Many2one(
		'res.partner',
		related='equipo_id.cliente_id',
		string="Cliente",
		readonly=True)
	equipo_tipo_id = fields.Many2one(
		'equipo.tipo',
		related='equipo_id.tipo_id',
		string="Equipo",
		readonly=True)
	equipo_localizacion = fields.Char(
		related='equipo_id.localizacion',
		store=True,
		readonly=True,
		copy=False)
	equipo_id = fields.Many2one(
		'equipo.estandar',
		string='Equipo',
		change_default=True,
		required=True,
		track_visibility='always',
		help='Equipo a realizar el mantenimiento')
	tecnico_id = fields.Many2one(
		'res.partner',
		string='Tecnico',
		change_default=True,
		required=True,
		track_visibility='always',
		help='Tecnico que realiza el mantenimiento')
	mantenimiento_linea_ids = fields.One2many(
		'mantenimiento.linea',
		'mantenimiento_id',
		string='Tareas de mantenimiento',
		copy=True)
	observacion = fields.Text(
		string='Observaciones',
		copy=False,
		help='Observaciones de la tarea de mantenimiento')

	_sql_constraints = [
		('name_uniq', 'unique(name)', 'Código unico de producto'),
	]

	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('mantenimiento.estandar')
		result = super(mantenimiento_estandar, self).create(vals)
		return result

	@api.onchange('equipo_id', 'semana_mes')
	def onchange_equipo_id(self):
		mantenimiento_line = []
		warning = {}

		if self.equipo_id:
			if not self.semana_mes:
				self.equipo_id = False
				raise UserError('Seleccione la semana o mes primero.')

			tarea_obj = self.env['mantenimiento.tarea']
			tarea_ids = tarea_obj.search([('tipo_id', '=', self.equipo_tipo_id.id), ('semana_mes', 'like', self.semana_mes[0:5]
)])
			if tarea_ids:
				sequence = 0
				for tarea in tarea_ids:
					values = {}
					values['name'] = tarea.name
					values['tarea_id'] = tarea.id
					values['visto_bueno'] = False
					values['sequence'] = sequence + 1
					values['valor'] = 0
					values['detalle'] = ''
					mantenimiento_line.append([0, 0, values])
			else:
				warning = {
						'title': ('Error'),
						'message' : 'Equipo no tiene asignado tareas de mantenimiento'
					}

		return {'value': {'mantenimiento_linea_ids': mantenimiento_line},
				'warning': warning }

class mantenimiento_linea(models.Model):
	_name = "mantenimiento.linea"
	_description = "Tareas de mantenimiento"
	_order = "mantenimiento_id, id"

	name = fields.Char(
		string='Tarea')
	tarea_id = fields.Many2one(
		'mantenimiento.tarea',
		string='Tarea',
		change_default=True,
		required=True,
		track_visibility='always',
		help='Tarea realizada del mantenimiento')
	visto_bueno = fields.Boolean(
		string='V°B°',
		copy=False,
		help='Visto bueno del mantenimiento')
	visto_a = fields.Float(
		string='A',
		copy=False,
		help='A',
		digits=(6, 1))
	visto_b = fields.Float(
		string='B',
		copy=False,
		help='B',
		digits=(6, 1))
	sequence = fields.Integer(
		string='N°',
		default=1,
		help='Secuencia')
	mantenimiento_equipo_id = fields.Many2one(
		'equipo.tipo',
		related='mantenimiento_id.equipo_id',
		string="Equipo",
		readonly=True)
	mantenimiento_id = fields.Many2one(
		'mantenimiento.estandar',
		string='Mantenimiento',
		ondelete='cascade',
		index=True)
	valor = fields.Integer(
		string='Valor',
		default=0,
		help='Valor de la tarea de mantenimiento')
	detalle = fields.Char(
		string='Detalle',
		copy=False,
		help='Detalle de la tarea de mantenimiento')

	_sql_constraints = [
		('tarea_uniq', 'unique(tarea_id,mantenimiento_id)', 'La tarea por mantenimiento debe ser unico'),
	]


class mantenimiento_tarea(models.Model):
	_name = "mantenimiento.tarea"
	_description = "Tarea de mantenimiento"
	_order = "tipo_id asc, semana_mes desc"

	name = fields.Char(string='Tarea', required=True)
	tipo_id = fields.Many2one(
		'equipo.tipo',
		string='Equipo',
		required=True)
	semana_mes = fields.Selection([
			('SEMANAL', 'SEMANAL'),
			('MENSUAL', 'MENSUAL'),
		],
		string='Semanal / Mensual',
		required=True,
		help="Seleccione la semana que se realizo el mantenimiento")

	_sql_constraints = [
		('name_uniq', 'unique(name,tipo_id)', 'La tarea por equipo debe ser unica'),
	]