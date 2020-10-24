from service.run_command import run_commad_do_task
import cacode_log

_log = cacode_log.CACode_log('run_command')
log = _log.logging


def run_command(host, port, user, password, command):
    if port is None:
        port = 22
    # 实例信息
    instance_info = {
        'host': host,
        'user': user,
        'password': password,
        'command': command,
        'port': port
    }
    _do_task = run_commad_do_task.Do_Task(instance_info)
    _result = _do_task.do()
    return _result


def comments():
    return 'access place using "run_command" interface<br>' \
           'and match carry args:host,user,password,command<br>' \
           'default using ssh host is:22' \
           'if you wall to using you customize port,you can carry args:port'


if __name__ == '__main__':
    comments()
