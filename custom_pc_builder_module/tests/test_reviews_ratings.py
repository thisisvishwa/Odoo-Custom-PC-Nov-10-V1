```python
from odoo.tests import common
from ..models.review import ReviewSchema

class TestReviewsRatings(common.TransactionCase):

    def setUp(self):
        super(TestReviewsRatings, self).setUp()
        self.Review = self.env['custom_pc_builder_module.review']
        self.test_review_data = {
            'user_id': 1,
            'component_id': 1,
            'rating': 4,
            'comment': 'Good component!'
        }

    def test_review_creation(self):
        review = self.Review.create(self.test_review_data)
        self.assertEqual(review.user_id, self.test_review_data['user_id'])
        self.assertEqual(review.component_id, self.test_review_data['component_id'])
        self.assertEqual(review.rating, self.test_review_data['rating'])
        self.assertEqual(review.comment, self.test_review_data['comment'])

    def test_review_update(self):
        review = self.Review.create(self.test_review_data)
        updated_comment = 'Great component!'
        review.write({'comment': updated_comment})
        self.assertEqual(review.comment, updated_comment)

    def test_review_deletion(self):
        review = self.Review.create(self.test_review_data)
        review_id = review.id
        review.unlink()
        self.assertFalse(self.Review.search([('id', '=', review_id)]))
```