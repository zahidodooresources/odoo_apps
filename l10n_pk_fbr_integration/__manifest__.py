# -*- coding: utf-8 -*-
{
    "name": "Pakistan FBR Digital Invoicing ",
    "version": "1.0",
    "category": "Accounting",
    'sequence': 215,
    "summary": "Integrate Odoo invoices with FBR Digital Invoicing APIs to get real-time taxes/validation",

    'website': "https://www.zalinotech.com",
    'author': 'Zalino Tech (Private) Limited',
    'company': 'Zalino Tech',
    'maintainer': 'Zalino Tech',
    "description": "Integrate Odoo invoices with FBR Digital Invoicing APIs to get real-time taxes/validation.",

    "depends": ['account'],
    "data": [
         "security/ir.model.access.csv",
        "views/res_config_views.xml",
        "views/account_move_view.xml",
        "views/product_template.xml",
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    "installable": True,
    "application": False,
    "auto_install": False,
}
