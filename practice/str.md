£¨1£©Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') ¡ú 'lloHe'

left2('java') ¡ú 'vaja'

left2('Hi') ¡ú 'Hi'

´ð°¸£º
def left2(str):
    return "{}{}".format(str[2:], str[:2])
	

£¨2£©Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') ¡ú 1

count_code('codexxcode') ¡ú 2

count_code('cozexxcope') ¡ú 2	

´ð°¸£º
	ÎÞ
	
----------------------------------------------------
count_code('aaacodebbb') ¡ú 1	1	OK	
count_code('codexxcode') ¡ú 2	2	OK	
count_code('cozexxcope') ¡ú 2	2	OK	
count_code('cozfxxcope') ¡ú 1	0	X	
count_code('xxcozeyycop') ¡ú 1	2	X	
count_code('cozcop') ¡ú 0	0	OK	
count_code('abcxyz') ¡ú 0	0	OK	
count_code('code') ¡ú 1	1	OK	
count_code('ode') ¡ú 0	0	OK	
count_code('c') ¡ú 0	0	OK	
count_code('') ¡ú 0	0	OK	
count_code('AAcodeBBcoleCCccoreDD') ¡ú 3	3	OK	
count_code('AAcodeBBcoleCCccorfDD') ¡ú 2	3	X	
count_code('coAcodeBcoleccoreDD') ¡ú 3	0	X	
----------------------------------------------------

	