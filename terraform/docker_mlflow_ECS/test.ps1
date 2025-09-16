# uvicorn mlflow_api:app --reload --port 8080
#
# Invoke-WebRequest -Uri "http://127.0.0.1:8080/predict" `
#   -Method POST `
#   -Headers @{ "Content-Type" = "application/json" } `
#   -Body '{
#     "data": [
#       {
#         "MedInc": 8.3252,
#         "HouseAge": 41.0,
#         "AveRooms": 6.984126984,
#         "AveBedrms": 1.023809524,
#         "Population": 322.0,
#         "AveOccup": 2.555555556,
#         "Latitude": 37.88,
#         "Longitude": -122.23
#       }
#     ]
#   }'

#   aws ecr describe-images `
#   --repository-name mlflow-api `
#   --region us-east-1

# curl -X POST "http://127.0.0.1:8080/predict" `
#   -H "Content-Type: application/json" `
#   -d '{
#     "data": [{
#       "MedInc": 8.3252,
#       "HouseAge": 41.0,
#       "AveRooms": 6.984126984,
#       "AveBedrms": 1.023809524,
#       "Population": 322.0,
#       "AveOccup": 2.555555556,
#       "Latitude": 37.88,
#       "Longitude": -122.23
#     }]
#   }'

# param($url)
# $url=1222717065
# #echo "http://mlflow-alb-$url.us-east-1.elb.amazoanws.com/predict"
# curl.exe -X POST "http://mlflow-alb-$url.us-east-1.elb.amazoanws.com/predict" `
#   -H "Content-Type: application/json" `
#   -d '{"data":[{"MedInc":8.3252,"HouseAge":41.0,"AveRooms":6.984126984,"AveBedrms":1.023809524,"Population":322.0,"AveOccup":2.555555556,"Latitude":37.88,"Longitude":-122.23}]}'
#
  $body = @{
    data = @(@{
        MedInc = 8.3252
        HouseAge = 41.0
        AveRooms = 6.984126984
        AveBedrms = 1.023809524
        Population = 322
        AveOccup = 2.555555556
        Latitude = 37.88
        Longitude = -122.23
    })
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://mlflow-alb-1222717065.us-east-1.elb.amazonaws.com/predict" `
  -Method POST -Body $body -ContentType "application/json"