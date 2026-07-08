# 项目落地示例

## 静态数据查询网站

适合使用 `web-static` profile。

推荐 Agent：

```text
manager：读项目、拆任务、派发、验收、汇报
design：设计方案和实现 brief
preview：隔离目录生成预览，不改生产页面
code：生产代码实现和 Playwright 验证
data：数据读取、生成、审计、字段口径
assets：轮播、图片、压缩和引用
research：外部参考研究，不改项目
release：git status、diff check、commit/push，必须等用户确认
docs：版本记忆和 Markdown 一致性
```

示例流程：

```text
用户：优化移动端结果卡
manager：确认范围和验收标准
design：输出移动端信息层级 brief
preview：生成 2-3 个预览方案
用户：选择方案
code：按方案改生产代码
validator/code：跑 Playwright 和截图检查
docs：更新版本记忆
release：用户明确同意后提交推送
```

关键边界：

- 数据字段判断归 data。
- 预览图只在隔离目录。
- 生产代码只由 code 根据 brief 改。
- 发布必须等用户确认。

## 内容团队

适合使用 `content-team` profile。

推荐 Agent：

```text
manager：定位、节奏、选题优先级
topic：选题会、话题池、标题方向
content：大纲、脚本、正文、发布文案
material：封面、截图、素材清单
review：数据复盘、方向调整
```

示例流程：

```text
topic 新增选题
-> content 生成大纲
-> material 准备封面和素材
-> 人类拍摄或发布
-> review 拉数据并总结
-> manager 调整后续方向
```
