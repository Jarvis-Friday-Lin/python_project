"""可运行示例：先预测结果，再执行。"""

import json
data = {"name": "小林", "skills": ["Python", "Pandas"]}
text = json.dumps(data, ensure_ascii=False, indent=2)
restored = json.loads(text)
print(text)
print(restored["skills"])
