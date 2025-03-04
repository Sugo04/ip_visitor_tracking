{
    'name': 'IP Visitor Tracking',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Localiza a los ususarios que se conecten geográficamente.',
    'author': 'Héctor Martín Ortega',
    'website': 'https://www.example.com',
    'depends': ['base', 'website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/visitor_tracking_views.xml',
    ],
    'image': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}