from odoo import models, fields, api

class SaleOrderProductLost(models.Model):
    _name = 'sale.order.product.lost'
    _description = 'Product Lost in Sale Order'

    order_id = fields.Many2one('sale.order', string='Sale Order')
    move_id = fields.Many2one('account.move', string='Invoice')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    price = fields.Float(string='Price', required=True)
    tax_ids = fields.Many2many('account.tax', string='Taxes')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)
    subtotal_untaxed = fields.Float(string='Untaxed Subtotal', compute='_compute_subtotal_untaxed', store=True)

    # Compute untaxed subtotal (quantity * price)
    @api.depends('quantity', 'price')
    def _compute_subtotal_untaxed(self):
        for line in self:
            line.subtotal_untaxed = line.price * line.quantity

    # Compute subtotal (quantity * price + taxes)
    @api.depends('quantity', 'price', 'tax_ids')
    def _compute_subtotal(self):
        for line in self:
            taxes = line.tax_ids.compute_all(line.price * line.quantity)
            line.subtotal = taxes['total_included']
