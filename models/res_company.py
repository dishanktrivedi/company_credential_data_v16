from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    credential_ids = fields.One2many('company.credentials.data', 'company_id')