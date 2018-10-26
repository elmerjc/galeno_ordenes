# -*- coding: utf-8 -*-
from odoo import http

# class AsiLtda(http.Controller):
#     @http.route('/asi_ltda/asi_ltda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asi_ltda/asi_ltda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asi_ltda.listing', {
#             'root': '/asi_ltda/asi_ltda',
#             'objects': http.request.env['asi_ltda.asi_ltda'].search([]),
#         })

#     @http.route('/asi_ltda/asi_ltda/objects/<model("asi_ltda.asi_ltda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asi_ltda.object', {
#             'object': obj
#         })