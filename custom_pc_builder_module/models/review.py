```python
from odoo import models, fields

class Review(models.Model):
    _name = 'custom_pc_builder_module.review'
    _description = 'Review'

    user_id = fields.Many2one('res.users', string='User')
    component_id = fields.Many2one('custom_pc_builder_module.component', string='Component')
    rating = fields.Selection([(num, str(num)) for num in range(1, 6)], 'Rating')
    comment = fields.Text('Comment')

    def postReview(self):
        # Code to post a review
        pass
```