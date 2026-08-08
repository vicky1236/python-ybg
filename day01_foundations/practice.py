service_name = "buddybot"
replicas = 3
desired_replicas = replicas

replicas = replicas + 2

cpu_limit = 0.5
is_healthy = True
last_error = None

print(f"Service: {service_name}")
print(f"Current replicas: {replicas}")
print(f"Original desired replicas: {desired_replicas}")

print(type(service_name))
print(type(cpu_limit))
print(type(is_healthy))
print(type(last_error))

print("\n--- Mutable List Test ---")

running_pods = ["buddybot-1", "buddybot-2"]
backup_pods = running_pods.copy()

running_pods.append("buddybot-3")

print(f"Running pods: {running_pods}")
print(f"Backup pods: {backup_pods}")
print(f"Same object: {running_pods is backup_pods}")