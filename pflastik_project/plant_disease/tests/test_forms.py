from django.test import TestCase
from ..forms import (
    DiseaseCategoryForm, PlantPartForm, DiseaseForm, DiseaseImageForm,
    EuropeanDiseaseForm, PlantForm, PlantImageForm
)
from ..models import DiseaseCategory, PlantPart, Disease, DiseaseImage, EuropeanDisease, Plant, PlantImage

class DiseaseCategoryFormTest(TestCase):

    def test_valid_form(self):
        data = {'name': 'Fungal', 'description': 'Diseases caused by fungi'}
        form = DiseaseCategoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': ''}
        form = DiseaseCategoryForm(data=data)
        self.assertFalse(form.is_valid())

class PlantPartFormTest(TestCase):

    def test_valid_form(self):
        data = {'name': 'Stem'}
        form = PlantPartForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': ''}
        form = PlantPartForm(data=data)
        self.assertFalse(form.is_valid())

class DiseaseFormTest(TestCase):

    def setUp(self):
        self.category = DiseaseCategory.objects.create(name="Fungal", description="Diseases caused by fungi")
        self.stem = PlantPart.objects.create(name="Stem")
        self.root = PlantPart.objects.create(name="Root")

    def test_valid_form(self):
        data = {
            'name': 'Stem Rust',
            'category': self.category.id,
            'description': 'A fungal disease affecting the stem',
            'symptoms': 'Rust colored spots',
            'treatment': 'Fungicides',
            'prevention': 'Crop rotation',
            'affected_parts': [self.stem.id, self.root.id]
        }
        form = DiseaseForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'category': '', 'description': ''}
        form = DiseaseForm(data=data)
        self.assertFalse(form.is_valid())

class PlantImageFormTest(TestCase):
    
    def setUp(self):
        # Create a sample plant object for the test
        self.plant = Plant.objects.create(
            name='Rose', 
            scientific_name='Rosa', 
            description='A beautiful flower', 
            habitat='Garden'
        )
        
        self.form_data = {
            'plant': self.plant.id,
            'description': 'A test image description',
            'is_healthy': True
        }
    
    def test_valid_form(self):
        # Provide a mock file for testing
        # In a real test, you would use an actual file or a `SimpleUploadedFile` object
        with open('path/to/image.jpg', 'rb') as image_file:
            form = PlantImageForm(data=self.form_data, files={'image': image_file})
            self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = PlantImageForm(data={})
        self.assertFalse(form.is_valid())

class EuropeanDiseaseFormTest(TestCase):

    def setUp(self):
        self.category = DiseaseCategory.objects.create(name="Bacterial", description="Diseases caused by bacteria")
        self.leaf = PlantPart.objects.create(name="Leaf")

    def test_valid_form(self):
        data = {
            'name': 'Fire Blight',
            'category': self.category.id,
            'description': 'A bacterial disease affecting leaves',
            'symptoms': 'Brown spots',
            'treatment': 'Antibiotics',
            'prevention': 'Sanitation',
            'affected_parts': [self.leaf.id]
        }
        form = EuropeanDiseaseForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'category': '', 'description': ''}
        form = EuropeanDiseaseForm(data=data)
        self.assertFalse(form.is_valid())

class PlantFormTest(TestCase):

    def test_valid_form(self):
        data = {'name': 'Wheat', 'scientific_name': 'Triticum aestivum', 'description': 'A cereal grain', 'habitat': 'Field'}
        form = PlantForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'scientific_name': '', 'description': '', 'habitat': ''}
        form = PlantForm(data=data)
        self.assertFalse(form.is_valid())

class PlantImageFormTest(TestCase):
    def setUp(self):
        self.plant = Plant.objects.create(name="Rose", scientific_name="Rosa", description="A beautiful flower", habitat="Garden")

    def test_valid_form(self):
     form_data = {
        'plant': self.plant.id,
        'image': 'path/to/image.jpg',
        'description': 'A healthy rose plant image',
        'is_healthy': True
    }
    form = PlantImageForm(data=form_data, files={'image': 'path/to/image.jpg'})
    if not form.is_valid():
        print(form.errors)
    self.assertTrue(form.is_valid())
