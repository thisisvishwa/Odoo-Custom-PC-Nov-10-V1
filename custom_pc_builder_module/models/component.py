```python
from odoo import models, fields

class Component(models.Model):
    _name = 'pc.builder.component'
    _description = 'PC Component'

    name = fields.Char(string='Component Name', required=True)
    component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('cooling', 'Cooling'),
        ('lighting', 'Lighting'),
        ('case', 'Case'),
    ], string='Component Type', required=True)
    price = fields.Float(string='Price', required=True)
    image = fields.Binary(string='Image')
    description = fields.Text(string='Description')

    def selectComponent(self, component_id):
        selectedComponent = self.browse(component_id)
        return selectedComponent
```