from sstack import *

text = '''
The manatees are attracted to (the warm coastal waters around Florida thanks to the abundance of) naturally occurring hot springs. They once gathered here in their thousands, but during the last century manatee numbers started to dramatically decline.

This was because {humans were [also attracted to the (abundant) delights of the Sunshine] State and a massive period of development began}. Homes were built and hotels erected. Millions flocked to the area, much like the manatees.

'''
parens = "()[]{}"  # 验证的括号
left_parens = "([{"
opposite = {
    ')': '(',
    ']': '[',
    '}': '{'
}  # 对应关系


# 生成器
def parent(text):
    # i记录字符串索引
    i, text_len = 0, len(text)
    while True:
        # 逐个遍历字符串，如果没到结尾并且不是括号，就向后遍历
        while i < text_len and text[i] not in parens:
            i += 1
        if i >= text_len:
            return
        else:
            yield text[i], i  # 生成括号字符和对应位置
            i += 1


st = SStack()
for pr, i in parent(text):
    if pr in left_parens:
        st.push((pr, i))  # 将左括号及其位置入栈
    elif st.is_empty() or st.pop()[0] != opposite[pr]:
        print("Unmatching is found at %d for %s" % (i, pr))
        break
else:
    # 循环正常结束，判断栈是否为空
    if st.is_empty():
        print("All parentheses are matched")
    else:
        # 有左括号没有匹配
        e = st.pop()
        print("Unmatching is found at %d for %s" % (e[1], e[0]))
