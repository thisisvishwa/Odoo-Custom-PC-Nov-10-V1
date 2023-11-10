```python
from odoo.tests import common

class TestOrderProcessing(common.TransactionCase):

    def setUp(self):
        super(TestOrderProcessing, self).setUp()
        self.Order = self.env['custom_pc_builder_module.order']

    def test_order_creation(self):
        """Test if order can be created with valid data"""
        order = self.Order.create({
            'user_id': 1,
            'component_ids': [(6, 0, [1, 2, 3])],
            'total_price': 500.00,
        })

        self.assertEqual(order.user_id.id, 1)
        self.assertEqual(len(order.component_ids), 3)
        self.assertEqual(order.total_price, 500.00)

    def test_order_update(self):
        """Test if order can be updated"""
        order = self.Order.create({
            'user_id': 1,
            'component_ids': [(6, 0, [1, 2, 3])],
            'total_price': 500.00,
        })

        order.write({
            'component_ids': [(6, 0, [1, 2])],
            'total_price': 400.00,
        })

        self.assertEqual(len(order.component_ids), 2)
        self.assertEqual(order.total_price, 400.00)

    def test_order_deletion(self):
        """Test if order can be deleted"""
        order = self.Order.create({
            'user_id': 1,
            'component_ids': [(6, 0, [1, 2, 3])],
            'total_price': 500.00,
        })

        order_id = order.id
        order.unlink()

        self.assertFalse(self.Order.search([('id', '=', order_id)]))
```