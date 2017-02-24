from openerp.osv import osv, fields

class ProductTemplate(osv.osv):
    _inherit = 'product.template'
    _columns = {
	'adjustments': fields.one2many('stock.inventory.line', 'product_tmpl_id', 'Adjustments'),
    }
