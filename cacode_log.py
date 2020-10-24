import logging
from logging.config import dictConfig
import time
import os


class CACode_log:
    logging = logging
    name = ''
    path = ''

    def __init__(self, name):
        self.name = name
        self.path = CACode_log._get_custom_file_name(name)
        dictConfig({
            'version': 1,
            'formatters': {'default': {
                'format': '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s',
            }},
            'handlers': {
                'default': {
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://flask.logging.wsgi_errors_stream',
                    'formatter': 'default'
                },
                'custom': {
                    'class': 'logging.FileHandler',
                    'formatter': 'default',
                    'filename': CACode_log._get_custom_file_name(name),
                    'encoding': 'utf-8'
                },
            },
            'root': {
                'level': 'INFO',
                'handlers': ['custom']
            }
        })

    @staticmethod
    def _mkdir(make_dir_path):
        """
        创建文件
        :param make_dir_path: 文件或者文件夹的路路径
        :return:绝对路径
        """

        path = make_dir_path.strip()
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    @staticmethod
    def _get_custom_file_name(name):
        """
        获取日志的绝对路径
        :return:项目路径+当前时间.log
        """
        log_dir = name + "-log"
        file_name = 'logger-' + \
                    time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
        file_folder = os.path.abspath(os.path.dirname(__file__)) + os.sep + log_dir
        CACode_log._mkdir(file_folder)
        return file_folder + os.sep + file_name
