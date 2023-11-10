```python
from odoo import models, fields

class Customization(models.Model):
    _name = 'custom.pc.builder.customization'
    _description = 'PC Build Customization'

    cooling_solution = fields.Selection([
        ('air', 'Air Cooling'),
        ('liquid', 'Liquid Cooling'),
    ], string='Cooling Solution', default='air')

    lighting = fields.Boolean(string='Include Lighting', default=False)

    casing_modifications = fields.Text(string='Casing Modifications')

    def customizeBuild(self, cooling_solution, lighting, casing_modifications):
        self.cooling_solution = cooling_solution
        self.lighting = lighting
        self.casing_modifications = casing_modifications
```