# -*- coding: utf-8 -*-
{
    'name': 'Primer Modulo En Odoo.sh',
    'version': '1',
    'summary':'Hola Mundo1',
    'description': 'Hola Mundo',
    'category': 'Account',
    'author': 'GREEN-VICTOR MERCADO',
    'website':'https://www.greenapplic.com/',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/curso_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/curso_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}