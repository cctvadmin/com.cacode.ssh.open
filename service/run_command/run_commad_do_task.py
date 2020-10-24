import cacode_log
from service.json_templates import _return
from service.run_command.util import ssh_util, messy_util

_log = cacode_log.CACode_log('run_command')
log = _log.logging


class Do_Task:
    info = {}

    def __init__(self, info=None):
        """
        携带参数：

        host:主机ip地址

        port:端口默认22

        user:用户名

        password:密码

        :param info:主机信息
        """
        self.info = info
        log.info(info)

    def do(self, info=None):
        """
        正式操作
        :return:
        """
        if info is None and self.info is None:
            result = _return.tem(500, 'instance info is null', {'error': 'error'})
            return result
        elif info is None:
            instance_info = self.info
        else:
            instance_info = info
        all_args_str = ['host', 'port', 'user', 'password', 'command']
        for key in all_args_str:
            if key not in instance_info:
                msg = f'not have args {key}'
                return _return.tem(500, msg, {'error': msg})
        host = instance_info['host']
        port = instance_info['port']
        user = instance_info['user']
        password = instance_info['password']
        command = instance_info['command']
        all_args = [host, port, user, password, command]
        i, all_not_null = messy_util.allNotNull(all_args)
        if not all_not_null:
            msg = f'args {all_args_str[i]} is empty'
            return _return.tem(500, msg, {'error': msg})

        ssh_conn = ssh_util.linux_get_conn(hostname=host, port=port, username=user, password=password)
        result = ssh_util.linux_exec_cmd(ssh_conn, command)

        return _return.tem(200, 'connect is ok', {'success': '200', 'result': result})
