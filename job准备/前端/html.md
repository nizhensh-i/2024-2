# <link rel="stylesheet" href="/css/pure/pure-min.css">



<link> 标签是用来引入外部资源的，其中 rel 属性指定了所引入资源的类型，href 属性指定了资源的路径。
在这个例子中，rel 属性的值为 "stylesheet"，表示引入的是一个样式表文件。href 属性的值为 "build/pure-min.css"，表示样式表文件的路径为 build/pure-min.css。
需要注意的是，这个路径是相对于当前 HTML 文件的路径。如果样式表文件和 HTML 文件不在同一个文件夹下，那么需要在路径中加上相应的文件夹名。
另外，<link> 标签中还可以使用 type 属性来指定所引入资源的 MIME 类型，但是对于样式表文件来说，通常不需要指定该属性，因为浏览器会自动识别样式表文件的 MIME 类型。



菜单栏变成折叠的图标：

~~~~
function toggleClass(element, className) {
        var classes = element.className.split(/\s+/);
        var length = classes.length;
        var i = 0;

        for (; i < length; i++) {
            if (classes[i] === className) {
                classes.splice(i, 1);
                break;
            }
        }
        // The className is not found
        if (length === classes.length) {
            classes.push(className);
        }

        element.className = classes.join(' ');
    }

~~~~

说白了，这个函数干了一件事，在指定元素class中加上active；若已经有了active，则移除active



移动屏幕下：

点击汉堡图标，对汉堡图标，侧边栏，布局 的class属性加上 “active”，此时会触发css样式，使侧边栏出现，布局右移，汉堡图标隐藏。

再次点击出现的侧边栏中菜单项时，会移除侧边栏，布局 的class属性的 “active”，使之恢复到只有汉堡图标。





~~~

  .menu-link span,
    .menu-link span:before,
    .menu-link span:after {
        background-color: #fff;
        pointer-events: none;
        width: 100%;
        height: 0.2em;
    }
~~~



~~~
#menu {
    margin-left: -150px; /* "#menu" width */
    width: 150px;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    z-index: 1000; /* so the menu or its navicon stays above all content */
    background: #191818;
    overflow-y: auto;
}

# 通过position： fixed 将菜单栏固定在左侧
# 通过 margin-left: -150px 使的位置初始是在屏幕之外。后面使用left: 150;正好放在左边栏开始
~~~





~~~
.menu-link {
    position: fixed;
    display: block; /* show this only on small screens */
    top: 0;
    left: 0; /* "#menu width" */
    background: #000;
    background: rgba(0,0,0,0.7);
    font-size: 10px; /* change this value to increase/decrease button size */
    z-index: 10;
    width: 2em;
    height: auto;
    padding: 2.1em 1.6em;
}
# 通过.menu-link中的display: block; ，在小屏幕时会显示出来


@media (min-width: 48em) {

    .header,
    .content {
        padding-left: 2em;
        padding-right: 2em;
    }

    #layout {
        padding-left: 150px; /* left col width "#menu" */
        left: 0;
    }
    #menu {
        left: 150px;
    }

    .menu-link {
        position: fixed;
        left: 150px;
        display: none;
    }

    #layout.active .menu-link {
        left: 150px;
    }
}
# 通过 .menu-link中的display: none;，在大屏幕上不显示toggle

~~~

# CSS动画

1.理解animation-delay负值

animation-delay: .25s  表示动画在0.25s之后从0%开始播放，

animation-delay: -.25s  表示在0.25s之前就已经从0%开始播放，即动画真正播放的时候动画已经执行了0.25s



2.reverse和alternate关键字的区别和应用

 reverse关键字 是让每一轮动画执行的方向相反

 而alternate关键字 是让下一轮动画的执行方向和上一轮动画的执行方向相反。

~~~
normal，0%→100%、0%→100%，

reverse，100%→0%、100%→0%，每一轮的动画方向都是相反的。

 alternate，0%→100%、100%→0%，每2n+1轮的动画方向是相反的。

alternate-reverse，100%→0%，0%→100%，每轮的动画方向是相反的。
~~~

3.animation-iteration-coun 动画播放次数可以是小数

~~~
.element {
    animation: fadeIn 1s linear both;
    animation-iteration-count: 1.5;
}
@keyframes fadeIn {
    0%   { opacity: 0; }
    100% { opacity: 1; }
}
# 动画播放的进度为0%→100%、0%→50%，也就是在第二轮播放的时候，播放到一半就会停止，此时元素的透明度是0.5
~~~

应用： 用淡出的动画来实现元素处于禁用态

 3.1.页面中有些元素处于禁用态，透明度只有40%，此时，使用完整的fadeIn动画就不合适

解决：对于ease时间函数，透明度提高到40%只需要25%的完整动画时间，因此，我们只需要播放`0.25次`即可

~~~
.visible:disabled {
    animation: fadeIn 1s .25 both;
}
~~~

3.2 只希望使用淡出动画的后半截

则使用animation-iteration-count小数值的方法就不管用了。此时可以使用animation-delay负属性值实现我们想要的效果

~~~
.visible-second-half {
    animation: fadeIn 1s -.25s;
}
~~~

3.3 使用淡出动画的中间部分

同时使用animation-iteration-count小数值和animation-delay负时间值

~~~
# 选取中间50%的时间区域：
.visible-middle-part {
    animation: fadeIn 1s -.25s .75;
}
~~~

注意：值不能是负数，否则会被认为不合法，但是可以是0，表示动画一次也不播放。

因此，如果想要重置animation属性，可以使用animation:0，比使用animation: none 的代码少。



# 暂停和重启CSS动画

暂停： 

~~~
/* 播放 */
animation-play-state: running;
/* 暂停 */
animation-play-state: paused;
~~~

重启：

使用下面的JavaScript代码

~~~
ele.classList.remove('active');
ele.offsetWidth;    // 触发重绘
ele.classList.add('active');
~~~

# 深入理解steps()函数

animation-timing-function  的属性值由cubic- bezier()函数和steps()函数组成。

steps()函数可以让动画效果不连续，就像楼梯；而cubic-bezier()函数，则更像是平滑的无障碍坡道

~~~
steps(number, position)

# number指数值，且是整数值。表示把动画分成了多少段
# position指关键字属性值，是可选参数，表示动画跳跃执行是在时间段的开始还是结束。
     start表示在时间段的开头处跳跃。 end表示在时间段的结束处跳跃，是默认值。
~~~

1.`一切都是反的。start不是开始，而是结束； end不是结束，而是开始。”`

  1.1 steps(5, start)应用的样式不是5个时间段的start样式，而是5个时间段的end样式，例如left:0到left:100px的位移，最 终元素表现出来的位移是20px、40px、60px、80px和100px。

![72396606572](C:\Users\19125\Desktop\2024-2月面试\job准备\前端\html.assets\1723966065722.png)



  1.2 steps(5, end)应用的是5个时间段的start样式，而是5个时间段的start样式，例如left:0到left:100px的位移，最终元素表现出来的位移是0px、20px、40px、60px和80px。

![72396611526](C:\Users\19125\Desktop\2024-2月面试\job准备\前端\html.assets\1723966115264.png)



1.3 step-start和step-end

   step-start等同于steps(1, start)，表示“一步到位”；

   step-end等同于steps(1, end)或者steps(1)，表示“延时到位”。

  可以让动画按照设定的关键帧步进变化，特别适合非等分的步进场景。例如实现一个打点动画

# forwards和backwards属性

1.语法

~~~
animation-fill-mode: none;    /* 默认值 */
animation-fill-mode: forwards;
animation-fill-mode: backwards;
animation-fill-mode: both;
~~~

2.forwards是“前进”的意思，表示`动画结束后`元素将应用当前动画结束时的属性值（什么时候结束由animation-iteration- count属性决定）

backwards是“后退”的意思，表示在`动画开始之前`，元素将应用当前动画第一轮播放的第一帧的属性值

（forwards指动画向前，backwards指动画向后）

![72398196230](C:\Users\19125\Desktop\2024-2月面试\job准备\前端\html.assets\1723981962302.png)



3.animation-fill-mode: both  可以让元素的动画在延时等待时保持第一帧的样式，在动画结束后保持最后一帧的样式。

  适用于绝大多数的开发场景





