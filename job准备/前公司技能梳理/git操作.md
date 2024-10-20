1. 将本机文件上传到GitHub上。

   1. git init   `(目录下只执行一次)`
   2. git add .
   3. git commit -m "描述"
   4. git remote add origin  远程网址
   5. git push -u origin master

2. 克隆远程的某个仓库

   git clone xx地址

3. 切换提交的历史

   git checkout 1a

   1a是某次提交历史的名称

4. 把改动的文件还原到最初状态

   git reset  --hard

5. 根据远程仓库更新本地仓库

   git fetch --all  ：根据远程仓库更新本地仓库的提交历史和标签，但不会真正改动源文件

   git reset --hard origin/master  :更新文件

6. 下载代码并且快速合并

   git pull origin master

7. 显示所有分支

   git banch

8. 切换到master分支

   git checkout master

9. 创建并切换到dev分支

   git checkout -b dev

10. 查看状态

    git status

11. 查看两个版本之前的差异

    git diff 2a 2b

12. 查看已关联的远程仓库地址

    git remote -v

13. 查看本地分支与远程分支的关联情况

    git branch -vv

14. 查看所有的分支情况(本地和远程)

    git branch -a

15. 将本地分支与远程分支关联

    git branch --set-upstream-to=origin/<远程分支名>

16. 将本地dev分支内容推送到远程test分支上

    git push origin dev:test