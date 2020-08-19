import requests
import unittest
#设计用例
class TestDepQueryALL(unittest.TestCase):
    def test_depQuery_all1(self):
        url = r'http://127.0.0.1:8000/api/departments/ghi/classes/'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)
    def test_depQuery_all2(self):
        url = r'http://127.0.0.1:8000/api/departments/ghi/classes/3/'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)
    def test_depQuery_all3(self):
        url = r'http://127.0.0.1:8000/api/departments/ghi/classes/?cls_id_list=A001,A002,A003'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)
    def test_depQuery_all4(self):
        url = r'http://127.0.0.1:8000/api/departments/ghi/classes/?$cls_id_list=3,4&$master_name_list=张3,张4'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)
    def test_depQuery_all5(self):
        url = r'http://127.0.0.1:8000/api/departments/ghi/classes/?cls_name=c++'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)
    def test_depQuery_all6(self):
        url = r'http://127.0.0.1:8000/api/departments/A班3/classes/?cls_name=前端80&master_name=张&slogan=1'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)
    def test_depQuery_all7(self):
        url = r'http://127.0.0.1:8000/api/departments/ghi/classes/?blur=1&cls_name=c'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)
    def test_depQuery_all8(self):
        url = r'http://127.0.0.1:8000/api/departments/ghi/classes/?blur=1&cls_name=c&master_name=张'
        res = requests.get(url)
        self.assertEqual(200,res.status_code)



