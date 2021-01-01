import json
import os

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        conf = f.read()
    conf = json.loads(conf)
else:
    default_json = {
        "data_host": "localhost",
        "data_user": "root",
        "data_pwd": "",
        "data_database": ""
    }
    with open('config.json', 'w') as f:
        json.dump(default_json, f, indent=4)
    raise FileExistsError('未检测到config.json，已生成默认配置，请修改后再启动"')


def get_conf(key, default=None):
    return conf.get(key, default)
