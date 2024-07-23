from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Conversation, AITool, AIQuestion, AIAnswer, AIToolUsage

class APIViewsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.conversation = Conversation.objects.create(
            user=self.user,
            llm_name='Test LLM',
            user_messages=['Hello'],
            llm_responses=['Hi'],
            context={}
        )

        self.ai_tool = AITool.objects.create(
            name='Test Tool',
            description='Description for the test tool.',
            model_file='path/to/model/file',
            usage_instructions='How to use the test tool.'
        )

        self.ai_question = AIQuestion.objects.create(
            user=self.user,
            question='What is the test question?'
        )

        self.ai_answer = AIAnswer.objects.create(
            question=self.ai_question,
            answer='This is the answer to the test question.'
        )

        self.ai_tool_usage = AIToolUsage.objects.create(
            tool=self.ai_tool,
            user=self.user,
            input_data='Test input data',
            result='Test result'
        )

    def test_get_conversations(self):
        url = reverse('conversation-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['llm_name'], 'Test LLM')

    def test_create_conversation(self):
        url = reverse('conversation-list')
        data = {
            'user': self.user.id,
            'llm_name': 'New LLM',
            'user_messages': ['New message'],
            'llm_responses': ['New response'],
            'context': {}
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversation.objects.count(), 2)
        self.assertEqual(Conversation.objects.get(id=response.data['id']).llm_name, 'New LLM')

    def test_update_conversation(self):
        url = reverse('conversation-detail', kwargs={'pk': self.conversation.pk})
        data = {
            'llm_name': 'Updated LLM',
            'user_messages': ['Updated message'],
            'llm_responses': ['Updated response'],
            'context': {}
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Conversation.objects.get(id=self.conversation.id).llm_name, 'Updated LLM')

    def test_delete_conversation(self):
        url = reverse('conversation-detail', kwargs={'pk': self.conversation.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Conversation.objects.count(), 0)

    def test_get_ai_tools(self):
        url = reverse('ai-tool-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Tool')

    def test_create_ai_tool(self):
        url = reverse('ai-tool-list')
        data = {
            'name': 'New Tool',
            'description': 'Description for the new tool.',
            'model_file': 'path/to/new/model/file',
            'usage_instructions': 'How to use the new tool.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AITool.objects.count(), 2)
        self.assertEqual(AITool.objects.get(id=response.data['id']).name, 'New Tool')

    def test_update_ai_tool(self):
        url = reverse('ai-tool-detail', kwargs={'pk': self.ai_tool.pk})
        data = {
            'name': 'Updated Tool',
            'description': 'Updated description.',
            'model_file': 'path/to/updated/model/file',
            'usage_instructions': 'Updated usage instructions.'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AITool.objects.get(id=self.ai_tool.id).name, 'Updated Tool')

    def test_delete_ai_tool(self):
        url = reverse('ai-tool-detail', kwargs={'pk': self.ai_tool.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AITool.objects.count(), 0)

    def test_get_ai_questions(self):
        url = reverse('ai-question-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], 'What is the test question?')

    def test_create_ai_question(self):
        url = reverse('ai-question-list')
        data = {
            'user': self.user.id,
            'question': 'New test question?'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AIQuestion.objects.count(), 2)
        self.assertEqual(AIQuestion.objects.get(id=response.data['id']).question, 'New test question?')

    def test_update_ai_question(self):
        url = reverse('ai-question-detail', kwargs={'pk': self.ai_question.pk})
        data = {
            'question': 'Updated question?'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AIQuestion.objects.get(id=self.ai_question.id).question, 'Updated question?')

    def test_delete_ai_question(self):
        url = reverse('ai-question-detail', kwargs={'pk': self.ai_question.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AIQuestion.objects.count(), 0)

    def test_get_ai_answers(self):
        url = reverse('ai-answer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['answer'], 'This is the answer to the test question.')

    def test_create_ai_answer(self):
        url = reverse('ai-answer-list')
        data = {
            'question': self.ai_question.id,
            'answer': 'New answer to the question.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AIAnswer.objects.count(), 2)
        self.assertEqual(AIAnswer.objects.get(id=response.data['id']).answer, 'New answer to the question.')

    def test_update_ai_answer(self):
        url = reverse('ai-answer-detail', kwargs={'pk': self.ai_answer.pk})
        data = {
            'answer': 'Updated answer to the question.'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AIAnswer.objects.get(id=self.ai_answer.id).answer, 'Updated answer to the question.')

    def test_delete_ai_answer(self):
        url = reverse('ai-answer-detail', kwargs={'pk': self.ai_answer.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AIAnswer.objects.count(), 0)

    def test_get_ai_tool_usages(self):
        url = reverse('ai-tool-usage-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['input_data'], 'Test input data')

    def test_create_ai_tool_usage(self):
        url = reverse('ai-tool-usage-list')
        data = {
            'tool': self.ai_tool.id,
            'user': self.user.id,
            'input_data': 'New input data',
            'result': 'New result'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AIToolUsage.objects.count(), 2)
        self.assertEqual(AIToolUsage.objects.get(id=response.data['id']).input_data, 'New input data')

    def test_update_ai_tool_usage(self):
        url = reverse('ai-tool-usage-detail', kwargs={'pk': self.ai_tool_usage.pk})
        data = {
            'input_data': 'Updated input data',
            'result': 'Updated result'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AIToolUsage.objects.get(id=self.ai_tool_usage.id).input_data, 'Updated input data')

    def test_delete_ai_tool_usage(self):
        url = reverse('ai-tool-usage-detail', kwargs={'pk': self.ai_tool_usage.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AIToolUsage.objects.count(), 0)
