# from ctypes import pythonapi
#
#
# @app.route("/")
# def function(args):
#     response = args
#     answer="answer"
#     return {response: answer}
#
# int float string list dict set

s = "python"
s1 = s[:len(s)-1]
s2 = list(s1)
s3 = s2.pop()
print("s2=",s2)
print("s3=",s3)
print("".join(s2))
print("".join(s3))
