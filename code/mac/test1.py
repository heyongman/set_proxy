#!/usr/bin/env python3
import base64
import ping3
import re
import os
import json
import subprocess
import requests


def test_connection(
        url='http://ip.cn',
        headers={'User-Agent': 'curl/7.21.3 (i686-pc-linux-gnu) '
                 'libcurl/7.21.3 OpenSSL/0.9.8o zlib/1.2.3.4 libidn/1.18'},
        proxies=None, port=1080, timeout=10):
    if not proxies:
        proxies = {'http': 'socks5://localhost:{}'.format(port),
                   'https': 'socks5://localhost:{}'.format(port)}
    ok = False
    content = ''
    try:
        respond = requests.get(url, headers=headers,
                               proxies=proxies, timeout=timeout)
        ok = respond.ok
        content = respond.text
    except Exception as e:
        print(e)
    return ok, content


ok, content = test_connection()
print(ok, content)
