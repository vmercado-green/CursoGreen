# -*- coding: utf-8 -*-
{
    'name': 'Administración de la Biblioteca ',
    'version': '1',
    'summary': 'Módulo que gestionará muchos aspectos de la Biblioteca',
    'description': 'Su biblioteca local quiere usar Odoo para administrar sus libros y clientes. Necesitarán ayuda para procesar a los clientes sacando libros y para organizar libros y alquileres.',
    'category': 'Account',
    'author': 'GREEN-VICTOR MERCADO',
    'website':'https://www.greenapplic.com/',
    'license': 'AGPL-3',
    'depends': ['base'],

    'demo': [
        'demo/libro_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}