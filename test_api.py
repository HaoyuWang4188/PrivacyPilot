import requests

BASE_URL = "http://localhost:8000"

TEST_DATA_CODE = """
import platform
import subprocess
import numpy
system = platform.system()
if system == "Windows":
    model = platform.processor()
elif system == "Linux":
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                model = line.split(":")[1].strip()
elif system == "Darwin":  # macOS
    model = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True).stdout.strip()
else:
    model = "Unsupported platform"
print("[MODEL]", model)
"""

def test_cpu_endpoint():
    response = requests.get(f"{BASE_URL}/cpu")
    if response.status_code == 200:
        data = response.json()
        print("CPU Usage:", data)
    else:
        print("Failed to get CPU info. Status code:", response.status_code)

def test_disk_endpoint():
    response = requests.get(f"{BASE_URL}/disk")
    if response.status_code == 200:
        data = response.json()
        print("Disk Usage:", data)
    else:
        print("Failed to get disk info. Status code:", response.status_code)

def test_manifest_endpoint():
    response = requests.get(f"{BASE_URL}/manifest.json")
    if response.status_code == 200:
        data = response.json()
        print("API Manifest:")
        print(data["name"])
    else:
        print("Failed to get manifest. Status code:", response.status_code)

def test_python_interpreter_endpoint():
    response = requests.post(
        url=f"{BASE_URL}/python_interpreter", 
        data={"input_code": TEST_DATA_CODE})
    if response.status_code == 200:
        data = response.json()
        print("API Python Interpreter:")
        print(data)
    else:
        print("Failed to execute code. Status code: ", response.status_code)

def main():
    print("Testing CPU endpoint:")
    test_cpu_endpoint()
    print("\nTesting Disk endpoint:")
    test_disk_endpoint()
    print("\nTesting Manifest endpoint:")
    test_manifest_endpoint()
    print("\nTesting Interpreter endpoint:")
    test_python_interpreter_endpoint()

if __name__ == "__main__":
    main()
