from odoo import models, fields


class ResUsers(models.Model):
    """
        Extends the 'res.users' model to include a relationship with user-specific credentials.
    """
    _inherit = 'res.users'

    credential_ids = fields.One2many('company.credentials.data', 'user_id',
                                     help="List of credentials associated with this user.")