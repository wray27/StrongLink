az login --service-principal -u $AZ_APP_URL -p $AZ_APP_SECRET --tenant $AZ_TENANT_ID
az iot hub device-identity connection-string show --device-id $DEVICE_ID --hub-name $AZ_IOT_HUB
export IOTHUB_DEVICE_CONNECTION_STRING="$(az iot hub device-identity connection-string show --device-id $DEVICE_ID \
    --hub-name StrongLink-IoT-Hub | python3 -c "import sys, json; print(json.load(sys.stdin)['connectionString'])")"
python3 simulation.py