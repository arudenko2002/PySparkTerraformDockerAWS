param($url)
#$url=1022310736
$q1="http://ollama-alb-$url.us-east-1.elb.amazonaws.com"
echo $q1
curl.exe $q1
$q1="http://ollama-alb-$url.us-east-1.elb.amazonaws.com/generate?prompt=Hello+World"
echo $q1
curl.exe $q1
$q1 = "http://ollama-alb-$url.us-east-1.elb.amazonaws.com/generate?prompt=hat+is+the+capital+of+France"
echo $q1
curl.exe $q1
$q1 = "http://ollama-alb-$url.us-east-1.elb.amazonaws.com/generate?prompt=who+is+us+president"
echo $q1
curl.exe $q1
$q1 = "http://ollama-alb-$url.us-east-1.elb.amazonaws.com/generate?prompt=who+is+Donald+Trump"
echo $q1
curl.exe $q1
$q1 = "http://ollama-alb-$url.us-east-1.elb.amazonaws.com/generate?prompt=who+is+Leonardo+da+Vinci"
echo $q1
curl.exe $q1