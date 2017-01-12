# -*- coding: utf-8 -*-
from openerp import models

class vat_unico_res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    _sql_constraints = [
        ('name_uniq', 'unique(vat)', u"Ya fue registrada una empresa o persona con este numero de RNC/Cédula"),
    ]
