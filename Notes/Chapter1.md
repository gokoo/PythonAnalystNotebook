# 第一章 准备工作
## 1.3 重要的Python库
- [**NumPy**](https://www.numpy.org.cn)
  > NumPy（Numerical Python的简称）是Python科学计算的基础包。本书大部分内容都基于NumPy以及构建于其上的库。它提供了以下功能（不限于此）：
  - **快速高效的多维数组对象ndarray。**
  - 用于对数组执行元素级计算以及直接对数组执行数学运算的函数。
  - 用于读写硬盘上基于数组的数据集的工具。线性代数运算、傅里叶变换，以及随机数生成。
  - 成熟的C API，用于Python插件和原生C、C++、Fortran代码访问NumPy的数据结构和计算工具。
- [**pandas**](https://www.pypandas.cn)
  > pandas提供了快速便捷处理结构化数据的大量数据结构和函数。自从2010年出现以来，它助使Python成为强大而高效的数据分析环境。本书用得最多的pandas对象是**DataFrame**，它是一个面向列（column-oriented）的二维表结构，另一个是**Series**，一个一维的标签化数组对象。pandas兼具NumPy高性能的数组计算功能以及电子表格和关系型数据库（如SQL）灵活的数据处理功能。它提供了复杂精细的索引功能，以便更为便捷地完成重塑、切片和切块、聚合以及选取数据子集等操作。因为数据操作、准备、清洗是数据分析最重要的技能，pandas是本书的重点。
- [**matplotlib**](https://www.matplotlib.org.cn)
  > matplotlib是最流行的用于绘制图表和其它二维数据可视化的Python库，非常适合创建出版物上用的图表。虽然还有其它的Python可视化库，matplotlib却是使用最广泛的，并且它和其它生态工具配合也非常完美。可以使用它作为默认的可视化工具。
- [**SciPy**](https://docs.scipy.org/doc/scipy/reference/)  未找到中文版文档
  >SciPy是一组专⻔解决科学计算中各种标准问题域的包的集合，主要包括下面这些包：
  - **scipy.integrate**：数值积分例程和微分方程求解器。
  - **scipy.linalg**：扩展了由numpy.linalg提供的线性代数例程和矩阵分解功能。
  - **scipy.optimiz**e：函数优化器（最小化器）以及根查找算法。
  - **scipy.signal**：信号处理工具。
  - **scipy.sparse**：稀疏矩阵和稀疏线性系统求解器。
  - **scipy.special**：SPECFUN（这是一个实现了许多常用数学函数（如伽玛函数）的Fortran库）的包装器。
  - **scipy.stats**：标准连续和离散概率分布（如密度函数、采样器、连续分布函数等）、各种统计检验方法，以及更好的描述统计法。
  - **NumPy和SciPy结合使用，便形成了一个相当完备和成熟的计算平台，可以处理多种传统的科学计算问题。**
- [**scikit-learn**](http://sklearn.apachecn.org/#/)
  > 2010年诞生以来，scikit-learn成为了Python的通用机器学习工具包。汇聚了全世界超过1500名贡献者。子模块包括：
  - 分类：SVM、近邻、随机森林、逻辑回归等等。
  - 回归：Lasso、岭回归等等。
  - 聚类：k-均值、谱聚类等等。
  - 降维：PCA、特征选择、矩阵分解等等。
  - 选型：网格搜索、交叉验证、
  - 度量。预处理：特征提取、标准化。
- [**statsmodels**](https://www.cherylgood.cn/docPage/statsmodels.html) 非官方文档
  > statsmodels是一个统计分析包，起源于斯坦福大学统计学教授Jonathan Taylor。提供了statsmodels的公式或模型的规范框架。**与scikit-learn比较，statsmodels包含经典统计学和经济计量学的算法**。包括如下子模块：
  - 回归模型：线性回归，广义线性模型，健壮线性模型，线性混合效应模型等等。
  - 方差分析（ANOVA）。
  - 时间序列分析：AR，ARMA，ARIMA，VAR和其它模型。
  - 非参数方法：核密度估计，核回归。统计模型结果可视化。
  - **statsmodels更关注与统计推断，提供不确定估计和参数p-值。相反的，scikit-learn注重预测。**
## 行话 
- **数据规整（Munge/Munging/Wrangling**）指的是将非结构化和（或）散乱数据处理为结构化或整洁形式的整个过程。这几个词已经悄悄成为当今数据黑客们的行话了。Munge这个词跟Lunge押韵。
- **伪码（Pseudocode**）算法或过程的“代码式”描述，而这些代码本身并不是实际有效的源代码。
- **语法糖（Syntactic sugar**）这是一种编程语法，它并不会带来新的特性，但却能使代码更易读、更易写。

# 第2章 Python语法基础，IPython和JupyterNotebooks
## Tips
> 在变量前后使用问号```？```，可以显示对象的信息
```python
In [8]: b = [1, 2, 3]
In [9]: b?
Type: list32
```
> ？可以作为对象的自省。如果对象是一个函数或实例方法，定义过的文档字符串，也会显示出信息。假设我们写了一个如下的函数：
```python
def add_numbers(a, b):   
    """
    Add two numbers together    
    Returns    
    -------    
    the_sum : type of arguments    
    """    
    return a + b
```
> 然后使用?符号，就可以显示如下的文档字符串：
```python
In [11]: add_numbers?
Signature: add_numbers(a, b)
Docstring:
Add two numbers together
Returns
-------
the_sum : type of arguments
File:      <ipython-input-9-6a548a216e27>
Type:      function
```
> 使用??会显示函数的源码：


> ?还有一个用途，就是像Unix或Windows命令行一样搜索IPython的命名空间。字符与通配符结合可以匹配所有的名字。例如，我们可以获得所有包含load的顶级NumPy命名空间：

> 从剪贴板执行程序最简单的方法是使用```%paste```和```%cpaste```函数。```%paste```可以直接运行剪贴板中的代码：使用```%cpaste```，你可以粘贴任意多的代码再运行。你可能想在运行前，先看看代码。如果粘贴了错误的代码，可以用Ctrl-C中断。
## 魔术命令
IPython中特殊的命令（Python中没有）被称作“魔术”命令。这些命令可以使普通任务更便捷，更容易控制IPython系统。魔术命令是在指令前添加百分号%前缀。

> 魔术函数默认可以不用百分号，只要没有变量和函数名相同。这个特点被称为“自动魔术”，可以用```%automagic```打开或关闭

> 一些魔术函数与Python函数很像，它的结果可以赋值给一个变量：
```python
In [22]: %pwd
Out[22]: '/home/wesm/code/pydata-book
In [23]: foo = %pwd
In [24]: foo
Out[24]: '/home/wesm/code/pydata-book'
```
> IPython的文档可以在shell中打开，我建议你用%quickref或%magic学习下所有特殊命令

**常用的指令**

|命令|说明|
|---|---|
|```%quickref```|显示Python的快速参考|
|```%magic```|显示所有魔术命令的详细文档|
|```%debug```|再出现异常的语句进入调试模式|
|```%hist```|打印命令的输入（可以选择输出）历史|
|```%pdb```|出现异常时自动进入调试|
|```%paste```|执行剪贴板中的代码|
|```%cpaste```|开启特别提示，手动粘贴待执行的代码|
|```%reset```|删除所有命名空间的变量和名字|
|```%time statement```|报告单条语句执行的时间|
|```%who，%who_is，%whos```|显示命名空间中的变量，三者显示的信息级别不同|
|```%xdel variable```|删除一个变量，并清空任何对他的引用|

# 第三章 Python的数据结构、函数和文件
## 3.1 数据结构和序列
## 3.2 函数
## 3.3 文件和操作系统
## 3.4 结论

# 第四章 NumPy基础：数组和矢量计算 [Chaper4.ipynb]()
> Day2 task
@所有人
【数据分析组队学习Task 1(2天)】
1. 完成 “Python for Data Analysis(第二版)” 书中第 4 章内容的学习，代码实现的过程上传到 GitHub；
2. 相关参考作业(作为考核指标之一)
    - [ 科赛之 Numpy 练习 (这100道题，带你玩转Numpy)](https://www.kesci.com/home/project/59f29f67c5f3f5119527a2cc)
    -  [Numpy基础学习1](https://blog.csdn.net/Crafts_Neo/article/details/90115742?utm_source=blog_wap_share)
## 4.1 NumPy的ndarray：一种多维数组对象
> 笔记：在本章及全书中，我会使用标准的NumPy惯用法```import numpy as np```。你当然也可以在代码中使用```from numpy import ```，但**不建议这么做**。numpy的命名空间很大，包含许多函数，其中一些的名字与Python的内置函数重名（比如min和max）。

> 笔记：当你在本书中看到“数组”、“NumPy数组”、"ndarray"时，基本上都指的是同一样东⻄，即ndarray对象。

> 注意：认为np.empty会返回全0数组的想法是不安全的。很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。

> 由于NumPy关注的是数值计算，因此，如果没有特别指定，数据类型基本都是float64（浮点数）。~~插图~~

> 使用numpy.string_类型时，一定要小心，**因为NumPy的字符串数据是大小固定的，发生截取时，不会发出警告**。pandas提供了更多非数值数据的便利的处理方法。

> 注意：如果你想要得到的是ndarray切片的一份副本而非视图，就需要明确地进行复制操作，例如arr[5:8].copy()。**(关于Python的深拷贝和浅拷贝)** ~~后面补笔记链接~~

> 布尔型数组的⻓度必须跟被索引的轴⻓度一致



## 4.2 通用函数：快速的元素级数组函数
## 4.3 利用数组进行数据处理
## 4.4 用于数组的文件输入输出
## 4.5 线性代数
## 4.6 伪随机数生成
## 4.7 示例：随机漫步
## 4.8 结论