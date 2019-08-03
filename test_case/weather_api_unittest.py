import unittest
import requests
from time import sleep

# 构造WeatherTest类，继承unittest.TestCase
class WeatherTest(unittest.TestCase):
    # def __init__(self,case_name):
    #     self.case_name = case_name
    u'''天气接口用例测试'''
    def setUp(self):

        self.url = 'http://t.weather.sojson.com/api/weather/city'
        # self.case_name = case_name
    # 定义测试guangzhou天气的方法
    def test_weather_guangzhou(self):   # 用例方法需要以test开头，便于执行顺利
        # print("打印成功")
        u'''
        Case01-正常存在的city_code值
        '''
        self.case_name = '获取成功'
        data = {'city_code':'101280101'}
        r = requests.get(self.url+'/'+data['city_code'])    # 拼接接口URL
        result = r.json()

        # 设置断言
        self.assertEqual(result['status'],200)  # 状态码的值是数字，非字符串
        self.assertEqual(result['message'],'success感谢又拍云(upyun.com)提供CDN赞助')
        self.assertEqual(result['cityInfo']['city'],'广州市')
        self.assertEqual(result['cityInfo']['citykey'],'101280101')
        sleep(3)
        return self.case_name

    def test_weather_param_error(self):
        u'''
        Case02-错误的city_code值
        '''
        self.case_name = '参数错误'
        data = {'city_code':'666abc'}
        r = requests.get(self.url+'/'+data['city_code'])
        result = r.json()

        self.assertEqual(result['message'],'Request resource not found.')
        self.assertEqual(result['status'],404)
        sleep(3)

    def test_weather_param_non_existent(self):
        u'''
        Case03-不存在的city_code值
        '''
        self.case_name = '参数未定义'
        data = {'city_code':'123456789'}
        r = requests.get(self.url+'/'+data['city_code'])
        result = r.json()

        self.assertEqual(result['message'],'获取失败')
        self.assertEqual(result['status'],400)
        sleep(3)

    def test_weather_no_param(self):
        '''
        Case04-不传入任何city_code值（空）
        '''
        self.case_name = '参数未传入'
        data = {'city_code':''}
        r = requests.get(self.url+'/'+data['city_code'])
        result = r.json()

        self.assertEqual(result['message'],'Request resource not found.')
        self.assertEqual(result['status'],404)
        sleep(3)
    def tearDown(self):
        u'''最后输出'''
        return '输出'



if __name__ == '__main__':
    unittest.main()
