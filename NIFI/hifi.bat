cd C:\Users\AlexR\NiFi\nifi-2.5.0-bin\nifi-2.5.0\bin
.\nifi.cmd start
vi ..\logs\nifi-app.log
vi ..\config\nifi.properties
@REM nifi.remote.input.secure=false
@REM nifi.web.http.host=localhost
@REM nifi.web.http.port=9090
@REM
@REM # HTTPS must be disabled:
@REM nifi.web.https.port=
@REM nifi.web.https.host=

netstat -aon | findstr :9090