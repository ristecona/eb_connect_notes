# -*- coding: utf-8 -*-
{
    'name': "eb_connect_notes_with_existing_fields",

    'summary': """
       Connect x_so_note with x_inv_note""",

    'description': """
        Connect x_so_note with x_inv_note
    """,

    'author': "Cona Cons",
    'website': "http://www.euroblaze.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',

}