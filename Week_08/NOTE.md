学习笔记
第八周 第16课 位运算
为什么需要位运算: 机器里的数字表示方式和存储格式就是二进制
位运算符: 按位或 | ，按位与 &, 按位取反 ~, 按位异或 ^--相同为0，不同为1
异或操作的特点：
x^0 = x
x^1s = ~x  1s = ~0
x^(~x) = 1s
x^x = 0
c = a^b => a^c = b, b^c =a //交换两个数
a^b^c = a^(b^c)=(a^b)^c //结合法

指定位置的位运算
1. 将x最右边的n位清零：x&(~0<<n)
2. 获取x的第n位值(0或者1)： (x>>n)&1
3. 获取x的第n位的幂值：x&(1<<n)
4. 仅将第n位置为1：x|(1<<n)
5. 仅将第n位置为0：x&(~(1<<n))
6. 将x最高位至第n位(含)清零: x&((1<<n)-1)

实战位运算要点
1. 判断奇偶
x % 2 == 1 -->(x&1)==1
x % 2 == 0 -->(x&1)==0

2. x>>1 -->x/2 即x=x/2; --> x=x>>1;
   mid = (left +right)/2; -->mid=(left+right) >> 1;

3. X=X&(X-1) 清零最低位的1
4. X&-X => 得到最低位的1
5. X&~X => 0

Day 57
https://leetcode-cn.com/problems/permutations/

Day 58:
https://leetcode-cn.com/problems/number-of-1-bits/

Day 59:
https://leetcode-cn.com/problems/relative-sort-array/

Day 60:
https://leetcode-cn.com/problems/lru-cache/#/

Day 61:
https://leetcode-cn.com/problems/power-of-two/
1. 若n=2^x 且 x 为自然数(即n为2的幂)，则一定满足一下条件：
   1）恒有 n&(n-1) == 0, 这是因为： n二进制最高位为1， 其余所有位为0， n-1二进制最高位为0，其余所有位为1
   2）一定满足 n > 0
