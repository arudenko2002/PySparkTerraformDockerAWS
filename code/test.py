# {     "Version": "2012-10-17",
#       "Statement": {
#           "Effect": "Allow",
#           "Action": "s3:GetObject",
#           "Resource": "arn:aws:s3:::example-bucket/file.txt"     }
#       }
# try:
s = {    "Version": "2012-10-17",
             "Statement": [        {            "Effect": "Allow",
                                                "Action": "s3:GetObject",
                                                "Resource": "arn:aws:s3:::example-bucket/file.txt"
                                                },
                                   {            "Effect": "Deny",            "Action": "s3:DeleteObject",
                                                "Resource": "arn:aws:s3:::example-bucket/file.txt"
                                                },        {            "Effect": "Allow",
                                                                       "Action": "s3:ListBucket",
                                                                       "Resource": "arn:aws:s3:::example-bucket"
                                                }    ]}
def function(s):
    print("THROUGH")
    for policy in s["Statement"]:
        if (policy["Effect"]=="Allow" and
                policy["Action"] == "s3:GetObject" and
                policy["Resource"] ==  "arn:aws:s3:::example-bucket/file.txt"):
            return "this file can be read"
    return "this file cannot be read"

print(function(s))

a = ["a","b","c"]
if "a" in a:
    print("A")

if "b" in a:
    print("B")

if "c" in a:
    print("C")

if "d" in a:
    print("D")
else:
    print("NO D")