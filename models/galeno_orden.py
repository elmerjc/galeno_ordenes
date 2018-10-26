# -*- coding: utf-8 -*-

from odoo import models, fields, api

class galeno_diente(models.Model):
	_name = 'galeno.diente'
	_description = "Piezas dentales para la radiografía periapical"
	_order = "name"
	
	name = fields.Char('Diente')
	maxilar = fields.Selection([
			('Superior', 'Superior'),
			('Inferior', 'Inferior')],
		string='Maxilar')
	lado = fields.Selection([
			('Derecho', 'Derecho'),
			('Izquierdo', 'Izquierdo')],
		string='Lado')
	grupo = fields.Selection([
			('1', '1'),
			('2', '2')],
		string='Grupo')

	_sql_constraints = [
		('name_uniq', 'unique(name)', 'La pieza dental debe ser unico!'),
	]

class galeno_orden(models.Model):
	_name = "galeno.orden"
	_description = "Ordenes de atencion"
	_order = "fecha desc, id desc"

	name = fields.Char(
		string='Código',
		index=True,
		readonly=True,
		copy=False,
		help='Código de la orden',
		default=lambda self: 'Nuevo')
	fecha = fields.Date(
		string='Fecha',
		copy=False,
		help='Fecha de la orden')
	cliente_id = fields.Many2one(
		'galeno.paciente',
		string="Cliente",
		change_default=True,
		required=True,
		track_visibility='always')
	cliente_edad = fields.Integer(
		related='cliente_id.edad',
		string="Edad",
		readonly=True)
	cliente_email = fields.Char(
		string="Email",
		related='cliente_id.email',
		readonly=True)
	cliente_datebd = fields.Date(
		string="Fecha de nacimiento",
		related='cliente_id.datebd',
		readonly=True)
	cliente_phone = fields.Char(
		string="Telefono / Celular",
		related='cliente_id.phone',
		readonly=True)
	cliente_dni = fields.Char(
		string="DNI / RUT",
		related='cliente_id.dni',
		readonly=True)
	cliente_sexo = fields.Selection([
			('M', 'M'),
			('F', 'F'),
		],
		string="Sexo",
		related='cliente_id.sexo',
		readonly=True)
	motivo = fields.Char(
		string='Motivo de la consulta',
		help='Motivo de la consulta')
	r_periapical = fields.Boolean(
		string='Radiografía Periapical',
		help='Seleccionar si es una radiografía periapical')
	dientes_msd1_ids = fields.Many2many(
		'galeno.diente',
		'galeno_periapical_diente_rel',
		'orden_id',
		'diente_ids', 
		string='Dientes maxilar superior derecho 1')
	dientes_msd2_ids = fields.Many2many(
		'galeno.diente',
		'galeno_periapical_diente_rel',
		'orden_id',
		'diente_ids', 
		string='Dientes maxilar superior derecho 2')
	dientes_msi1_ids = fields.Many2many(
		'galeno.diente',
		'galeno_periapical_diente_rel',
		'orden_id',
		'diente_ids', 
		string='Dientes maxilar superior izquierdo 1')
	dientes_msi2_ids = fields.Many2many(
		'galeno.diente',
		'galeno_periapical_diente_rel',
		'orden_id',
		'diente_ids', 
		string='Dientes maxilar superior izquierdo 2')
	dientes_mid1_ids = fields.Many2many(
		'galeno.diente',
		'galeno_periapical_diente_rel',
		'orden_id',
		'diente_ids', 
		string='Dientes maxilar inferior derecho 1')
	dientes_mid2_ids = fields.Many2many(
		'galeno.diente',
		'galeno_periapical_diente_rel',
		'orden_id',
		'diente_ids', 
		string='Dientes maxilar inferior derecho 2')
	dientes_mii1_ids = fields.Many2many(
		'galeno.diente',
		'galeno_periapical_diente_rel',
		'orden_id',
		'diente_ids', 
		string='Dientes maxilar inferior izquierdo 1')
	dientes_mii2_ids = fields.Many2many(
		'galeno.diente',
		'galeno_periapical_diente_rel',
		'orden_id',
		'diente_ids', 
		string='Dientes maxilar inferior izquierdo 2')
	r_bitewing = fields.Boolean(
		string='Radiografía Bitewing',
		help='Seleccionar si es una radiografía bitewing')
	r_bw_molar_d = fields.Boolean(
		string='Molar')
	r_bw_premolar_d = fields.Boolean(
		string='Pre Molar')
	r_bw_molar_i = fields.Boolean(
		string='Molar')
	r_bw_premolar_i = fields.Boolean(
		string='Pre Molar')
	r_bw_serie = fields.Boolean(
		string='Serie radiográfica (14PP + 2BW)')
	r_bw_estudio = fields.Boolean(
		string='Estudio localizacion')
	r_oclusal = fields.Boolean(
		string='Radiografía Oclusal',
		help='Seleccionar si es una radiografía oclusal')
	r_os_sup = fields.Char(
		string='SUP')
	r_os_inf = fields.Char(
		string='INF')
	r_os_donovan = fields.Char(
		string='DONOVAN')
	r_os_grid = fields.Boolean(
		string='Con Grid')
	r_panoramica = fields.Boolean(
		string='Panoramica',
		help='Seleccionar si es una radiografía panoramica')
	r_lateral = fields.Boolean(
		string='Lateral',
		help='Seleccionar si es una radiografía lateral')
	r_atm = fields.Boolean(
		string='ATM (B. abrierta / B. cerrada)',
		help='Seleccionar si es una radiografía ATM')
	r_frontal = fields.Boolean(
		string='Frontal (P-A/A-P)',
		help='Seleccionar si es una radiografía Frontal')
	r_waters = fields.Boolean(
		string='Waters',
		help='Seleccionar si es una radiografía waters')
	r_lateral_estricta = fields.Boolean(
		string='Lateral estricta 7ma vertebra',
		help='Seleccionar si es una radiografía lateral estricta 7ma vertebra')
	r_carpal = fields.Boolean(
		string='Carpal',
		help='Seleccionar si es una radiografía carpal')
	r_towne = fields.Boolean(
		string='Inversa de Towne',
		help='Seleccionar si es una radiografía Towne')
	r_px_lx = fields.Boolean(
		string='PX, LX (2BW + 2PERIA)',
		help='Seleccionar si es una radiografía PX, LX')
	r_extraoral_esp = fields.Char(
		string='Especificaciones para el estudio solicitado')
	d_orto1 = fields.Boolean(
		string='Orto 1: PX + LX c/análisis (incluye 2 análisis + fotos extraorales)')
	d_orto2 = fields.Boolean(
		string='Orto 2: PX + LX c/análisis + fotos extraorales e intraorales (incluye 2 análisis))')
	d_ricketts = fields.Boolean(
		string='Ricketts',
		help='Seleccionar si es un análisis cefalométrico de Ricketts')
	d_steiner = fields.Boolean(
		string='Steiner',
		help='Seleccionar si es un análisis cefalométrico de Steiner')
	d_upch = fields.Boolean(
		string='U.P.C.H.',
		help='Seleccionar si es un análisis cefalométrico de U.P.C.H.')
	d_tejidos_blandos = fields.Boolean(
		string='Tejidos blandos',
		help='Seleccionar si es un análisis cefalométrico de tejidos blandos')
	d_ricketts_resumido = fields.Boolean(
		string='Ricketts resumido',
		help='Seleccionar si es un análisis cefalométrico de Ricketts resumido')
	d_jarabak = fields.Boolean(
		string='Jarabak',
		help='Seleccionar si es un análisis cefalométrico de Jarabak')
	d_bjork = fields.Boolean(
		string='Bjork',
		help='Seleccionar si es un análisis cefalométrico de Bjork')
	d_vto_crecimiento = fields.Boolean(
		string='Vto. crecimiento',
		help='Seleccionar si es un análisis cefalométrico de Vto. crecimiento')
	d_schwartz = fields.Boolean(
		string='Schwartz',
		help='Seleccionar si es un análisis cefalométrico de Schwartz')
	d_downs = fields.Boolean(
		string='Downs',
		help='Seleccionar si es un análisis cefalométrico de Downs')
	d_burstone = fields.Boolean(
		string='Burstone - Legan',
		help='Seleccionar si es un análisis cefalométrico de Burstone - Legan')
	d_namara = fields.Boolean(
		string='Mc Namara',
		help='Seleccionar si es un análisis cefalométrico de Mc Namara')
	d_rocabado = fields.Boolean(
		string='Rocabado',
		help='Seleccionar si es un análisis cefalométrico de Rocabado')
	d_tweed = fields.Boolean(
		string='Tweed - Merrifield',
		help='Seleccionar si es un análisis cefalométrico de Tweed - Merrifield')
	d_roth = fields.Boolean(
		string='Roth - Jarabak',
		help='Seleccionar si es un análisis cefalométrico de Roth - Jarabak')
	f_intraorales = fields.Boolean(
		string='Intraorales',
		help='Seleccionar si es una fotograía clínica de intraorales')
	f_extraorales = fields.Boolean(
		string='Extraorales',
		help='Seleccionar si es una fotograía clínica de extraorales')
	f_otros = fields.Char(
		string='Otros')
	t_software = fields.Selection([
			('Real Scan', 'Real Scan'),
			('Xelis', 'Xelis')],
		string='Software')
	t_sinanalisis = fields.Boolean(
		string='Sin análisis (sólo CD)')
	t_conanalisis = fields.Boolean(
		string='Con análisis')
	t_implantes = fields.Boolean(
		string='Implantes')
	t_implantes_maxilar = fields.Selection([
			('Maxilar superior', 'Maxilar superior'),
			('Maxilar inferior', 'Maxilar inferior')],
		string='Maxilar')
	t_endodoncia = fields.Boolean(
		string='Endodoncia')
	t_fractura = fields.Boolean(
		string='Fractura radicular')
	t_implantes_guia = fields.Selection([
			('SI', 'SI'),
			('NO', 'NO')],
		string='Paciente trae guía')
	t_localizacion = fields.Boolean(
		string='Localización de diente impactado')
	t_localizacion_esp = fields.Char(
		string='Localización de diente impactado')
	t_area = fields.Boolean(
		string='Área patológica')
	t_area_esp = fields.Char(
		string='Área patológica')
	t_senos = fields.Boolean(
		string='Senos maxilares')
	t_senos_esp = fields.Char(
		string='Senos maxilares')
	t_atm = fields.Boolean(
		string='ATM (B. abierta/B. cerrada)')
	t_atm_esp = fields.Char(
		string='ATM (B. abierta/B. cerrada)')
	t_otros = fields.Boolean(
		string='Otros / Obs')
	t_otros_esp = fields.Char(
		string='Otros / Obs')
	indicaciones = fields.Text(
		string='Indicaciones',
		copy=False,
		help='Indicaciones del dentista')
	state = fields.Selection([
			('ABIERTO', 'ABIERTO'),
			('ATENDIDO', 'ATENDIDO'),
			('CANCELADO', 'CANCELADO'),
			('CERRADO', 'CERRADO'),
		],
		string='Estado',
		help="Estado de la orden de atención")

	_sql_constraints = [
		('name_uniq', 'unique(name)', 'El código de la orden de atencion debe ser unico'),
	]

	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('galeno.orden')
		result = super(galeno_orden, self).create(vals)
		return result