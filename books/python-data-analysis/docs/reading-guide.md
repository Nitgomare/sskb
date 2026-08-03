# 按章学习路线

路线完全依照教材目录组织；“优先级”只帮助研究生按需求取舍，不改变书中结构。

## 第一阶段：数据处理核心

| 教材章 | 内容 | 优先级 | 可检查输出 |
|---|---|---|---|
| [1 数据分析基础](chapters/01-chapter/index.md) | 方法、流程与常用模块 | 必读 | 为自己的课题画数据分析流程 |
| [2 开发环境](chapters/02-chapter/index.md) | Anaconda、Jupyter、PyCharm | 按需 | 从空环境运行一个 Notebook |
| [3 NumPy 数组计算](chapters/03-numpy/index.md) | 数组、矩阵、数学、统计、排序 | **核心** | 将一段循环改写为向量化运算 |
| [4 Pandas 基础](chapters/04-pandas/index.md) | Series、DataFrame、索引 | **核心** | 解释行列索引与布尔选择 |
| [5 数据读取](chapters/05-pandas/index.md) | 文本、Excel、CSV、HTML、数据库 | **核心** | 读入真实数据并保存数据字典 |
| [6 数据处理](chapters/06-pandas/index.md) | 抽取、增删改查、排序排名 | **核心** | 写一条可重复的数据处理链 |
| [7 数据清洗](chapters/07-pandas/index.md) | 缺失、重复、异常、字符串、转换 | **核心** | 生成清洗前后质量报告 |
| [8 计算与格式化](chapters/08-chapter/index.md) | 常见 / 高级计算与格式 | 必读 | 将派生变量写成可测试函数 |
| [9 统计与透视](chapters/09-chapter/index.md) | 分组、移位、合并、透视 | **核心** | 用 groupby 与透视表回答同一问题 |
| [10 日期与时间](chapters/10-chapter/index.md) | 频率、采样、移动窗口 | 研究数据常用 | 构造无未来信息泄漏的滚动特征 |
| [11 Scikit-Learn](chapters/11-scikit-learn/index.md) | 线性模型、SVM、聚类 | 选读 | 建立带预处理的基线模型 |

## 第二阶段：可视化表达

| 教材章 | 内容 | 最低输出 |
|---|---|---|
| [12 Matplotlib 入门](chapters/12-matplotlib/index.md) | 基本设置与常用图表 | 一张标签、单位、图例完整的结果图 |
| [13 Matplotlib 进阶](chapters/13-matplotlib/index.md) | 色彩、日期、双轴、子图、3D | 一张多面板对照图；说明为何需要每个面板 |
| [14 Seaborn](chapters/14-seaborn/index.md) | 统计图与样式 | 用分布和关系图检查数据假设 |
| [15 Plotly](chapters/15-plotly/index.md) | 交互式图表 | 一个仅在交互确有价值时使用的图 |
| [16 Bokeh](chapters/16-bokeh/index.md) | 浏览器交互图表 | 比较静态图与交互图的适用边界 |
| [17 Pyecharts](chapters/17-pyecharts/index.md) | ECharts Python 接口 | 制作一张可复用的交互图 |

## 第三阶段：完整项目

| 教材章 | 案例 | 学习重点 |
|---|---|---|
| [18 股票数据分析](chapters/18-chapter/index.md) | 金融时间序列 | 数据获取、时间索引与趋势表达 |
| [19 淘宝网订单分析](chapters/19-chapter/index.md) | 订单数据 | 清洗、分组统计与业务指标 |
| [20 网站用户数据分析](chapters/20-chapter/index.md) | 用户行为 | 行为指标与可视化表达 |
| [21 NBA 球员薪资分析](chapters/21-nba/index.md) | 多源体育数据 | 数据整合、关系分析与结论表达 |

## 科研数据检查清单

- [ ] 原始数据只读保存，清洗结果写入新文件
- [ ] 明确变量单位、缺失值编码和时间范围
- [ ] 合并前检查键的唯一性，合并后检查行数
- [ ] 画图前说明图要回答的问题
- [ ] 图中包含轴名、单位、样本量与必要的不确定性
- [ ] Notebook 能按“重启并全部运行”无错误执行

[开始阅读第 1 章](chapters/01-chapter/index.md){ .md-button .md-button--primary }
