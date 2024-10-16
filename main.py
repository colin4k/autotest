import yaml
from openai import OpenAI
from pathlib import Path

# 读取配置文件
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# 设置接口文档目录路径
docs_dir = Path(config['docs_directory'])

# 创建 OpenAI 客户端
client = OpenAI(
    api_key=config['openai_api_key'],
    base_url=config['openai_api_base']
)
model_name = config['model_name']

# 获取docs_dir目录下所有的.md文件
interface_files = list(docs_dir.glob('*.md'))

# 创建 interfaces-script 目录（如果不存在）
script_dir = Path('interfaces-script')
script_dir.mkdir(exist_ok=True)

# 循环处理每个接口文档
for interface_file in interface_files:
    # 读取接口文档内容
    with open(interface_file, 'r') as f:
        interface_content = f.read()
    
    # 调用OpenAI API生成测试脚本
    prompt = f"请你作为资深的自动化测试专家，根据以下接口文档内容，调用unittest，不要使用 mock，生成准确、完整的可直接执行的自动化测试的 Python 脚本：{interface_content}，返回内容请只包括可执行的 Python 代码，不要解释，不要为代码块增加代码块修饰符。"
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # 提取生成的Python代码
    test_script = response.choices[0].message.content
    
    # 对生成的代码进行评审
    review_prompt = f"请你作为一个Python专家对以下代码进行评审，确保这些内容满足自动化接口测试的要求，并可以直接作为Python来运行：\n\n{test_script}，返回内容请只包括可执行的 Python 代码，不要解释，也不要有任何注释，不要为代码块增加代码块修饰符。"
    review_response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": review_prompt}]
    )
    
    # 获取评审后的代码
    reviewed_test_script = review_response.choices[0].message.content
    
    # 删除可能存在的代码块修饰符
    reviewed_test_script = reviewed_test_script.strip()
    if reviewed_test_script.startswith("```python"):
        reviewed_test_script = reviewed_test_script[9:]
    if reviewed_test_script.endswith("```"):
        reviewed_test_script = reviewed_test_script[:-3]
    reviewed_test_script = reviewed_test_script.strip()

    # 生成测试脚本文件名
    test_file_name = f"test_{Path(interface_file).stem}.py"
    
    # 将评审后的测试脚本写入 interfaces-script 目录中的文件
    with open(script_dir / test_file_name, 'w') as f:
        f.write(reviewed_test_script)

print("自动化测试脚本生成完成。")
