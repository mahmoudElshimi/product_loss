{
    'name': 'Product Loss',
    'version': '1.0',
    'category': 'Sales',
    "author": "Mahmoud ElShimi",
    "website": "mailto:mahmoudelshimi@protonmail.ch",
    'depends': ['base', 'sale_management', 'account'],
    "license": "Other proprietary",  # See LICENSE(MIT/X) File in the same dir.
    "images": [
        "static/description/icon.png",
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    "installable": True,
    "application": True,  # I set this to True on purpose to make the module easier to find in the Odoo Apps menu.
}
