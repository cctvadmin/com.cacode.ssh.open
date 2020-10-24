from flask import Flask, request, Response
from configparser import ConfigParser
import cacode_log
import json
import os
from service.json_templates import _page
from service.run_command import run_command_controller

app = Flask(__name__)
log = cacode_log.CACode_log('run_command_main').logging


@app.route('/ssh/<_host>')
def dockerConsole(_host):
    _port = request.args.get('port')
    _user = request.args.get('user')
    _pwd = request.args.get('password')
    _command = request.args.get('command')
    _key = request.args.get('key')
    result = run_command_controller.run_command(host=_host,
                                                port=_port,
                                                user=_user,
                                                password=_pwd,
                                                command=_command)
    return Response(json.dumps(result), mimetype='application/json')


@app.route('/init_server')
def index():
    _abs_path = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'config/init.conf'
    _config = ConfigParser()
    _config.read(filenames=_abs_path, encoding='utf-8')
    cmds = _config.items('command')
    user = _config.get('local', 'user')
    host = _config.get('local', 'host')
    password = _config.get('local', 'password')
    port = _config.get('local', 'port')

    commands = []
    for i in cmds:
        commands.append(i[1])
    _result = []
    for cmd in commands:
        try:
            result = run_command_controller.run_command(host=host,
                                                        port=port,
                                                        user=user,
                                                        password=password,
                                                        command=cmd)
            _result.append(result)
        except Exception as e:
            _result.append({
                'error': str(e)
            })
    if _result == '':
        _result = _page.null_tem()
    return json.dumps(_result)


@app.route('/')
def init():
    return _page.null_tem()


if __name__ == '__main__':
    app.run()
