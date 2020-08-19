import requests
import unittest
import time
import HTMLTestReportCN
suite = unittest.TestSuite()
load = unittest.defaultTestLoader
testcases=load.discover('test_cases',pattern='test*',top_level_dir=None)
suite.addTests(testcases)
#timestr = time.strftime('%Y%m%d-%H%M%S')
st=open('reports/reporter.html','wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=st,title='学院测试报告',
                                         description='测试新增查询功能',
                                         tester='吴')
runner.run(suite)















