"""案例驱动示例：不同科目加不同分，再计算偏离均值"""
# 对应 PDF：11-numpy-full.pdf 第 37—46 页
# 任务：三科分别加5、2、3分，再看每位学生与各科平均的差距。
# 广播从最右侧比较形状：长度相等或一方为1才兼容；缺少的左侧轴视为1。
# 案例数据：
# | 学生 | Python | 数学 | 英语 |
# |---|---:|---:|---:|
# | A | 80 | 70 | 90 |
# | B | 60 | 85 | 75 |
# | C | 90 | 65 | 80 |
# 先看整体路线：
# 第 1 步：用嵌套循环完成按科目加分。
# 第 2 步：用显式重复数组重算，观察多余存储。
# 第 3 步：用广播代替重复，再减各科均值。

import numpy as np
scores=np.array([[80,70,90],[60,85,75],[90,65,80]])
bonus=np.array([5,2,3])
manual=[[scores[i,j]+bonus[j] for j in range(3)] for i in range(3)]
print('\n===== manual =====')
print(manual)
# tile(a,reps) 显式重复数据；这里每人复制一份加分规则。
repeated=np.tile(bonus,(3,1))
print('\n===== scores+repeated =====')
print(scores+repeated)
# (3,3)+(3,)：把右边视为(1,3)，学生轴1可扩展，科目轴3匹配。
adjusted=scores+bonus
print('\n===== adjusted =====')
print(adjusted)
means=scores.mean(axis=0,keepdims=True)
# (3,3)-(1,3) 表示每行都减去相同的三科均值。
centered=scores-means
print('\n===== centered =====')
print(centered)
print('\n===== centered.mean(axis=0) =====')
print(centered.mean(axis=0))
# 为每名学生加不同分，需(3,1)，不能误用(3,)而碰巧按科目加。
per_student=np.array([1,2,3])[:,None]
print('\n===== scores+per_student =====')
print(scores+per_student)
assert np.array_equal(adjusted,manual)
assert np.allclose(centered.mean(axis=0),0)
# (3,3)+(2,)不兼容。先口算shape，不执行错误表达式以免中断学习。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 让不同但兼容形状的数据批量运算。
# 2. 科目加分规则要重复作用到每个学生，不必真复制多份。
# 3. 循环给基准，tile显式展示重复，再用广播省掉副本，最后验证中心化。
# 4. 广播避免显式重复的小数组，但运算结果仍占内存，轴方向错误会产生合理外观的错数。
