# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Mision_Espacial (models.Model):
    _name = 'mision_espacial'
    _description = 'Mision_Espacial Info'

    name = fields.Char(string='Title', required=True)
    dimensiones_del_barco = fields.Integer(string='Dimensiones Del Barco', required=True)

    combustibles = fields.Selection(string='Combustibles',
                             selection=[('1', 'Criogénicos'),
                             ('2', 'semi criogénicos'),
                             ('3', 'hipergólicos '),
                             ('4', 'sólidos ')],
                             copy=False, required=True)
    Tipo_De_Barco = fields.Selection(string='Tipo De Barco',
                                    selection=[('1', 'Nave espacial sobrevuelo'),
                                    ('2', 'Nave espacial Orbiter'),
                                    ('3', 'Nave espacial Atmosférica'),
                                    ('4', 'Lander'),
                                    ('5', 'Rover'),
                                    ('6', 'Nave espacial Penetradora'),
                                    ('7', 'Nave espacial Observatorio'),
                                    ('8', 'Nave espacial de comunicaciones')],
                                    copy=False, required=True)
    Numero_De_Pasajeros = fields.Integer(string='Numero De Pasajero', required=True)

    active = fields.Boolean(string='Active', default=True)

