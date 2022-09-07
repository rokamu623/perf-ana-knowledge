from os import listdir
import os.path

# get sub directory
dir = [d for d in listdir(".") if os.path.isdir(d) is True and d != ".git"]

# add abst
text ="""# perf-ana-knowledge
EmbIVの性能評価グループの共有知識です。

- [閲覧(HP)](https://rokamu623.github.io/perf-ana-knowledge/)
- [編集(Github)](https://github.com/rokamu623/perf-ana-knowledge)
"""

# add pages link
text += """
## Pages
"""

for d in dir:
    text += f"""- [{d}](./{d})
"""

text += """
## Index
"""
text += """- Autoware
  - [AutowareのOO](./Autoware#AutowareのOO)
  - [AutowareのXX](./Autoware#AutowareのXX)
- CARET
  - [CARETのhogehoge](./CARET#CARETのhogehoge)
- Tools
  - [VSCodeの環境導入](./Tools#VSCodeの環境導入)
  - [Githubの環境導入](./Tools#Githubの環境導入)

"""
text += """## How to Use
各々のディレクトリの`README.md`に、テンプレートに従ってTipsを書き込んでください。<br>
『閲覧』をクリックすることでGithub Pagesで閲覧できます。
"""
md = open("./README.md", 'w')
md.write(text)
print(dir)