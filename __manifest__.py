# -*- coding: utf-8 -*-pack
{
    # App information
    'name': 'Company Credential Data',
    'category': 'Module',
    'version': '16.0.0',
    'summary': """""",
    'description': """ """,
    'depends': ['base'],

    'data': ['security/ir.model.access.csv',
             'views/res_company.xml',
             'views/company_credentials_data_views.xml',
             ],

    'author': 'Vraja Technologies',
    'maintainer': 'Vraja Technologies',
    'website': 'https://www.vrajatechnologies.com',
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}