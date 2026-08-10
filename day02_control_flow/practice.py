total_pods = 16
pods_per_node = 4

normal_division = total_pods / pods_per_node
fully_occupied_nodes = total_pods // pods_per_node
remaining_pods = total_pods % pods_per_node

print(normal_division)
print(fully_occupied_nodes)
print(remaining_pods)

required_nodes = fully_occupied_nodes

if remaining_pods > 0:
    required_nodes = required_nodes + 1

print(f"Required nodes: {required_nodes}")

print("\n--- CPU Health Check ---")

cpu_usage = int(input("Enter CPU usage percentage: "))

if cpu_usage >= 90:
    status = "CRITICAL"
elif cpu_usage >= 70:
    status = "WARNING"
else:
    status = "HEALTHY"

print(f"CPU usage: {cpu_usage}%")
print(f"Status: {status}")


print("\n--- Deployment Authorization ---")

tests_passed = True
approval_received = False
emergency_change = False
deployment_frozen = True

can_deploy = (
    tests_passed
    and (approval_received or emergency_change)
    and not deployment_frozen
)

print(f"Can deploy: {can_deploy}")

print("\n--- Multiple CPU Checks ---")

cpu_readings = [40, 75, 95]

for cpu_usage in cpu_readings:
    if cpu_usage >= 90:
        status = "CRITICAL"
    elif cpu_usage >= 70:
        status = "WARNING"
    else:
        status = "HEALTHY"

    print(f"CPU: {cpu_usage}% | Status: {status}")

print("All CPU checks completed")  

print("\n--- Deployment Retry Attempts ---")

for attempt in range(1, 4):
    print(f"Running deployment attempt: {attempt}")

print("Maximum attempts completed")

print("\n--- Health Check Retry ---")

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print(f"Health check attempt: {attempt}")
    attempt = attempt + 1

print("Health check retries completed")
print(f"Final attempt value: {attempt}")

print("\n--- Controlled Deployment Attempts ---")

for attempt in range(1, 6):
    if attempt == 2:
        print("Attempt 2 skipped: maintenance activity detected")
        continue

    if attempt == 4:
        print("Attempt 4 succeeded")
        break

    print(f"Attempt {attempt} failed")

print("Deployment loop finished")