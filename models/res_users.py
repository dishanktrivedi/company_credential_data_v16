from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    credential_ids = fields.One2many('company.credentials.data', 'user_id')