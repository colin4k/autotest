# autotest
Generate Auto Test Scripts by AI\

## 安装
```bash
conda create -n autotest python=3.12
conda activate autotest
pip install -r requirements.txt
```

## 配置
```bash
cp config.yaml.example config.yaml
vi config.yaml
#配置自己在 Siliconflow 的 apikey
openai_api_key: "sk-xxxxxx"

#配置接口文件保存地址的绝对路径
docs_directory: "/Users/colin/workspace/autotest/interfaces"
```

## 使用
1\.准备接口文档，可从 tarno 中导出markdown 格式的接口文档;
2\.将接口文档保存到上述 `docs_directory` 参数所设定的文件夹，并将文件名写入 `interface.txt`，一行一个文件名;
3\.执行 `python main.py`，生成的 `python` 文件将保存在当面目录下的 `interfaces-script` 目录下。


