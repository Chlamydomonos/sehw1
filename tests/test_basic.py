import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''
    def test_register_params_check(self):
        content = None
        self.assertEqual(register_params_check(content), ('error: content', False))
        content = {}
        self.assertEqual(register_params_check(content), ('lost: username', False))
        content['username'] = 0
        self.assertEqual(register_params_check(content), ('error: username', False))
        content['username'] = 'asd'
        self.assertEqual(register_params_check(content), ('error: username', False))
        content['username'] = 'asd123'
        self.assertEqual(register_params_check(content), ('lost: password', False))
        content['password'] = 0
        self.assertEqual(register_params_check(content), ('error: password', False))
        content['password'] = 'Asd123'
        self.assertEqual(register_params_check(content), ('error: password', False))
        content['password'] = 'Asd123-^'
        self.assertEqual(register_params_check(content), ('lost: nickname', False))
        content['nickname'] = 0
        self.assertEqual(register_params_check(content), ('error: nickname', False))
        content['nickname'] = ''
        self.assertEqual(register_params_check(content), ('lost: url', False))
        content['url'] = 0
        self.assertEqual(register_params_check(content), ('error: url', False))
        content['url'] = 'http://'
        self.assertEqual(register_params_check(content), ('error: url', False))
        content['url'] = 'http://a.b'
        self.assertEqual(register_params_check(content), ('lost: mobile', False))
        content['mobile'] = 0
        self.assertEqual(register_params_check(content), ('error: mobile', False))
        content['mobile'] = '+11.1'
        self.assertEqual(register_params_check(content), ('error: mobile', False))
        content['mobile'] = '+11.111111111111'
        self.assertEqual(register_params_check(content), ('ok', True))
        content['magic_number'] = 0
        self.assertEqual(register_params_check(content), ('error: magic_number', False))
        content['magic_number'] = '-1'
        self.assertEqual(register_params_check(content), ('error: magic_number', False))
        content['magic_number'] = '0'
        self.assertEqual(register_params_check(content), ('ok', True)) 


if __name__ == '__main__':
    unittest.main()
