# cloud-computing-lab

云计算课程 8.3 课后作业的个人项目仓库。

## 关于我

- 网名 / GitHub：XIngJIuuu
- 方向：前端 + Python，正在学习 AI 应用开发
- 这门课覆盖：Linux 基础、Git 与 GitHub、SSH 远程开发、Docker 与虚拟化

## 仓库内容

| 文件 | 说明 |
|---|---|
| `cloud_bill.py` | 云服务器（ECS）费用估算小工具，Python 实现 |
| `.gitignore` | 忽略 Python 缓存等本地文件 |

## 运行方式

```bash
python cloud_bill.py        # 估算单台服务器费用
python cloud_bill.py 3      # 估算 3 台的包年总价
```

输出各规格云服务器的包月、包年（85 折）费用。

## 开发记录

1. 初始化仓库，添加 README 与第一版计费脚本
2. 新增包年折扣，支持按台数估算