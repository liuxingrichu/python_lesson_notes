（1）Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') → 'lloHe'

left2('java') → 'vaja'

left2('Hi') → 'Hi'

答案：
def left2(str):
    return "{}{}".format(str[2:], str[:2])
	

（2）Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1

count_code('codexxcode') → 2

count_code('cozexxcope') → 2	

答案：
def count_code(str):
  count = 0
  if "co" not in str:
    return count
  pos = str.index("co")
  if len(str) < pos + 4:
    return count
  str = str.lower()
  count = str.count("coae") +  str.count("cobe") + str.count("coce") +\
        str.count("code") +  str.count("coee") + str.count("cofe") + \
        str.count("coge") +  str.count("cohe") + str.count("coie") +\
        str.count("coje") +  str.count("coke") + str.count("cole") + \
        str.count("come") +  str.count("cone") + str.count("cooe") + \
        str.count("cope") +  str.count("coqe") + str.count("core") +\
        str.count("cose") +  str.count("cote") + str.count("coue") + \
        str.count("cove") +  str.count("cowe") + str.count("coxe") + \
        str.count("coye") +  str.count("coze")
  return count	

测试用例：  
----------------------------------------------------
count_code('aaacodebbb') → 1	1	OK	
count_code('codexxcode') → 2	2	OK	
count_code('cozexxcope') → 2	2	OK	
count_code('cozfxxcope') → 1	0	X	
count_code('xxcozeyycop') → 1	2	X	
count_code('cozcop') → 0	0	OK	
count_code('abcxyz') → 0	0	OK	
count_code('code') → 1	1	OK	
count_code('ode') → 0	0	OK	
count_code('c') → 0	0	OK	
count_code('') → 0	0	OK	
count_code('AAcodeBBcoleCCccoreDD') → 3	3	OK	
count_code('AAcodeBBcoleCCccorfDD') → 2	3	X	
count_code('coAcodeBcoleccoreDD') → 3	0	X	
----------------------------------------------------


（3）Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True

end_other('AbC', 'HiaBc') → True

end_other('abc', 'abXabc') → True

答案：
def end_other(a, b):
	a = a.lower()
	b = b.lower()
	return (b.endswith(a) or a.endswith(b))

	
（4）Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True

xyz_there('abc.xyz') → False

xyz_there('xyz.abc') → True	

答案：
def xyz_there(str):
  if "xyz" not in str:
    return False
  if str.count("xyz") == str.count(".xyz"):
    return False
  return True