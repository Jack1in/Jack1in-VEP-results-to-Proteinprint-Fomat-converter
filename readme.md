# NCBI MANE Select Data Retrieval Script

## 项目简介

这个 Python 脚本使用 Selenium 自动化工具从 NCBI（数据库检索特定的遗传数据。它专门用于识别和提取标记为 "MANE Select" 的遗传特征，并将相关数据保存到本地文件中。原始数据为进行VPE突变注释后的txt文档，结果数据符合ProteinPrint绘图的数据格式

## 安装步骤

在运行此脚本之前，您需要安装 Python 和一些依赖库。

### 预先要求
- Python 3.x
- pip (Python 包管理器)

### 安装指南

1. **安装 Selenium**：在您的终端或命令提示符中运行以下命令来安装 Selenium。

    ```bash
    pip install selenium
    ```

2. **安装 WebDriver Manager**：此脚本使用 Chrome 浏览器的自动化，因此需要安装 WebDriver Manager。

    ```bash
    pip install webdriver-manager
    ```

## 使用说明
1.准备数据
    原始数据格式为VPE突变注释结果（https://grch37.ensembl.org/Homo_sapiens/Tools/VEP）的txt格式，**将其存储为data.txt** 具体参考仓库中的data example.txt
    
1. **运行脚本**：使用 Python 运行脚本。

    ```bash
    python GraphDataComplete.py
    ```

2. **输出文件**：脚本执行完毕后，会生成两个文件 - `MANE_select.txt` 和 `graph.txt`，前者为标有"MANE Select" 的遗传特征的数据，后者为转化为ProteinPrint绘图格式的数据

## 功能说明

- **数据检索**：脚本会访问 NCBI 数据库，检索每个特定遗传特征，确定其是否被标记为 "MANE Select"。
- **数据转换**：提取的数据会被转换并保存到 `graph.txt` 文件中，以便进一步分析。

## 注意事项

- 确保您的系统已安装 Chrome 浏览器。
- 由于脚本依赖于外部网络资源，因此执行期间需要稳定的网络连接。

## 联系方式

如有任何问题或需要进一步的帮助，请通过 3272602487@qq.com 联系我。
