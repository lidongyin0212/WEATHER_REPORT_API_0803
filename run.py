import unittest
from BSTestRunner import BSTestRunner
# from HtmlTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner
import time

# 指定测试用例 & 测试报告的存放路径
testcase_dir = './test_case'
report_dir = './reports'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='weather_api_unittest.py')

# 定义测试报告的文件格式
now = time.strftime("%y-%m-%d %H_%M_%S")    # 对时间格式化
report_name = report_dir+'/'+now+'_test_report.html'    # 报告的名称规则

# 运行测试用例，并生成测试报告
def run_test():
    with open(report_name,'wb') as f:
        runner = HTMLTestRunner(stream=f,title="天气接口测试报告",description="中国城市天气测试报告",tester='暂无')
        # runner = BSTestRunner(stream=f, title="天气接口测试报告", description="中国城市天气测试报告")
        runner.run(discover)
run_test()