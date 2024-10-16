import unittest
import requests

class TestOpenApi(unittest.TestCase):
    def test_get2(self):
        url = "http://172.16.70.107:7700/default/openApi/get2"
        params = {
            "header": {
                "requestId": "string",
                "errorCode": "string",
                "errorMsg": "string"
            },
            "id": "string",
            "name": "12",
            "aLong": 0,
            "localDate": "yyyy-MM-dd",
            "localDateTime": "yyyy-MM-dd HH:mm:ss",
            "localTime": "HH:mm:ss"
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }
        response = requests.post(url, data=params, headers=headers)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn("data", response_json)
        self.assertIn("header", response_json["data"])
        self.assertIn("id", response_json["data"])
        self.assertIn("name", response_json["data"])
        self.assertIn("aLong", response_json["data"])
        self.assertIn("localDate", response_json["data"])
        self.assertIn("localDateTime", response_json["data"])
        self.assertIn("localTime", response_json["data"])

if __name__ == '__main__':
    unittest.main()