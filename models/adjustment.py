from openerp.osv import osv, fields


class StockInventoryLine(osv.osv):
    _inherit = 'stock.inventory.line'

    def _get_template_product(self, cr, uid, context=None):
        if context is None:
            context = {}
        lines = context and context.get('active_ids', [])
	line_obj = self.pool.get('stock.inventory.line')
	if not lines:
	    return False

	line = line_obj.browse(cr, uid, lines[0])
	return line.product_id.product_tmpl_id.id


    _columns = {
	'date_done': fields.related('inventory_id', 'date', type="date", string='Date Done'),
	'product_tmpl_id': fields.related('product_id', 'product_tmpl_id', type="many2one", relation="product.template", string='Template Product'),
    }

    _defaults = {
	'product_tmpl_id': _get_template_product,
    }


