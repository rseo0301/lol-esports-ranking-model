#!/bin/bash
# This script will build the Docker image for data_cleaner and upload it to aws ECR
docker build -t riot-hackathon-api -f ./Dockerfile ..
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/m4w6d1r1
docker build -t riot-hackathon-api .
docker tag riot-hackathon-api:latest public.ecr.aws/m4w6d1r1/riot-hackathon-api:latest
docker push public.ecr.aws/m4w6d1r1/riot-hackathon-api:latest