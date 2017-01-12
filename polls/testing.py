# from django.test import TestCase
# from django.utils import timezone
# import datetime
# 
# from .models import Question, Choice
# 
# from unittest.mock import Mock, call, patch
# import polls
# 
# 
# class QuestionMethodTests(TestCase):
# 
# #     def test_mock(self):
# # 
# #         fooSource = Mock(spec=Question)
# # 
# #         choice_example = Choice()
# # 
# #         testSource = fooSource()
# # 
# #         choice_example.example(testSource)
# # 
# #         testCalls = [call()]
# # 
# #         #fooSource.assert_any_call()
# #         fooSource.assert_has_calls(testCalls)
# 
# #     def test_mock_more(self):
# # 
# #         mockSource = Mock(spec=Choice)
# #         testMock = mockSource()
# #         result = testMock.example()
# # 
# #         testCalls = [call.example()]
# #         print(result, "<><>", testCalls)
# #         test_calls2 = [call()]
# #         testMock.assert_has_calls(testCalls)
# 
#     
#     @patch('polls.models.Question')
#     def test_was_published_recently_with_future_question(self, QuestionMock):
# 
#         """
#         was_published_recently() should return False for questions whose pub_date is in the future.
#         """
#         
#         
#         future_time = timezone.now() + datetime.timedelta(days=30)
# 
#         
# 
#         future_question = QuestionMock(pub_date=future_time)
#         future_mock = future_question()
#         #assert future_question.was_published_recently() is polls.models.Question.was_published_recently()
#         #print(">>>>>>>>>>> ",QuestionMock.called)
#         self.assertIs(future_mock.was_published_recently(), False)
#          
#          
#         #print (question_mock.was_published_recently())
#          
#         #assert question_mock == Question(pub_date=time)
#         #future_question = Question(pub_date=time)
#         #self.assertIs(future_question.was_published_recently(), False)




# import datetime
# from django.utils import timezone
# from django.test import TestCase
# from django.urls import reverse
# 
# from .models import Question, Warehouse, Order
# 
# #from unittest.mock import patch
# from unittest.mock import Mock, call
# 
# class QuestionMethodTests(TestCase):
#     
#     def test_was_published_recently_with_future_question(self):
#  
# #         """
# #         was_published_recently() should return False for questions whose pub_date is in the future.
# #         """
# 
#         
#         #print question_mock.was_published_recently()
#         
#         #assert question_mock == Question(pub_date=time)
#         #future_question = Question(pub_date=time)
#         #self.assertIs(future_question.was_published_recently(), False)
#     
# 
# #     def test_was_published_recently_with_future_question(self):
# #         """
# #         was_published_recently() should return False for questions whose pub_date is in the future.
# #         """
# #         time = timezone.now() + datetime.timedelta(days=30)
# #         future_question = Question(pub_date=time)
# #         self.assertIs(future_question.was_published_recently(), False)
#     
# #     def test_was_published_recently_with_old_question(self):
# #         """
# #         was_published_recently() should return False for questions whose pub_date is older than 1 day.
# #         """
# #         time = timezone.now() - datetime.timedelta(days=30)
# #         old_question = Question(pub_date=time)
# #         self.assertIs(old_question.was_published_recently(), False)
# #         
# #     def test_was_published_recently_with_recent_question(self):
# #         """
# #         was_published_recently() should return True for questions whose pub_date is within the last day.
# #         """
# #         time = timezone.now() - datetime.timedelta(hours=1)
# #         recent_question = Question(pub_date=time)
# #         self.assertIs(recent_question.was_published_recently(), True)
# # 
# # 
# # def create_question(question_text, days):
# #     """
# #     Creates a question with the given `question_text` and published the
# #     given number of `days` offset to now (negative for questions published
# #     in the past, positive for questions that have yet to be published).
# #     """
# #     time = timezone.now() + datetime.timedelta(days=days)
# #     return Question.objects.create(question_text=question_text, pub_date=time)
# # 
# # class QuestionViewTests(TestCase):
# #     def test_index_view_with_no_questions(self):
# #         """
# #         If no questions exist, an appropriate message should be displayed.
# #         """
# #         response = self.client.get(reverse('polls:index'))
# #         self.assertEqual(response.status_code, 200)
# #         self.assertContains(response, "No polls are available.")
# #         self.assertQuerysetEqual(response.context['latest_question_list'], [])
# # 
# #     def test_index_view_with_a_past_question(self):
# #         """
# #         Questions with a pub_date in the past should be displayed on the index page.
# #         """
# #         create_question(question_text="Past question.", days=-30)
# #         response = self.client.get(reverse('polls:index')) 
# #         self.assertQuerysetEqual(
# #             response.context['latest_question_list'],
# #         ['<Question: Past question.>']
# #     )
# #         
# #     def test_index_view_with_a_future_question(self):
# #         """
# #         Questions with a pub_date in the future should not be displayed on
# #         the index page.
# #         """
# #         create_question(question_text="Future question.", days=30)
# #         response = self.client.get(reverse('polls:index')) 
# #         self.assertContains(response, "No polls are available.") 
# #         self.assertQuerysetEqual(response.context['latest_question_list'], [])
# #     
# #     def test_index_view_with_future_question_and_past_question(self):
# #         """
# #         Even if both past and future questions exist, only past questions should be displayed.
# #         """
# #         create_question(question_text="Past question.", days=-30)
# #         create_question(question_text="Future question.", days=30)
# #         response = self.client.get(reverse('polls:index'))
# #         self.assertQuerysetEqual(
# #             response.context['latest_question_list'],
# #             ['<Question: Past question.>']
# #         )
# #         
# #     def test_index_view_with_two_past_questions(self):
# #         """
# #         The questions index page may display multiple questions.
# #         """
# #         create_question(question_text="Past question 1.", days=-30)
# #         create_question(question_text="Past question 2.", days=-5)
# #         response = self.client.get(reverse('polls:index'))
# #         self.assertQuerysetEqual(
# #             response.context['latest_question_list'],
# #             ['<Question: Past question 2.>', '<Question: Past question 1.>']
# #         )
# # 
# # 
# # class QuestionIndexDetailTests(TestCase):
# #     def test_detail_view_with_a_future_question(self):
# #         """
# #         The detail view of a question with a pub_date in the future should
# #         return a 404 not found.
# #         """
# #         future_question = create_question(question_text='Future question.', days=5)
# #         url = reverse('polls:detail', args=(future_question.id,))
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 404)
# # 
# #     def test_detail_view_with_a_past_question(self):
# #         """
# #         The detail view of a question with a pub_date in the past should
# #         display the question's text.
# #         """
# #         past_question = create_question(question_text='Past Question.', days=-5) 
# #         url = reverse('polls:detail', args=(past_question.id,))
# #         response = self.client.get(url) 
# #         self.assertContains(response, past_question.question_text)
# 
# 
# class OrderTest(TestCase):
#     #declare the test resource
#     fooSource = None
#     
#     #preparing to test
#     def setUp(self):
#         """ Setting up for the test """
#         
#         #print "OrderTest:setUp_:begin"
#         
#         # identify the test routine
#         testName = self.id().split(".")
#         testName = testName[2]
#         #print testName
#         
#         # prepare and configure the test resource
#         if (testName == "testA_newOrder"):
#             pass
#             #print "OrderTest:setup_:testA_newOrder:RESERVED"
#         elif (testName == "testB_nilInventory"):
#             self.fooSource = Mock(spec = Warehouse, return_value = None)
#         elif (testName == "testC_orderCheck"):
#             self.fooSource = Mock(spec = Warehouse)
#             self.fooSource.hasInventory.return_value = True
#             self.fooSource.getInventory.return_value = 0
#         elif (testName == "testD_orderFilled"):
#             self.fooSource = Mock(spec = Warehouse)
#             self.fooSource.hasInventory.return_value = True
#             self.fooSource.getInventory.return_value = 10
#         elif (testName == "testE_orderIncomplete"):
#             self.fooSource = Mock(spec = Warehouse)
#             self.fooSource.hasInventory.return_value = True
#             self.fooSource.getInventory.return_value = 5
#         else:
#             self.fooSource = Mock(spec = Warehouse, return_value = None)
#     
#     # ending the test
#     def tearDown(self):
#         """Cleaning up after the test"""
#         #print "OrderTest:tearDown_:begin"
#         #print ""
#         pass
#     
# #     # test: new order
# #     # objective: creating an order
# #     def testA_newOrder(self):
# #         # creating a new order
# #         testOrder = Order("mushrooms", 10)
# #         #print repr(testOrder)
# #         
# #         # test for a nil object
# #         self.assertIsNotNone(testOrder, "Order object is a nil.")
# #         
# #         # test for a valid item name
# #         testName = testOrder._orderItem
# #         self.assertEqual(testName, "mushrooms", "Invalid item name")
# #         
# #         # test for a valid item amount
# #         testAmount = testOrder._orderAmount
# #         self.assertGreater(testAmount, 0, "Invalid item amount")
#     
#     # test: nil inventory
#     # objective: how the order object handles a nil inventory
#     def testB_nilInventory(self):
#         """Test routine B"""
#         # creating a new order
#         testOrder = Order("mushrooms", 10)
#         #print repr(testOrder)
#         
#         # fill the order
#         testSource = self.fooSource()
#         testOrder.fill(testSource)
#         
#         # print the mocked calls
#         #print self.fooSource.mock_calls
#         
#         # check the call history
#         testCalls = [call()]
#         self.fooSource.assert_has_calls(testCalls)