from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(title="Test Task", description="A test task.")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "A test task.")

    def test_task_update(self):
        task = Task.objects.create(title="Test Task", description="A test task.")
        task.title = "Updated Task"
        task.save()
        self.assertEqual(task.title, "Updated Task")

    def test_task_deletion(self):
        task = Task.objects.create(title="Test Task", description="A test task.")
        task.delete()
        self.assertEqual(Task.objects.count(), 0)

    def test_task_list(self):
        Task.objects.create(title='Test Task')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
