# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Biblioteca (models.Model):
    _name = 'biblioteca.libro'
    _description = 'Módulo que gestionará muchos aspectos de la Biblioteca'

    name = fields.Char(string='Title', required=True)
    description = fields.Char(string='description', required=True)
    autor = fields.Char(string='Autor', required=True)
    editor = fields.Char(string='Editor', required=True)
    editorial = fields.Char(string='Editorial', required=True)
    year_edicion = fields.Char(string='Año Edicion', required=True)
    genero = fields.Selection(string='Tipo De Barco',
                                     selection=[('1', 'Aventuras'),
                                     ('2', 'Ciencia ficción'),
                                     ('3', 'Los cuentos de hadas'),
                                     ('4', 'La novela gótica'),
                                     ('5', 'La novela policíaca'),
                                     ('6', 'El romance paranormal'),
                                     ('7', 'La novela distópica'),
                                     ('8', 'La novela fantástica')],
                                     copy=False, required=True)
    active = fields.Boolean(string='Active', default=True)
