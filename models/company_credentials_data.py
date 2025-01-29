from odoo import fields, models

class CompanyCredentialsData(models.Model):
    """
        This model stores credential details for companies and users,
        including login information and descriptions.
    """
    _name = 'company.credentials.data'
    _description = 'Company Credential Data'

    name = fields.Char(string="Credential Name",help="Name of the credential.")
    url = fields.Text(string="URL", help="Website or service URL associated with the credentials.")
    username = fields.Text(string="Username", help="Username for login.")
    password = fields.Text(string="Password", help="Password for login.")
    description = fields.Text(string="Description", help="Additional details about the credential.")
    company_id = fields.Many2one('res.company', string="Company ID", help="The company associated with this credential.")
    user_id = fields.Many2one('res.users', string="User ID", help="The user associated with this credential.")
