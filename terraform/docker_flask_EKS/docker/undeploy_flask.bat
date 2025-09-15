@REM aws ecr batch-get-image --repository-name flask-app ^
@REM --image-ids imageTag=latest ^
@REM --region us-east-1

@REM aws ecr batch-delete-image --repository-name flask-app ^
@REM --image-ids imageTag=latest imageDigest=sha256:29634942d30aa196d152aa68ac73b9f773ec28840b4136ac426309859cc0273e ^
@REM --region us-east-1

aws ecr delete-repository ^
    --repository-name flask-app ^
    --region us-east-1 ^
    --force
@REM terraform destroy

