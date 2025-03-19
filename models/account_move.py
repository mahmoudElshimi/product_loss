from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'
    product_lost_ids = fields.One2many('sale.order.product.lost', 'move_id', string='Product Lost')

    # Override the confirm button to add restrictions
    def action_post(self):
        for move in self:
            total_lost = sum(move.product_lost_ids.mapped('subtotal'))
            if self.env.user.has_group('product_loss.group_sales_manager'):
                return super(AccountMove, self).action_post()
            if self.env.user.has_group('product_loss.group_sales_user'):
                if total_lost > 1000:
                    raise ValidationError("Sales User: Total Product Lost exceeds 1000 SAR.")
                else:
                    return super(AccountMove, self).action_post()

            if self.env.user.has_group('product_loss.group_presales_user'):
                if total_lost > 100:
                    raise ValidationError("PreSales User: Total Product Lost exceeds 100 SAR.")
                else:
                    return super(AccountMove, self).action_post()
            raise ValidationError("You Have To Be In One Of The Product Loss Groups.")
