# -*- coding: utf-8 -*-

import re
from typing import Dict


_USERNAME = re.compile(r'^(?=.{5,12}$)[A-Za-z]+\d+$')
_PASSWORD = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[-_*^])(?=.{8,15}$)[A-Za-z0-9-_*^]*$')
_URL = re.compile(r'^(?=https?://.{0,48}$)https?://(([A-Za-z0-9]|(?<![\./])-(?!\.))+\.)+([0-9](?![0-9]*$)|[A-Za-z])([A-Za-z0-9]|-(?!$))*$')
_MOBILE = re.compile(r'^\+\d{2}\.\d{12}$')
_MAGIC_NUMBER = re.compile(r'^0|([1-9][0-9*])$')

def register_params_check(content: Dict):
    """
    TODO: 进行参数检查
    """
    if not isinstance(content, Dict):
        return 'error: content', False

    if 'username' in content:
        username = content['username']
        if not isinstance(username, str) or not _USERNAME.match(username):
            return 'error: username', False
    else:
        return 'lost: username', False

    if 'password' in content:
        password = content['password']
        if not isinstance(password, str) or not _PASSWORD.match(password):
            return 'error: password', False
    else:
        return 'lost: password', False

    if 'nickname' in content:
        nickname = content['nickname']
        if not isinstance(nickname, str):
            return 'error: nickname', False
    else:
        return 'lost: nickname', False

    if 'url' in content:
        url = content['url']
        if not isinstance(url, str) or not _URL.match(url):
            return 'error: url', False
    else:
        return 'lost: url', False

    if 'mobile' in content:
        mobile = content['mobile']
        if not isinstance(mobile, str) or not _MOBILE.match(mobile):
            return 'error: mobile', False
    else:
        return 'lost: mobile', False

    if 'magic_number' in content:
        magic_number = content['magic_number']
        if not isinstance(magic_number, str) or not _MAGIC_NUMBER.match(magic_number):
            return 'error: magic_number', False
    else:
        content['magic_number'] = '0'

    return 'ok', True
