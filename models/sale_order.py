from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # One2many field for Product Lost
    product_lost_ids = fields.One2many('sale.order.product.lost', 'order_id', string='Product Lost')

    # Override _prepare_invoice to pass product_lost_ids to the invoice
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        if self.product_lost_ids:
            invoice_vals['product_lost_ids'] = [(0, 0, {
                'product_id': line.product_id.id,
                'quantity': line.quantity,
                'price': line.price,
                'tax_ids': [(6, 0, line.tax_ids.ids)],
                'subtotal': line.subtotal,
            }) for line in self.product_lost_ids]
        return invoice_vals
