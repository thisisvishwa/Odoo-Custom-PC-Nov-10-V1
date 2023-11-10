```python
from odoo import models, fields, api

class Price(models.Model):
    _name = 'custom_pc_builder.price'
    _description = 'Price Model for Custom PC Builder'

    component_id = fields.Many2one('custom_pc_builder.component', ondelete='cascade', string="Component")
    price = fields.Float(string="Price")

    @api.onchange('component_id')
    def _onchange_component_id(self):
        self.price = self.component_id.price

    @api.model
    def update_price(self, component_id, new_price):
        price_record = self.search([('component_id', '=', component_id)], limit=1)
        if price_record:
            price_record.price = new_price
        else:
            self.create({
                'component_id': component_id,
                'price': new_price
            })

    @api.model
    def get_total_price(self, component_ids):
        total_price = 0.0
        for component_id in component_ids:
            price_record = self.search([('component_id', '=', component_id)], limit=1)
            if price_record:
                total_price += price_record.price
        return total_price
```