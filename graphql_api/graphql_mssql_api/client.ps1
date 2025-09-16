$headers = @{
  "Content-Type" = "application/json"
}

$body = @{
  query = "{ books { id title } }"
} | ConvertTo-Json -Compress

$response = Invoke-RestMethod -Uri "http://localhost:4000/graphql" -Method Post -Headers $headers -Body $body

$response.data.books | Format-Table

$response | ConvertTo-Json -Depth 10


$body = @{
  query = "{ authors { id name } }"
} | ConvertTo-Json -Compress

$response = Invoke-RestMethod -Uri "http://localhost:4000/graphql" -Method Post -Headers $headers -Body $body

$response.data.authors | Format-Table

$response | ConvertTo-Json -Depth 10