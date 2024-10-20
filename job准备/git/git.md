1.取消跟踪某个文件

~~~~
# 忽略文件路径是相对于.gitignore文件
# .env 与.gitignore同级
git rm --cached ./.env 

git commit -m "Remove file from tracking"
~~~~

