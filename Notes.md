**枚举型DFS** <br>
*以 425 Word Squares 为例* <br>
函数参数：
1. for 循环里【每一次recursion都需要更新】 <br>
   l: 记录当前位置的pointer <br>
   squares: 记录当前状态的list， 注意更新用 square + [item], 而不是square.append(),因为后者返回None,作为函数参数是无效的 <br>
   
2. 退出条件 <br>
   wordLen:终点位置，一般list、str的总长度；当l == wordLen 退出 <br>
   ans：记录所有可行的答案，退出之前ans.append(squares)

3. 记录冗余
   dic:hash table，查找o(1) <br>

临时变量：<br>
1. pre：记录当前的前缀，用于在dic中查找可行的单词 <br>
