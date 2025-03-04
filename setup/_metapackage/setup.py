import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-stock-logistics-warehouse",
    description="Meta package for oca-stock-logistics-warehouse Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_move_line_product',
        'odoo12-addon-account_move_line_stock_info',
        'odoo12-addon-stock_account_change_qty_reason',
        'odoo12-addon-stock_available_unreserved',
        'odoo12-addon-stock_change_qty_reason',
        'odoo12-addon-stock_demand_estimate',
        'odoo12-addon-stock_inventory_chatter',
        'odoo12-addon-stock_inventory_exclude_sublocation',
        'odoo12-addon-stock_inventory_lockdown',
        'odoo12-addon-stock_inventory_preparation_filter',
        'odoo12-addon-stock_mts_mto_rule',
        'odoo12-addon-stock_orderpoint_manual_procurement',
        'odoo12-addon-stock_orderpoint_manual_procurement_uom',
        'odoo12-addon-stock_orderpoint_move_link',
        'odoo12-addon-stock_orderpoint_purchase_link',
        'odoo12-addon-stock_orderpoint_uom',
        'odoo12-addon-stock_packaging',
        'odoo12-addon-stock_picking_procure_method',
        'odoo12-addon-stock_request',
        'odoo12-addon-stock_request_picking_type',
        'odoo12-addon-stock_request_purchase',
        'odoo12-addon-stock_request_tier_validation',
        'odoo12-addon-stock_secondary_unit',
        'odoo12-addon-stock_warehouse_calendar',
        'odoo12-addon-stock_warehouse_orderpoint_stock_info',
        'odoo12-addon-stock_warehouse_orderpoint_stock_info_unreserved',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
