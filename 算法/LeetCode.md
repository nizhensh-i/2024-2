滚动数组思想  ==> 使空间复杂度降为O(1)

~~~ 
int p = 0, q = 0, r = 1;
for (int i = 2; i <= n; ++i) {
    p = q; 
    q = r; 
    r = p + q;
}

~~~

