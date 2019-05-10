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