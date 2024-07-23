from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Conversation, AITool, AIQuestion, AIAnswer, AIToolUsage

class ConversationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_conversation_creation(self):
        conversation = Conversation.objects.create(
            user=self.user,
            llm_name='Test LLM',
            user_messages=["Hello, how are you?"],
            llm_responses=["I'm good, thank you!"]
        )
        self.assertEqual(conversation.user.username, 'testuser')
        self.assertEqual(conversation.llm_name, 'Test LLM')
        self.assertEqual(conversation.user_messages, ["Hello, how are you?"])
        self.assertEqual(conversation.llm_responses, ["I'm good, thank you!"])

    def test_conversation_string_representation(self):
        conversation = Conversation.objects.create(
            user=self.user,
            llm_name='Test LLM',
            user_messages=["Hello, how are you?"],
            llm_responses=["I'm good, thank you!"]
        )
        self.assertEqual(str(conversation), f'Conversation id={conversation.id} with Test LLM initiated by testuser')

    def test_conversation_ordering(self):
        older_conversation = Conversation.objects.create(
            user=self.user,
            llm_name='Older LLM',
            user_messages=["Hello!"],
            llm_responses=["Hi!"]
        )
        newer_conversation = Conversation.objects.create(
            user=self.user,
            llm_name='Newer LLM',
            user_messages=["Hello again!"],
            llm_responses=["Hi again!"]
        )
        conversations = Conversation.objects.all()
        self.assertEqual(conversations[0], newer_conversation)
        self.assertEqual(conversations[1], older_conversation)

class AIToolModelTest(TestCase):

    def test_aitool_creation(self):
        aitool = AITool.objects.create(
            name='Test Tool',
            description='This is a test tool.',
            model_file='test_model_file',
            usage_instructions='Use this tool for testing.'
        )
        self.assertEqual(aitool.name, 'Test Tool')
        self.assertEqual(aitool.description, 'This is a test tool.')
        self.assertEqual(aitool.model_file, 'test_model_file')
        self.assertEqual(aitool.usage_instructions, 'Use this tool for testing.')

    def test_aitool_string_representation(self):
        aitool = AITool.objects.create(
            name='Test Tool',
            description='This is a test tool.',
            model_file='test_model_file',
            usage_instructions='Use this tool for testing.'
        )
        self.assertEqual(str(aitool), 'Test Tool')

class AIQuestionModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_aiquestion_creation(self):
        question = AIQuestion.objects.create(
            user=self.user,
            question='What is AI?'
        )
        self.assertEqual(question.user.username, 'testuser')
        self.assertEqual(question.question, 'What is AI?')

    def test_aiquestion_string_representation(self):
        question = AIQuestion.objects.create(
            user=self.user,
            question='What is AI?'
        )
        self.assertEqual(str(question), f'Question by {self.user.username} on {question.created_at}')

class AIAnswerModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.question = AIQuestion.objects.create(user=self.user, question='What is AI?')

    def test_aianswer_creation(self):
        answer = AIAnswer.objects.create(
            question=self.question,
            answer='AI stands for Artificial Intelligence.'
        )
        self.assertEqual(answer.question.question, 'What is AI?')
        self.assertEqual(answer.answer, 'AI stands for Artificial Intelligence.')

    def test_aianswer_string_representation(self):
        answer = AIAnswer.objects.create(
            question=self.question,
            answer='AI stands for Artificial Intelligence.'
        )
        self.assertEqual(str(answer), f'Answer to {self.question}')

class AIToolUsageModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.tool = AITool.objects.create(
            name='Test Tool',
            description='This is a test tool.',
            model_file='test_model_file',
            usage_instructions='Use this tool for testing.'
        )

    def test_aitoolusage_creation(self):
        usage = AIToolUsage.objects.create(
            tool=self.tool,
            user=self.user,
            input_data='Test input',
            result='Test result'
        )
        self.assertEqual(usage.tool.name, 'Test Tool')
        self.assertEqual(usage.user.username, 'testuser')
        self.assertEqual(usage.input_data, 'Test input')
        self.assertEqual(usage.result, 'Test result')

    def test_aitoolusage_string_representation(self):
        usage = AIToolUsage.objects.create(
            tool=self.tool,
            user=self.user,
            input_data='Test input',
            result='Test result'
        )
        self.assertEqual(str(usage), f'Usage of {self.tool.name} by {self.user.username} on {usage.usage_date}')
