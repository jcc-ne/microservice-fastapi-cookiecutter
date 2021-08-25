.PHONY: run gcloud-deploy-dev gcloud-deploy-prod
rootdir = $(realpath .)

run:
	@cd app_pkg/ && python main.py

gcloud-deploy-dev:
	@cd app_pkg/ && gcloud app deploy app.yaml

gcloud-deploy-prod:
	@cd deploy/ && ./deploy.sh
