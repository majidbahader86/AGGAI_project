from django.test import TestCase
from django.contrib.auth.models import User
from disease_detection.models import DiseaseIdentificationRequest
from disease_detection.forms import DiseaseIdentificationRequestForm

class DiseaseIdentificationRequestFormTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_form_fields(self):
        form = DiseaseIdentificationRequestForm()
        self.assertEqual(list(form.fields), ['image', 'ai_requested'])

    def test_form_valid_data(self):
        form_data = {
            'ai_requested': True,
        }
        form = DiseaseIdentificationRequestForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {
            'ai_requested': 'not_a_boolean',
        }
        form = DiseaseIdentificationRequestForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_save(self):
        form_data = {
            'ai_requested': True,
        }
        form = DiseaseIdentificationRequestForm(data=form_data)
        self.assertTrue(form.is_valid())
        disease_request = form.save(commit=False)
        disease_request.user = self.user
        disease_request.save()

        self.assertEqual(disease_request.ai_requested, True)
        self.assertEqual(disease_request.user, self.user)
        self.assertIsNone(disease_request.image)

    def test_form_widgets(self):
        form = DiseaseIdentificationRequestForm()
        self.assertIsInstance(form.fields['ai_requested'].widget, forms.CheckboxInput)

# The below lines ensure the tests are executed as part of the test suite
if __name__ == "__main__":
    TestCase.main()
