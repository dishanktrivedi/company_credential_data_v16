from odoo import fields, models

class CompanyCredentialsData(models.Model):
    _name = 'company.credentials.data'
    _description = 'Company Credential Data'

    name = fields.Char()
    url = fields.Text(string="URL of the Company")
    username = fields.Text(string="Username")
    password = fields.Text(string="Password")
    description = fields.Text(string="Description")
    company_id = fields.Many2one('res.company', string="Company ID")