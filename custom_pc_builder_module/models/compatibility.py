```python
from odoo import models, fields, api

class Compatibility(models.Model):
    _name = 'pcbuilder.compatibility'
    _description = 'PC Builder Compatibility'

    component_ids = fields.Many2many('pcbuilder.component', string='Components')
    is_compatible = fields.Boolean(string='Is Compatible', compute='_compute_compatibility')

    @api.depends('component_ids')
    def _compute_compatibility(self):
        for record in self:
            # Placeholder for compatibility logic
            # This should be replaced with actual compatibility checking logic
            record.is_compatible = True

    def check_compatibility(self, component_ids):
        self.component_ids = component_ids
        return self.is_compatible
```