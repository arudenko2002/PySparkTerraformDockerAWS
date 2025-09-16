@REM Linux version
@REM curl https://api.openai.com/v1/chat/completions \
@REM   -H "Authorization: Bearer YOUR_API_KEY" \
@REM   -d '{
@REM     "model": "gpt-4",
@REM     "messages": [{"role": "user", "content": "Write a Dockerfile for a Flask app."}]
@REM   }'

@REM You must pay for this service, get right bearer
@REM curl https://api.openai.com/v1/chat/completions ^
@REM   -H "Content-Type: application/json" ^
@REM   -H "Authorization: ^
@REM   -d "{\"model\": \"gpt-3.5-turbo\", \"messages\": [{\"role\": \"user\", \"content\": \"Hello!\"}]}"