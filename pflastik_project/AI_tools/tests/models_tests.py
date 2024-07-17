from django.test import TestCase
from django.contrib.auth.models import User
from AI_tools.models import Conversation, AITool, AIQuestion, AIAnswer, AIToolUsage

class ModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create some instances of your models
        self.conversation = Conversation.objects.create(user=self.user, llm_name='Test LLM')
        self.ai_tool = AITool.objects.create(name='Test Tool', description='Test description', usage_instructions='Test instructions')
        self.ai_question = AIQuestion.objects.create(user=self.user, question='Test question')
        self.ai_answer = AIAnswer.objects.create(question=self.ai_question, answer='Test answer')
        self.ai_tool_usage = AIToolUsage.objects.create(tool=self.ai_tool, user=self.user, input_data='Test data', result='Test result')

    def test_conversation_model(self):
        # Retrieve the conversation instance created in setUp
        conversation = Conversation.objects.get(user=self.user)

        # Test the __str__ method
        self.assertEqual(str(conversation), f'Conversation id={conversation.id} with Test LLM initiated by testuser')

    def test_ai_tool_model(self):
        # Retrieve the AI tool instance created in setUp
        ai_tool = AITool.objects.get(name='Test Tool')

        # Test the __str__ method
        self.assertEqual(str(ai_tool), 'Test Tool')

    def test_ai_question_model(self):
        # Retrieve the AI question instance created in setUp
        ai_question = AIQuestion.objects.get(user=self.user)

        # Test the __str__ method
        expected_str = f"Question by testuser on {ai_question.created_at}"
        self.assertEqual(str(ai_question), expected_str)

    def test_ai_answer_model(self):
        # Retrieve the AI answer instance created in setUp
        ai_answer = AIAnswer.objects.get(question=self.ai_question)

        # Test the __str__ method
        expected_str = f"Answer to {self.ai_question}"
        self.assertEqual(str(ai_answer), expected_str)

    def test_ai_tool_usage_model(self):
        # Retrieve the AI tool usage instance created in setUp
        ai_tool_usage = AIToolUsage.objects.get(user=self.user)

        # Test the __str__ method
        expected_str = f"Usage of Test Tool by testuser on {ai_tool_usage.usage_date}"
        self.assertEqual(str(ai_tool_usage), expected_str)
