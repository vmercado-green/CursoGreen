# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Voluntarios_Cooperativos (models.Model):
    _name = 'voluntarios_cooperativos'
    _description = 'voluntarios_cooperativos Info'

    name = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description', required=True)
    tipotarea = fields.Selection(string='Tipo Tarea',
                              selection=[('1', 'Tarea 1'),
                              ('2', 'Tarea 2'),
                              ('3', 'Tarea 3')],
                              copy=False, required=True)
    tiempo_inicio = fields.Float(string='Tiempo Inicio', compute="_compute_time")
    tiempo_final = fields.Float(string='Tiempo Final', compute="_compute_time")
    active = fields.Boolean(string='Active', default=True)
