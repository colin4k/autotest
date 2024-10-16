import unittest
import requests

class TestOpenApi(unittest.TestCase):

    def test_get2(self):
        url = 'http://172.16.70.107:7700/mock/default/openApi/get2'
        params = {
            'id': 'example_id',
            'name': '12',
            'aLong': 0,
            'localDate': '2023-10-05',
            'localDateTime': '2023-10-05 12:34:56',
            'localTime': '12:34:56'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        response = requests.post(url, data=params, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json())

if __name__ == '__main__':
    unittest.main()