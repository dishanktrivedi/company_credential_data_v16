from odoo import models, fields


class ResCompany(models.Model):
    """
        Extends the 'res.company' model to include a relationship with company credentials.
    """
    _inherit = 'res.company'

    credential_ids = fields.One2many('company.credentials.data', 'company_id',
                                     help="List of credentials associated with this company.")