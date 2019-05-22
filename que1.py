'''
题目描述
输入两个字母串，将两个字母串都包含的字母用'_'替换后，输出两个字母串的剩余部分。
输入描述:
输入两个字符串，字符串最大长度为100。字符串只包含字母，不可能为空串，区分大小写。
输出描述:
按字符串顺序输出处理后的字符串
示例1
输入
abcd
bdef
输出
a_c_ 
__ef
'''
str1=input()
str2=input()
for i in str1:
	for j in str2:
		if i==j:
			str1=str1.replace(i,'_')
			str2=str2.replace(i,'_')
			
print(str1)
print(str2)

'''
def run():

    str1=input('第一组字符串:')

    str2=input('第二组字符串:')

    if len(str1)>100 or len(str2)>100:

        print('请输入长度不超过100的字符串')

        return False

    elif str1=="" or str2=="":

        print('字符串不能为空')

        return False

    elif not str1.isalpha() or not str2.isalpha():

        print('请输入只包含字母的字符串')

        return False

    comment_list = set(str1).intersection(str2)

    for row in comment_list:

        str1 = str1.replace(row,'_')

        str2 = str2.replace(row,'_')

    print('相同的字母:{0}'.format(comment_list))

    print(str1)

    print(str2)

    return True

run()
'''
