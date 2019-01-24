import allure

class TestAllure:
    def test_a(self):
        print('aaa')
        assert 1

    @allure.step(title='测试登录的流程')
    def test_login(self):
        allure.attach('登录', '输入用户名')
        print('bbb')

        allure.attach('登录', '输入密码')
        print('cccc')

        allure.attach('登录', '点击登录')
        print('ddd')
        assert 1