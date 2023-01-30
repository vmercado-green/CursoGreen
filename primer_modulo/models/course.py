# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Course (models.Model):
    _name = 'curso.odoo'
    _description = 'Curso Info'

    name = fields.Char(string='Title',required=True)
    description=fields.Text (string= 'Description')

    level = fields.Selection (string='Level',
                              selection=[('1','Beginner'),
                              ('2','Intermediate'),
                              ('3','Advanced')],
                              copy=False)

    active = fields.Boolean(string='Active', default=True)
