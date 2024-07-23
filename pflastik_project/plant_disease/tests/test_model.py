from django.test import TestCase
from ..models import DiseaseCategory, PlantPart, Disease, DiseaseImage, EuropeanDisease, Plant, PlantImage

class DiseaseCategoryTest(TestCase):

    def setUp(self):
        DiseaseCategory.objects.create(name="Fungal", description="Diseases caused by fungi")
        DiseaseCategory.objects.create(name="Bacterial", description="Diseases caused by bacteria")

    def test_disease_category_creation(self):
        fungal = DiseaseCategory.objects.get(name="Fungal")
        bacterial = DiseaseCategory.objects.get(name="Bacterial")
        self.assertEqual(fungal.name, "Fungal")
        self.assertEqual(bacterial.description, "Diseases caused by bacteria")

class PlantPartTest(TestCase):

    def setUp(self):
        PlantPart.objects.create(name="Stem")
        PlantPart.objects.create(name="Root")

    def test_plant_part_creation(self):
        stem = PlantPart.objects.get(name="Stem")
        root = PlantPart.objects.get(name="Root")
        self.assertEqual(stem.name, "Stem")
        self.assertEqual(root.name, "Root")

class DiseaseTest(TestCase):

    def setUp(self):
        fungal = DiseaseCategory.objects.create(name="Fungal", description="Diseases caused by fungi")
        stem = PlantPart.objects.create(name="Stem")
        root = PlantPart.objects.create(name="Root")
        disease = Disease.objects.create(
            name="Stem Rust",
            category=fungal,
            description="A fungal disease affecting the stem",
            symptoms="Rust colored spots",
            treatment="Fungicides",
            prevention="Crop rotation"
        )
        disease.affected_parts.set([stem, root])

    def test_disease_creation(self):
        disease = Disease.objects.get(name="Stem Rust")
        self.assertEqual(disease.name, "Stem Rust")
        self.assertEqual(disease.category.name, "Fungal")
        self.assertIn("Stem", [part.name for part in disease.affected_parts.all()])

class DiseaseImageTest(TestCase):

    def setUp(self):
        fungal = DiseaseCategory.objects.create(name="Fungal", description="Diseases caused by fungi")
        disease = Disease.objects.create(
            name="Stem Rust",
            category=fungal,
            description="A fungal disease affecting the stem",
            symptoms="Rust colored spots",
            treatment="Fungicides",
            prevention="Crop rotation"
        )
        DiseaseImage.objects.create(disease=disease, image="path/to/image.jpg", description="Rust spots on stem")

    def test_disease_image_creation(self):
        image = DiseaseImage.objects.get(description="Rust spots on stem")
        self.assertEqual(image.disease.name, "Stem Rust")
        self.assertEqual(image.image, "path/to/image.jpg")

class EuropeanDiseaseTest(TestCase):

    def setUp(self):
        bacterial = DiseaseCategory.objects.create(name="Bacterial", description="Diseases caused by bacteria")
        leaf = PlantPart.objects.create(name="Leaf")
        disease = EuropeanDisease.objects.create(
            name="Fire Blight",
            category=bacterial,
            description="A bacterial disease affecting leaves",
            symptoms="Brown spots",
            treatment="Antibiotics",
            prevention="Sanitation"
        )
        disease.affected_parts.set([leaf])

    def test_european_disease_creation(self):
        disease = EuropeanDisease.objects.get(name="Fire Blight")
        self.assertEqual(disease.name, "Fire Blight")
        self.assertEqual(disease.category.name, "Bacterial")
        self.assertIn("Leaf", [part.name for part in disease.affected_parts.all()])

class PlantTest(TestCase):

    def setUp(self):
        Plant.objects.create(name="Wheat", scientific_name="Triticum aestivum", description="A cereal grain", habitat="Field")

    def test_plant_creation(self):
        plant = Plant.objects.get(name="Wheat")
        self.assertEqual(plant.scientific_name, "Triticum aestivum")
        self.assertEqual(plant.habitat, "Field")

class PlantImageTest(TestCase):

    def setUp(self):
        plant = Plant.objects.create(name="Wheat", scientific_name="Triticum aestivum", description="A cereal grain", habitat="Field")
        PlantImage.objects.create(plant=plant, image="path/to/healthy_image.jpg", description="Healthy wheat plant", is_healthy=True)
        PlantImage.objects.create(plant=plant, image="path/to/diseased_image.jpg", description="Diseased wheat plant", is_healthy=False)

    def test_plant_image_creation(self):
        healthy_image = PlantImage.objects.get(description="Healthy wheat plant")
        diseased_image = PlantImage.objects.get(description="Diseased wheat plant")
        self.assertTrue(healthy_image.is_healthy)
        self.assertFalse(diseased_image.is_healthy)
