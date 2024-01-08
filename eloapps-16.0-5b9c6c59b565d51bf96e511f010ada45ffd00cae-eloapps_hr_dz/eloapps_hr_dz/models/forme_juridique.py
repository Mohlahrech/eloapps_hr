# -*- coding: utf-8 -*-
from odoo import models, fields, api

from odoo.addons.eloapps_hr_dz.commun import data

class FormeJuridique(models.Model):

    _name = 'forme.juridique'
    _description = 'Forme jutidique'

    code = fields.Char(string='Code')

    name = fields.Char(string='Nom')

    # Concaténation du Code et du Nom dans les vues Partner et Company
    def name_get(self):
        result = []
        for record in self:
            result.append(
                (record.id, (record.code and (record.code + ' - ') or '') + record.name))
        return result

    @api.model
    def verifer_juridique_records(self):
        vals = []
        vals = data.FORME_JURIDIQUE
        for val in vals:
            if not self.search([('code','=',val['code'])]):
                self.create(val)