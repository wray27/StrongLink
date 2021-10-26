from azure.cli.core import get_default_cli

for i in range(1, 9):
    get_default_cli().invoke(['iot', 'hub', 'device-identity', 'create', '--hub-name', 'StrongLink-Iot-Hub', '--device-id', f'Truck-000{i}'])