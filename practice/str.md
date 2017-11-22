��1��Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') �� 'lloHe'

left2('java') �� 'vaja'

left2('Hi') �� 'Hi'

�𰸣�
def left2(str):
    return "{}{}".format(str[2:], str[:2])
	

��2��Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') �� 1

count_code('codexxcode') �� 2

count_code('cozexxcope') �� 2	

�𰸣�
	��
	
----------------------------------------------------
count_code('aaacodebbb') �� 1	1	OK	
count_code('codexxcode') �� 2	2	OK	
count_code('cozexxcope') �� 2	2	OK	
count_code('cozfxxcope') �� 1	0	X	
count_code('xxcozeyycop') �� 1	2	X	
count_code('cozcop') �� 0	0	OK	
count_code('abcxyz') �� 0	0	OK	
count_code('code') �� 1	1	OK	
count_code('ode') �� 0	0	OK	
count_code('c') �� 0	0	OK	
count_code('') �� 0	0	OK	
count_code('AAcodeBBcoleCCccoreDD') �� 3	3	OK	
count_code('AAcodeBBcoleCCccorfDD') �� 2	3	X	
count_code('coAcodeBcoleccoreDD') �� 3	0	X	
----------------------------------------------------

	