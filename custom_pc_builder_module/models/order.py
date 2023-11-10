```python
from odoo import models, fields, api

class Order(models.Model):
    _name = 'custom_pc_builder.order'
    _description = 'Order for Custom PC Builder'

    user_id = fields.Many2one('res.users', string='User')
    component_ids = fields.Many2many('custom_pc_builder.component', string='Components')
    total_price = fields.Float(compute='_compute_total_price', string='Total Price')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft', string='Status')

    @api.depends('component_ids')
    def _compute_total_price(self):
        for order in self:
            order.total_price = sum(component.price for component in order.component_ids)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'
```