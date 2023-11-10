```python
from odoo.tests import common
from ..models import price

class TestPriceEstimator(common.TransactionCase):

    def setUp(self):
        super(TestPriceEstimator, self).setUp()
        self.price_estimator = self.env['price.estimator']
        self.component1 = self.env['component'].create({'name': 'Component 1', 'price': 100})
        self.component2 = self.env['component'].create({'name': 'Component 2', 'price': 200})

    def test_estimate_price(self):
        self.price_estimator.selectedComponents = [self.component1.id, self.component2.id]
        self.price_estimator.estimatePrice()
        self.assertEqual(self.price_estimator.totalPrice, 300, "Price Estimation is incorrect")

    def test_price_update_on_component_change(self):
        self.price_estimator.selectedComponents = [self.component1.id, self.component2.id]
        self.price_estimator.estimatePrice()
        self.assertEqual(self.price_estimator.totalPrice, 300, "Initial Price Estimation is incorrect")
        
        self.component2.price = 250
        self.price_estimator.estimatePrice()
        self.assertEqual(self.price_estimator.totalPrice, 350, "Price Estimation after component price change is incorrect")
```