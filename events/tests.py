from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.tests import userProfileTestCase
from .models import Reviews,Event

class eventTestCase(userProfileTestCase):
    # def setUp(self):
    #     # create a new user making a post request to djoser endpoint
    #     self.user=self.client.post('/auth/users/',data={'username':'mario','password':'i-keep-jumping'})
    #     # obtain a json web token for the newly created user
    #     response=self.client.post('/auth/jwt/create/',data={'username':'mario','password':'i-keep-jumping'})
    #     self.token=response.data['access']
    #     self.api_authentication()
        
    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)

    # def test_userprofile_profile(self):
    #     profile_data={'description':'I am a very famous game character','location':'nintendo world','is_creator':'True',}
    #     response=self.client.put(reverse('profile',kwargs={'pk':1}),data=profile_data)
    #     print(response.data)
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_create_event(self):
        event_data={'name':'good life','description':'happy times','location':'kenya',}
        response=self.client.post('http://127.0.0.1:8000/api/events/all-events/',data=event_data)
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    