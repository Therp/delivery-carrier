{
    "name": "Tracking URL Clickable Extension",
    "summary": """
        lickable tracking URLs on pickings and sales""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "maintainers": ["ntsirintanis"],
    "author": "Therp BV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/delivery-carrier",
    "depends": ["delivery_carrier_default_tracking_url", "sale_stock"],
    "data": ["views/sale_order_views.xml", "views/stock_picking_views.xml"],
}
