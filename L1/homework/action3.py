# Action3: 统计全班的成绩
import numpy as np

scoretype = np.dtype({'names': ['name', 'chinese', 'math', 'english'],
                      'formats': ['U32', 'i', 'i', 'i']})
peoples = np.array(
    [
        ("张飞", 68, 65, 30),
        ("关羽", 95, 76, 98),
        ("刘备", 98, 86, 88),
        ("典韦", 90, 88, 77),
        ("许褚", 80, 90, 90)
    ], dtype=scoretype)
print("科目 | 平均成绩 | 最小成绩 | 最大成绩 | 方差 | 标准差")
courses = {'语文': peoples[:]['chinese'],
           '英文': peoples[:]['english'], '数学': peoples[:]['math']}
for course, scores in courses.items():
    print(course, np.mean(scores), np.amin(scores), np.amax(scores), np.std(scores),
          np.var(scores))
print('Ranking:')
ranking = sorted(peoples, key=lambda x: x[1]+x[2]+x[3], reverse=True)
print(ranking)