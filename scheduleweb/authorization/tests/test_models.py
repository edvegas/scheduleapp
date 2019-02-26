from django.test import TestCase

from django.contrib.auth.models import User
from authorization.models import Profile


class ProfileModelTest(TestCase):
  
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username='vedevas',
                                    password='SuperPassword777',
                                    first_name='Billy',
                                    last_name='Bong',
                                    email='billybong@gmail.com')
        profile1 = Profile.objects.update(user=user1,
                                          phone='+79005553535',
                                          team='team4')

    def test_phone_max_length(self):
        profile=Profile.objects.get(id=1)
        max_length = profile._meta.get_field('phone').max_length
        self.assertEquals(max_length, 15)

    def test_team_max_length(self):
        profile=Profile.objects.get(id=1)
        max_length = profile._meta.get_field('team').max_length
        self.assertEquals(max_length, 30)
