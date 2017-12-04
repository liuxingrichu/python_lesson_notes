£¨1£©When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.

cigar_party(30, False) ¡ú False

cigar_party(50, False) ¡ú True

cigar_party(70, True) ¡ú True

´ğ°¸£º
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)
	
£¨2£©You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, 
and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, 
then the result is 0 (no). Otherwise the result is 1 (maybe).

date_fashion(5, 10) ¡ú 2

date_fashion(5, 2) ¡ú 0

date_fashion(5, 5) ¡ú 1

´ğ°¸£º
def date_fashion(you, date):
  ## Check the <=2 case first, since it takes precedence
  ## over the >=8 case.
  if (you <= 2) or (date <= 2):
    return 0
  elif (you >= 8) or (date >= 8):
    return 2
  else:
    return 1