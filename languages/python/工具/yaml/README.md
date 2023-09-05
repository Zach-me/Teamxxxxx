# yaml

## 📖 简介

- 🌈 yaml 文件是一种数据序列化语言，其良好的跨语言、跨平台、易于理解、格式简单而广泛应用于配置文件、数据文件、日志文件等，因为采用了缩进方式表示层级关系，在python语言中使用就显得更加亲切。

## ✨ 特性

- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用Tab键，只允许使用空格
- 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
- 使用#进行注释，从这个字符一直到行尾，都会被解析器忽略

## ⏬ 下载安装

```bash
pip install ruamel.yaml
```

## 🌰 使用Demo

python 中读取 yaml 文件

- 其实就是将 yaml 格式的数据转化为 python 中的数据类型（字典、列表及基本类型）的过程。

```python
from ruamel.yaml import YAML
import pprint # 美化输出数据
yaml = YAML(typ='safe')
with open(r'e:\area.yaml',“r“,encoding='utf-8') as file:
    data = yaml.load(file) 
pprint.pprint(data)
```

python 数据输出到 yaml 文件中

- 其实是将python中的字典、列表等数据类型写入yaml格式文件中。

```python
from ruamel.yaml import YAML
import pprint
area = {
    '山东': [
        {'济宁': ['邹城', '兖州', '曲阜', '泗水']},
        {'济南': ['历下区', '莱城区', '高新区']},
        '青岛',
        '菏泽'
    ],
    '河北': [
        '石家庄',
        '廊坊',
        '张家口',
        '唐山'
    ],
'直辖市': {'经济中心': '深圳', '行政中心': '北京', '金融中心': '上海'}}
yaml = YAML(typ='safe')
with open(r'e:\area1.yaml','w', encoding='utf-8') as file:
yaml.dump(area,file)
```
