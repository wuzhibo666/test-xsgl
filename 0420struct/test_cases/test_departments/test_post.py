import requests
import unittest
#设计用例
class TestDepPost(unittest.TestCase):
    def test_depPost1(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type":"application/json"}
        body = r'{"data": [{"dep_id":"北京001","dep_name":"中关村001","master_name":"市长","slogan":"Here is Slogan"}]}'
        res = requests.post(url,data=body.encode('utf-8'),headers=head)
        self.assertEqual(201,res.status_code)
    def test_depPost2(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type":"application/json"}
        body = r'{"data": [{"dep_id":"北京002","dep_name":"Test学院2","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url,data=body.encode('utf-8'),headers=head)
        self.assertEqual(201,res.status_code)
    def test_depPost3(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type":"application/json"}
        body = r'{"data": [{"dep_id":"北京003","dep_name":"Test学院3","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url,data=body.encode('utf-8'),headers=head)
        self.assertEqual(201,res.status_code)

    def test_depPost4(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京004","dep_name":"中关村004","master_name":"市长","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost5(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京005","dep_name":"Test5","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost6(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京006","dep_name":"Test6","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost7(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京007","dep_name":"中关村007","master_name":"市长","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost8(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京008","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost9(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京009","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost10(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京010","dep_name":"中关村001","master_name":"市长","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost11(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京011","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost12(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京012","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost13(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京013","dep_name":"中关村001","master_name":"市长","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost14(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京014","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)

    def test_depPost15(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        head = {"Content-Type": "application/json"}
        body = r'{"data": [{"dep_id":"北京015","dep_name":"Test学院","master_name":"Test-Master","slogan":"Here is Slogan"}]}'
        res = requests.post(url, data=body.encode('utf-8'), headers=head)
        self.assertEqual(201, res.status_code)



