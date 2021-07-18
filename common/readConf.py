# -*- coding: utf-8 -*-
# Created by YUYONG on 2021/7/18

import configparser
import os


class ReadConf(object):
    conf_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'conf.ini')

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(self.conf_file)

    def get_env(self):
        env = self.conf.get("Env", "env")
        return env


# if __name__ == '__main__':
#     pass
#     conf = ReadConf()
#     print('conf_file: ' + conf.conf_file)
    # env = conf.get_env()
    # print(env)
