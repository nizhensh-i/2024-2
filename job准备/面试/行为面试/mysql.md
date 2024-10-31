# 数据库查询时对多个字段group by 有什么作用

比如：

~~~
GROUP BYstudent.SId, student.Sname
~~~

"group by 字段列表" 
表示根据后面的字段来分组,如果只有1个字段,那只是根据这个字段的值来进行一次分组就可以了；若后面有多个字段,那表示根据多字段的值来进行层次分组,分组层次从左到右,即先按第1个字段分组,然后在第1个字段值相同的记录中,再根据第2个字段的值进行分组；接着第2个字段值相同的记录中,再根据第3个字段的值进行分组.依次类推.



左外连接与内连接的区别：

左外连接的性能会比内连接稍差。

因为左外连接需要处理左表中没有在右表中匹配的记录（如下图，`多出5行` 用null填充了score字段。

![73022220888](C:\Users\19125\Desktop\2024-2月面试\job准备\面试\行为面试\mysql.assets\1730222208880.png)



~~~
---2
SELECT
    students.student_id,
    students.name,
    AVG(grades.score) AS average_score
FROM
    students
JOIN
    grades ON students.student_id = grades.student_id
GROUP BY
    students.student_id,
    students.name
HAVING
    AVG(grades.score) >= 60;



--3
select DISTINCT s.*
from student as s left join sc as c on s.SId = c.SId
where c.score is not null

--4
select s.SId,s.Sname,count(*) as '选课数量',sum(c.score) as '总成绩'
from student as s left join sc as c on s.SId = c.SId
group by s.SId,s.Sname


-- 4.1
select distinct s.*
from student as s inner join sc as c on s.SId = c.SId

-- 5
select count(*)
from teacher
where Tname like '李%'

-- 6
select DISTINCT s.*
from student as s 
inner join sc on s.SId = sc.SId
inner join course on sc.CId = course.CId
inner join teacher as t on course.TId = t.TId
where t.Tname = '张三'

--7 用子查询更清晰
select *
from student
where SId not in (select SId
              from sc
              group by SId
              having count(*)= (select count(*) from course));
              
-- 8
select *
from student
where SId in(select SId
             from sc
             where CId in(select CId
                          from sc
                          where SId ='01'));
~~~



在MySQL中，可以使用基本的数学运算符（加法 `+`，减法 `-`，乘法 `*`，除法 `/`）在 `SELECT` 语句中进行计算

- **使用 `CONCAT` 函数进行字符串连接**

  如果你想要将一个数值和字符串连接起来：

  ```sql
  SELECT CONCAT('Total price: ', (price + tax)) AS formatted_total_price
  FROM products;
  ```

- **使用 `ROUND` 函数进行四舍五入**

  如果你想要将计算结果四舍五入到小数点后两位：

  ```sql
  SELECT ROUND((price + tax), 2) AS rounded_total_price
  FROM products;
  ```

- **使用 `IF` 或 `CASE` 语句进行条件运算**

  假设你想根据某个条件对价格进行调整：

  ```sql
  SELECT price,
         IF(price < 50, price * 0.9, price) AS adjusted_price
  FROM products;
  ```

  或者使用 `CASE` 语句：

  ```sql
  SELECT price,
         CASE
           WHEN price < 50 THEN price * 0.9
           ELSE price
         END AS adjusted_price
  FROM products;
  ```

在上述示例中，你可以在 `SELECT` 语句中使用数学运算符和函数来解决各种业务逻辑问题，如计算税费、折扣、利润、平均值等。

