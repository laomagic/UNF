#coding:utf-8
"""
data_loader conf解释：
dataset: 配置训练数据和训练数据的格式，提供自动加载的功能
field: 针对每一个域提供一个相应的配置，每一个域的tokenzie，最大长度，是否返回padding长度（LSTM用）等
iterator: 提供迭代的配置，包括每个batch大小，device是cpu还是gpu
"""
#data_loader相关
data_loader_conf = {
    "dataset":{
        "path": "test/test_data/data",
        "train": "train",
        "validation": "valid",
        "test": "test",
        "format": "json"
    },
    "fields":[{
        "name":"TEXT",
        "name_cls":"WordField",
        "attrs":{
            "tokenize":"WhitespaceTokenizer",
            "min_count": 3
            }
        },
        {
            "name":"LABEL",
            "name_cls":"LabelField",
        }],
    "iterator":{
        "batch_size":512,
        "shuffle": True,
    }
}

#模型相关
model_conf = [
    {
        "name": "TEXT",
        "encoder_cls": "TextCnn",
        "encoder_params": {
            "input_dim": 100,
            "filter_num": 100,
            "filter_size": [1,2,3,4],
            "pretrained": False,
        }
    }
]


#learner相关的
learner_conf = {
    "num_epochs": 6,
    "optimizer": "Adam",
    "optimizer_parmas": {
        "lr": 1e-4
    },
    "device": "cuda:0",
    "loss": "CrossEntropyLoss",
    "serialization_dir": "sample_dir",
    "label_tag": "1",
    "use_fp16": False,
    "multi_gpu": False
}

