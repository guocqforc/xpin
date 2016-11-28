# -*- coding: utf-8 -*-

"""
支持ssh pam

所有步骤都用 root 执行

1. 安装 pam
    yum install pam pam-devel -y

2. 下载 http://pam-python.sourceforge.net/ 并编译.
    wget http://downloads.sourceforge.net/project/pam-python/pam-python-1.0.6-1/pam-python_1.0.6.orig.tar.gz

    cd src; make; make install

    centos 6.4 x64默认编译不过，修改 src/Makefile，将编译告警等级调低
    WARNINGS=-Wunreachable-code

    如果报错找不到python，安装一下最新的python2.x即可

    注意:
        默认 pam_python.so会安装在 /lib/security
        但有些系统会要求pam_python.so安装在: /lib64/security/ 目录下，所以可以手动copy一下

3. 将ssh_pam目录下所有文件 copy 到 /lib/security/

4. 修改 修改/etc/pam.d/sshd，顶上新增一行
    auth       required     pam_python.so    ssh_pam.py

5. 修改/etc/ssh/sshd_config
    ChallengeResponseAuthentication yes

    # 可选，禁用掉公钥登录
    PubkeyAuthentication no

6. 安装xpin

    pip install xpin

7. 重启 sshd
    service sshd restart

错误日志: /var/log/secure
"""

from xpin import API


MAX_TRY_TIMES = 3

XPIN_CLIENT_SECRET = 'xxx'

XPIN_BASE_URL = 'http://127.0.0.1:5000/'

XPIN_TIMEOUT = 30

XPIN_SOURCE = 'ssh'

xpin_client = API(XPIN_CLIENT_SECRET, XPIN_BASE_URL, XPIN_TIMEOUT)


def pam_sm_authenticate(pamh, flags, argv):
    username = pamh.get_user()

    pin = xpin_client.create_pin(username, XPIN_SOURCE)

    if not pin:
        return pamh.PAM_AUTH_ERR

    for it in xrange(0, MAX_TRY_TIMES):
        msg = pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, "Pin: ")
        resp = pamh.conversation(msg)
        if pin == resp.resp:
            return pamh.PAM_SUCCESS
        else:
            continue

    return pamh.PAM_AUTH_ERR


# 以下都是默认函数
def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_acct_mgmt(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_open_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS


def pam_sm_chauthtok(pamh, flags, argv):
    return pamh.PAM_SUCCESS
