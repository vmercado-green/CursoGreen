# -*- coding: utf-8 -*-
{
    
    'name': ' Misión Espacial de Odoo',
    'version': '1',
    'summary': 'Módulo que planifique y ayude a Odoo a llegar a la Luna',
    'description': 'Odoo Inc. está intentando visitar la Luna. Necesitan tu ayuda para crear una Aplicación para organizar la logística. Esto incluye la nave espacial y la tripulación',
    'category': 'Account',
    'author': 'GREEN-VICTOR MERCADO',
    'website':'https://www.greenapplic.com/',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
            'security/mision_espacial_security.xml',
            'security/ir.model.access.csv',
        ],
    'demo': ['demo/nave_demo.xml',],
    'installable': True,
    'application': True,
    'auto_install': False,
}