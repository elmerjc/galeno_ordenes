# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class mantenimiento_esterilizador(models.Model):
	_name = "mantenimiento.esterilizador"
	_description = "Mantenimiento Esterilizadores"
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
	area = fields.Selection([
			('SALA EXTRACCION', 'SALA EXTRACCION'),
			('TS', 'TS'),
			('CULTIVO 1', 'CULTIVO 1'),
			('SUBCULTIVO', 'SUBCULTIVO'),
			('TTO', 'TTO'),
		],
		string='Area',
		required=True,
		help="Seleccione el area donde se realizo el mantenimiento")
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
		'mantenimiento.esterilizador.linea',
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
		vals['name'] = self.env['ir.sequence'].next_by_code('mantenimiento.esterilizador')
		result = super(mantenimiento_esterilizador, self).create(vals)
		return result

	@api.onchange('equipo_id', 'area')
	def onchange_equipo_id(self):
		mantenimiento_line = []
		warning = {}

		tareas = {
			'1':'Revisión de funcionamiento del equipo.',
			'2':'Temperatura  250°C',
		}

		if self.equipo_id:
			if not self.area:
				raise UserError('Seleccione el area primero.')

			if self.area == 'SALA EXTRACCION':
				j = 7
			if self.area == 'TS':
				j = 2
			if self.area == 'CULTIVO 1':
				j = 2
			if self.area == 'SUBCULTIVO':
				j = 5
			if self.area == 'TTO':
				j = 1

			sequence = 0
			
			for k in range(0, j):
				equipo_cont = 0
				for i in range(0, 2):
					values = {}
					equipo_cont = k + 1
					values['area'] = self.area
					values['name'] = 'CFL' + str(equipo_cont)
					if i % 2:
						values['tarea'] = tareas['2']
					else:
						values['tarea'] = tareas['1']
					values['numero'] = i + 1
					values['visto_a'] = False
					values['visto_b'] = False
					values['sequence'] = sequence + 1
					values['valor'] = 0
					values['detalle'] = ''
					mantenimiento_line.append([0, 0, values])
					sequence += 1

		return {'value': {'mantenimiento_linea_ids': mantenimiento_line},
				'warning': warning }

class mantenimiento_esterilizador_linea(models.Model):
	_name = "mantenimiento.esterilizador.linea"
	_description = "Tareas de mantenimiento"
	_order = "mantenimiento_id, id"

	name = fields.Char(
		string='Equipo')
	tarea = fields.Char(
		string='Tarea')
	numero = fields.Integer(
		string='N°')
	visto_a = fields.Boolean(
		string='A',
		copy=False)
	visto_b = fields.Boolean(
		string='B',
		copy=False)
	area = fields.Char(
		string='Area',
		copy=False)
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
		'mantenimiento.esterilizador',
		string='Mantenimiento',
		ondelete='cascade',
		index=True)
	valor = fields.Integer(
		string='Valor',
		default=0,
		help='Valor de la tarea de mantenimiento')
	detalle = fields.Char(
		string='Observaciones',
		copy=False,
		help='Observacion de la tarea de mantenimiento')