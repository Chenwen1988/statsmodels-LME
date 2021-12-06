# Linear Mixed Effect Model

[toc]

## Basic

- Understand [LME]()

- How to use [LME](https://www.statsmodels.org/stable/examples/notebooks/generated/mixed_lm_example.html) with Pyhton
- LME常用来解决两类问题
  1. 样本不独立，带有一定分组结构的，组内样本不独立；
  2. 可以作为第一类问题的特例，就是样本带有序结构（比如时间）的数据，时间形成分组；

- LME中的分为固定效应和随机效应，拟合模型输出固定效应系数和随机效应方差

- LME常用的模型结构可以很复杂，但最常用的就是随机效应分别作为常数项或随机效应作为某固定效应变量系数，效果示意图如下所示

  ![1638801674553](D:\华西统计\Inter or Slope random effects.png)

> 总的来说，一般线性回归(OLR)是计算相关系数的升级，LME是计算分组相关系数的升级，还是相当实用滴。



## Example



```python
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
```

```python
data = pd.read_csv('./AlDep',sep = '\t')
```

| Hospital | PhysNo | Experiment | ADR  | filmNo | ExpertScore | Time     | AlScore  |
| -------- | ------ | ---------- | ---- | ------ | ----------- | -------- | -------- |
| 1        | 1      | 1          | 0.15 | 1      | 10          | 2.006    | 0.12802  |
| 1        | 1      | 1          | 0.15 | 2      | 9.333333333 | 1.592667 | 0.14788  |
| 1        | 1      | 1          | 0.15 | 3      | 10          | 5.078    | 0.213409 |
| 1        | 1      | 1          | 0.15 | 4      | 13.33333333 | 3.056667 | 0.331254 |
| 1        | 1      | 1          | 0.15 | 5      | 7.333333333 | 1.369333 | 0.075816 |
| 1        | 1      | 1          | 0.15 | 6      | 11.66666667 | 3.162667 | 0.168641 |
| 1        | 1      | 1          | 0.15 | 7      | 10.33333333 | 2.712    | 0.152469 |

```python
md = smf.mixedlm("AlScore ~ ADR",data,groups = data["Hospital"])
mdf = md.fit()
print(mdf.summary())
```

![1638788298204](D:\华西统计\ModelSummary-ADR.png)

我们将医院作为分组变量，分析Al评估的图像质量（AlScore）与医生历史息肉检出率（ADR）的关系。

混合效应模型结果显示Al评分结果与医生的ADR显著相关，医生的ADR越高，操作窥镜的得到的影片质量越高。



我们将医生作为分组变量，进一步分析Al评估的图像质量与操作时长（Time）的关系。

```python
md = smf.mixedlm("AlScore ~ Time",data,groups = data["Phys"])
mdf = md.fit()
print(mdf.summary())
```

![1638788818990](D:\华西统计\ModelSummary-Time.png)

混合效应模型结果显示Al评分结果与医生的操作时长并无显著相关性。