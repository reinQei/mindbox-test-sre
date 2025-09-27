import subprocess
from time import sleep


if __name__ == "__main__":
    print("Установка тестового стенда:")
    subprocess.run(["kubectl", "apply", "-f", "test-deploy.yml"], check=True)
    sleep(1)

    print("Все ноды в кластере:")
    subprocess.run(["kubectl", "get", "nodes", "-o", "wide"], check=True)
    sleep(1)

    print("Все поды:")
    subprocess.run(["kubectl", "get", "pods", "-o", "wide"], check=True)
    sleep(1)