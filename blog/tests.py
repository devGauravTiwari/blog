from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.
class SimpleDbTest(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create(
			username = 'test',
			email = 'test@test.com',
			password = 'secret')
		self.post = Post.objects.create(
			title = "sample post",
			author = self.user,
			body = 'sample body')
	def test_string_representation(self):
		post = Post(title= 'sample post')
		self.assertEqual(str(post),post.title)
	def test_post_contents(self):
		self.assertEqual(f'{self.post.title}', "sample post")
		self.assertEqual(f'{self.post.author}', 'test')
		self.assertEqual(f'{self.post.body}', 'sample body')
	def test_list_view(self):
		resp = self.client.get(reverse('posts'))
		self.assertEqual(resp.status_code,200)
		self.assertTemplateUsed(resp,'blog/list.html')
		self.assertContains(resp,'sample body')
	def test_detail_view(self):
		resp = self.client.get('post/1/')
		no_resp = self.client.get('post/200/')
		self.assertEqual(resp.status_code,200)
		self.assertEqual(no_resp.status_code,404)
		self.assertTemplateUsed(resp,'blog/detail.html')
		self.assertContains(resp,'sample post')

