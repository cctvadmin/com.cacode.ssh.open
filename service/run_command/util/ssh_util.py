import paramiko

import cacode_log

_log = cacode_log.CACode_log('run_command_ssh_util')
log = _log.logging


def linux_get_conn(hostname='127.0.0.1', port=22, username='root', password='123'):
    """
    获取与远程linux主机的连接，记得关闭连接

    :param hostname:ip地址

    :param port:端口，默认22

    :param username:登录名

    :param password:密码

    :return:
    """
    paramiko.util.log_to_file(_log.path)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=port, username=username, password=password)
    return ssh


def linux_exec_cmd(ssh, command):
    """
    连接远程linux主机执行命令

    :param ssh:已经获得连接的ssh对象
    首先使用使用get_ssh_conn(**args)获取ssh连接

    :param command:要执行的命令

    :return:执行的结果，返回真实的样式
    """
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    result = ''
    for i in lines:
        result += i
    return result


#
# def win_get_conn():
#     暂时不支持window
#     wintest = winrm.Session('localhost:3389', auth=('administrator', ''))
#     ret = wintest.run_cmd('ipconfig')
#     print(ret)

def demo():
    """
     conn = linux_get_conn('101.37.76.55', 22, 'root', 'ABSznh123')

     line = linux_exec_cmd(conn, "ls")

     print(line)

     line = linux_exec_cmd(conn, "ls")

     print(line)

     line = linux_exec_cmd(conn, "ls")

     print(line)

     conn.close()
    :return:
    """


if '__main__' == __name__:
    pass
