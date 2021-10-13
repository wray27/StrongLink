echo $AZ_APP_URL
az login --service-principal -u $AZ_APP_URL -p $AZ_APP_SECRET --tenant $AZ_TENANT_ID --allow-no-subscriptions
az account show
az iot hub device-identity create --hub-name $AZ_IOT_HUB --device-id $DEVICE_ID