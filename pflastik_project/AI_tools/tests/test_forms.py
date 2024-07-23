# tests/test_forms.py

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from ..forms import AIToolForm, AIQuestionForm, AIAnswerForm, AIToolUsageForm

class AIToolFormTests(TestCase):

    def test_valid_ai_tool_form(self):
        form_data = {
            'name': 'Test Tool',
            'description': 'A tool for testing.',
            'usage_instructions': 'Test usage instructions.'
        }
        file_data = {
            'model_file': SimpleUploadedFile("model_file.txt", b"file_content")
        }
        form = AIToolForm(data=form_data, files=file_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_ai_tool_form(self):
        form_data = {
            'name': '',
            'description': 'A tool for testing.',
            'usage_instructions': 'Test usage instructions.'
        }
        file_data = {
            'model_file': SimpleUploadedFile("model_file.txt", b"file_content")
        }
        form = AIToolForm(data=form_data, files=file_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

class AIQuestionFormTests(TestCase):

    def test_valid_ai_question_form(self):
        form_data = {'question': 'What is AI?'}
        form = AIQuestionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_ai_question_form(self):
        form_data = {'question': ''}
        form = AIQuestionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('question', form.errors)

class AIAnswerFormTests(TestCase):

    def test_valid_ai_answer_form(self):
        form_data = {'answer': 'AI stands for Artificial Intelligence.'}
        form = AIAnswerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_ai_answer_form(self):
        form_data = {'answer': ''}
        form = AIAnswerForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('answer', form.errors)

class AIToolUsageFormTests(TestCase):

    def test_valid_ai_tool_usage_form(self):
        form_data = {
            'input_data': 'Sample input data.',
            'result': 'Sample result.'
        }
        form = AIToolUsageForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_ai_tool_usage_form(self):
        form_data = {
            'input_data': '',
            'result': 'Sample result.'
        }
        form = AIToolUsageForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('input_data', form.errors)
