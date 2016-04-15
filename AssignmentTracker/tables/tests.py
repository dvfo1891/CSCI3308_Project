from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your tests here.
class MainpageResponseTests(TestCase):
    """
    Test the HttpResponse of the main page.
    """
    def test_notification_link_for_unauthenticated_user(self):
        """
        If the user is unauthenticated, Notification link shouldn't be showed.
        """
        response = self.client.get(reverse('test_main'))
        self.assertNotContains(response, "Notification", status_code=200)

    def test_notification_link_for_authenticated_user(self):
        """
        If the user is login, Notification link should show up.
        """
        User.objects.create_user('unittestuser', 'test@test.com', '12345678')
        login = self.client.login(username='unittestuser', password='12345678')
        self.assertTrue(login)

        response = self.client.get(reverse('test_main'))
        self.assertContains(response, "Notification", status_code=200)

    def test_signup_and_login_link_for_unauthenticated_user(self):
        """
        If the user is unauthenticated, Login and Sign Up link should show up.
        """
        response = self.client.get(reverse('test_main'))
        self.assertContains(response, "Login", status_code=200)
        self.assertContains(response, "Sign up", status_code=200)

    def test_signup_and_login_link_for_authenticated_user(self):
        """
        If the user is authenticated, Login and Sign Up link shouldn't exist.
        """
        User.objects.create_user('unittestuser', 'test@test.com', '12345678')
        login = self.client.login(username='unittestuser', password='12345678')
        self.assertTrue(login)

        response = self.client.get(reverse('test_main'))
        self.assertNotContains(response, "Login", status_code=200)
        self.assertNotContains(response, "Sign up", status_code=200)

class GetAllCoursesTests(TestCase):
    def test_get_all_courses_when_database_is_empty(self):
        pass

    def test_get_all_courses(self):
        pass

class GetEnrolledCoursesTests(TestCase):
    def test_get_enrolled_courses_when_no_course_enrolled(self):
        pass

    def test_get_enrolled_courses(self):
        pass

class GetNotificationsTests(TestCase):
    def test_get_notification_when_no_notification_received(self):
        pass

    def test_get_notification(self):
        pass

class GetAssignmentsTests(TestCase):
    def test_get_assignment_when_no_assignment_posted(self):
        pass

    def test_get_assignment(self):
        pass

class SchedulerTest(TestCase):
    pass

class ParserTest(TestCase):
    pass