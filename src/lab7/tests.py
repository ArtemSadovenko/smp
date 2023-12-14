import unittest
from UserService import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()

    def tearDown(self):
        self.user_service = None

    def test_returnDetailList(self):
        # Arrange
        post_details = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
        expected_output = 'userId: 1id: 1title: sunt aut facere repellat provident occaecati excepturi optio reprehenderitbody: quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
        
        # Act
        result = self.user_service.returnDetailList(post_details)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_returnDetailTable(self):
        # Arrange
        post_details = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
        expected_output = '+--------+----------------------------------------------------------------------------+\n| Field  |                                   Value                                    |\n+--------+----------------------------------------------------------------------------+\n| userId |                                     1                                      |\n|   id   |                                     1                                      |\n| title  | sunt aut facere repellat provident occaecati excepturi optio reprehenderit |\n|  body  |                              quia et suscipit                              |\n|        |              suscipit recusandae consequuntur expedita et cum              |\n|        |                  reprehenderit molestiae ut ut quas totam                  |\n|        |            nostrum rerum est autem sunt rem eveniet architecto             |\n+--------+----------------------------------------------------------------------------+'
        
        # Act
        result = self.user_service.returnDetailTable(post_details)
        
        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
