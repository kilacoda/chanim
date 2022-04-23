# Chanim

这是[Manim库](https://github.com/ManimConmunity/manim)（最初由[3Blue1Brown](https://github.com/3b1b/manim)创建）的一个扩展，用于制作有关化学的视频。
## 安装（使用pip）

`pip install chanim`
## 安装（使用克隆）

1. 首先，根据你的系统，由[此处](https://docs.manim.community/en/latest/installation.html)下载应有的外部依赖项。
2. 克隆此存储库。
3. 在克隆目录中打开一个终端，输入并执行`pip install -e`，或者输入`poetry install`（如果你更喜欢使用[poetry](https://python-poetry.org)的话）

如果上述流程顺利，您就可以使用`from chanim import <*|some object name>`以使用chanim了。

### 注意！无论使用什么安装方式，您都必须安装外部依赖项！
## 使用

这里有一个使用的小例子。
```py
from chanim import *

class ChanimScene(Scene):
    def construct(self):
        ## ChemWithName 会创建一个带有标签的化学分子式
        chem = ChemWithName("*6((=O)-N(-CH_3)-*5(-N=-N(-CH_3)-=)--(=O)-N(-H_3C)-)", "Caffeine")

        self.play(chem.creation_anim())
        self.wait()
```
把它保存为一个python文件，我先假设你将其命名为`chem.py`（当然，什么名字都可以）。

接着，在`chem.py`所在的文件夹打开终端，输入以下指令：

`manim -p -qm chem.py ChanimScene`

这将渲染该场景并使用您的默认播放器播放它（以中等画质播放）。如果一切顺利，它应当播放如下情景：

https://user-images.githubusercontent.com/65204531/124297601-dcafcf80-db78-11eb-936b-cdc913c91f25.mp4

恭喜！你制作出了你的第一个Chanim视频（或者叫做Chanimation)!
通过学习源码和将推出的文档以继续学习Chanim。
## 功能

目前Chanim仅支持绘制一些化学分子和Chemfig指令（Chemfig 是一个latex包，可以绘制配位键等化学分子。描述文档网站在[这里]（http://ctan.imsc.res.in /macros/generic/chemfig/chemfig-en.pdf)
但我们会推出更多！如果您有建议或者问题，请用标签提交适当的issue。
## 附记

这个库目前仍不完善，可能有一些错误的地方。如果影响到了您的使用，欢迎提出自己的建议和修改。
