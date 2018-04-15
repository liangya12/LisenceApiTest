#  _*_ coding:utf-8 _*_
import json
import unittest

import HTMLTestRunner

from tools.HttpRunner import HttpRunner
from tools.Operate_Dir_jsons_data import OperatingFiles_json
from tools.assert_helper import Assert_helper


class Create_lisence_files_test(unittest.TestCase):

    def setUp(self):
        print "创建license接口测试执行开始"
        self.url='http://47.92.88.246:8999/it-license/it/license/create'
        self.data=OperatingFiles_json().get_json_files_data("..\\TestData")
    def test_create_lisence_files(self):
        license_list=[]
        try:
            for item in self.data.values():
                self.response=HttpRunner(self.url,'POST',item).post_data()
                print self.response
                license_list.append(self.response['result'])
                self.version=json.loads(item)["productLicensePojo"]["productVersion"]
                self.res=Assert_helper().query_helper('216',self.version)
            #判断生成的license是否可以查询到  在该客户对应版本号数据里
                self.assertTrue(self.response['result'] in str(self.res))
            # self.assertEqual(self.response["errCode"], 0)
            # self.assertEqual(self.response['errMessage'], 'success')
            # self.assertTrue(self.response['result'])
         #清理测试数据 即生成的该客户下的licenseId
        finally:
            print license_list
            Assert_helper().del_helper('216',license_list)



    def tearDown(self):
        print "创建license接口测试执行结束"

if __name__ == '__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(Create_lisence_files_test('test_create_lisence_files'))
    fp=open("..\\Report\\my_report.html",'wb')
    runner1=HTMLTestRunner.HTMLTestRunner(fp,title=u'测试报告',description='This is a create_test_report')
    runner1.run(suite)
    # discover=unittest.defaultTestLoader.discover('..\\TestCase',pattern='*_test.py')
    # for item in discover:
    #     print item
    # fp=open("..\\Report\\my_report.html",'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(fp,title=u'测试报告',description='This is a create_test_report')
    # runner.run(discover)

