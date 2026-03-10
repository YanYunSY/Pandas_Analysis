# Pandas 数据分析实战训练营
这份代码涵盖日常数据分析工作中最常用的 6 大核心场景，从「脏数据清洗」到「多表合并汇报」，全程可直接运行。

## 核心内容
| 关卡 | 主题                | 核心知识点                          |
|------|---------------------|-------------------------------------|
| 1    | 数据探查与概览      | head()、info()、isnull()            |
| 2    | 数据清洗            | drop_duplicates()、fillna()         |
| 3    | 特征工程            | to_datetime()、列运算创建新列       |
| 4    | 多条件筛选          | 布尔索引、& 多条件连接              |
| 5    | 分组聚合            | groupby()、agg()、sort_values()     |
| 6    | 多表合并            | pd.merge() 左连接（等价Excel VLOOKUP）|

## 运行环境
- Python 3.8+
- Pandas 2.0+
- 可选：openpyxl（导出Excel需安装：pip install openpyxl）

##核心依赖库（必须安装）
| 库名         | 最低版本  | 功能说明                          | 安装命令                  |
|--------------|-----------|-----------------------------------|---------------------------|
| pandas       | 2.0.0+    | 核心数据分析库（处理表格、清洗、聚合） | `pip install pandas>=2.0.0` |
| numpy        | 1.21.0+   | 数值计算基础（支持Pandas空值填充、运算） | `pip install numpy>=1.21.0` |
| matplotlib   | 3.5.0+    | 可选（代码中仅配置中文，无绘图逻辑）| `pip install matplotlib>=3.5.0` |

## 快速开始
```bash
# 克隆仓库
git clone https://github.com/YanYunSY/pandas_analysis_camp.git

# 安装依赖
pip install pandas numpy matplotlib openpyxl

# 运行代码
python pandas_analysis_camp.py