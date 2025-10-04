import yaml
import os

root_dir = '/src/kafka-producer'
with open(f'{root_dir}/config/application.yml', 'r') as config:
    all_conf_dict = yaml.load(config, Loader=yaml.FullLoader)

for (root, dirs, files) in os.walk(root_dir):
    if root.find('/.git') > 0 or root.find('/config/') > 0 or root.find('/.github/') > 0:
        continue

    if len(files) > 0:
        for file in files:
            if file.endswith('.py'):
                with open(f'{root}/{file}','r', encoding='utf-8') as file_read:
                    py_file_all = ''.join(file_read.readlines())
                    with open(f'{root}/{file}','w', encoding='utf-8') as file_write:

                        for conf_item_dict in list(all_conf_dict.values()):
                            for k, v in conf_item_dict.items():
                                py_file_all = py_file_all.replace(f'##{k}##', v)
                            file_write.write(py_file_all)