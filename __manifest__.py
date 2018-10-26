# -*- coding: utf-8 -*-
{
    'name': "Galeno",

    'summary': """
        Acceso a medicos por una extranet, para realizar ordenes de atención
        """,

    'description': """
        Acceso a medicos por una extranet, para realizar ordenes de atención
    """,

    'author': "ARC",
    'website': "http://www.arc.pe",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/asi_ltda_security.xml',
        #'security/ir.model.access.csv',
        'views/menu_view.xml',
        #'views/galeno_cliente_view.xml',
        'views/galeno_orden_view.xml',
        'views/galeno_orden_sequence.xml',
        'data/dientes_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}