regex_integer_in_range = r"^[7,8,9][0-9]{9}$"	# Do not delete 'r'.
reg = r"^[A-z][A-z,-,_,.]*"
reg=r"[-a-zA-Z0-9@:%._\+~#=].[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)"
reg=r"^[a-zA-Z][a-zA-Z0-9-_.]*@[/w].[/w]"
reg=r"^[a-zA-Z]([a-zA-Z0-9_\-\.]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})$"

#reg="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"

# (\d): Match and capture a digit in group #1
# (?=: Start lookahead
# \d: Match any digit
# \1: Back-reference to captured group #1
# ): End lookahead

import re

ss = ["DEXTER <dexter@hotmail.com>",
"VIRUS <virus!@variable.:p>",
"AAA <a@b>"]

sss = """dheeraj <dheeraj-234@gmail.com>
crap <itsallcrap>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
mattp <matt23@@india.in>
harsh <.harsh_1234@rediff.in>
harsh <-harsh_1234@rediff.in>"""

# sss = """vineet <vineet.iitg@gmail.com>
# vineet <vineet.iitg@gmail.co>
# vineet <vineet.iitg@gmail.c>"""
#
# sss = """this <is@valid.com>
# this <is_som@radom.stuff>
# this <is_it@valid.com>
# this <_is@notvalid.com>"""
#
# sss = """vin <vineet@>
# vineet <vineet@gmail.com>
# vineet <vineet@gma.il.co.m>
# vineet <vineet@gma-il.co-m>
# vineet <vineet@gma,il.co@m>
# vineet <vineet@gmail,com>
# vineet <.vin@gmail.com>
# vineet <vin-nii@gmail.com>
# vineet <v__i_n-n_ii@gmail.com>"""

# sss="""shashank <shashank@9mail.com>
# shashank <shashank@gmail.9om>
# shashank <shashank@gma_il.com>
# shashank <shashank@mail.moc>
# shashank <shashank@company-mail.com>
# shashank <shashank@companymail.c_o>"""
ss = sss.split("\n")
ss = [x+"\n" for x in ss]
for p in ss:
    s = p.split()[1][1:-1]
    if bool(re.match(reg, s)):
        print(p,end="")
    #print(bool(re.match(reg, s)))