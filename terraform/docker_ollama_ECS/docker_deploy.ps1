aws ecr create-repository --repository-name ollama-api --no-cli-pager
docker build -t ollama-api .
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 917819970045.dkr.ecr.us-east-1.amazonaws.com
docker tag ollama-api:latest 917819970045.dkr.ecr.us-east-1.amazonaws.com/ollama-api:latest
docker push 917819970045.dkr.ecr.us-east-1.amazonaws.com/ollama-api:latest
exit
# docker build -t ollama-api .
# curl http://127.0.0.1:11434/api/tags
# ollama pull llama3


# Invoke-RestMethod -Uri "http://localhost:11434/api/generate" `
#      -Method Post `
#      -ContentType "application/json" `
#      -Body '{ "model": "llama3", "prompt": "Hello from host outside Docker", "stream": false }'

# docker run -it --rm ollama-api bash
# which ollama
# ls -lh /usr/local/bin/ollama
# ollama serve

# http://ollama-alb-2044797842.us-east-1.elb.amazonaws.com/generate?prompt=Hello+World

#curl.exe -X POST "http://ollama-alb-1219227329.us-east-1.elb.amazonaws.com/api/generate" -H "Content-Type: application/json" -d "{\"model\": \"llama3\", \"prompt`\": \"Hello World\"}"



# curl.exe -X POST "http://ollama-alb-1219227329.us-east-1.elb.amazonaws.com/generate" -H "Content-Type: application/json" -d "{`"model`": `"llama3`", `"prompt`": `"Hello World`"}"
#curl.exe -X POST "http://ollama-alb-1219227329.us-east-1.elb.amazonaws.com/generate" -H "Content-Type: application/json" -d "{\"model\": \"llama3\", \"prompt\": \"Hello World\"}"

# Invoke-RestMethod -Uri "http://ollama-alb-1219227329.us-east-1.elb.amazonaws.com/generate" `
#      -Method POST `
#      -ContentType "application/json" `
#      -Body '{ "prompt": "Hello from host outside Docker" }'

# aws elbv2 modify-target-group `
#   --target-group-arn arn:aws:elasticloadbalancing:us-east-1:917819970045:targetgroup/ollama-tg/fc30619a97c1ddcb `
#   --health-check-path "/generate" `
#   --health-check-protocol HTTP `
#   --health-check-port "8080"

# aws elbv2 modify-target-group `
#   --target-group-arn arn:aws:elasticloadbalancing:us-east-1:917819970045:targetgroup/ollama-tg/fc30619a97c1ddcb `
#   --health-check-path "/healthz" `
#   --health-check-protocol HTTP `
#   --health-check-port "8080" `
#   --matcher HttpCode=200

# aws logs tail /ecs/ollama-api --follow


aws ecs update-service `
  --cluster ollama-cluster `
  --service ollama-service `
  --force-new-deployment

 aws ecs describe-tasks `
  --cluster ollama-cluster `
  --tasks arn:aws:ecs:us-east-1:917819970045:task/ollama-cluster/fa0d45b6f7754a3e95038e9b057977c5

  aws elbv2 describe-target-groups --query 'TargetGroups[].[TargetGroupName, TargetGroupArn]' --output table
  terraform output
  terraform show | findstr arn:aws:elasticloadbalancing

  aws elbv2 describe-target-health --target-group-arn arn:aws:elasticloadbalancing:us-east-1:917819970045:targetgroup/ollama-tg/a2d5df8e56bab104

  aws elbv2 describe-load-balancers `
  --names ollama-alb `
  --query 'LoadBalancers[0].DNSName' `
  --output text
  # ollama-alb-1947541846.us-east-1.elb.amazonaws.com

  28266e8b2062

curl http://127.0.0.1:11434/api/generate -X POST \
  -H "Content-Type: application/json" \
  -d '{"model": "llama3", "prompt": "test", "stream": false}'

docker run -it --rm `
  -p 8080:8080 -p 11434:11434 `
  -v $HOME/.ollama/models:/root/.ollama/models `
  917819970045.dkr.ecr.us-east-1.amazonaws.com/ollama-api:latest /bin/sh

# start container
  docker run -it --rm `
  -p 8080:8080 -p 11434:11434 `
  -v $HOME/.ollama/models:/root/.ollama/models \
  917819970045.dkr.ecr.us-east-1.amazonaws.com/ollama-api:latest /bin/sh

  curl.exe -X POST http://127.0.0.1:11434/api/generate `
     -H "Content-Type: application/json" `
     -d '{ "model": "llama3:latest", "prompt": "Hello World", "stream": false }'