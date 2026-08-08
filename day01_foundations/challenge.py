engineer_name = input("Enter engineer name: ")
service_name = input("Enter service name: ")
environment_name = input("Enter environment name: ")
current_replicas = int(input("Enter current replicas: "))
desired_replicas = int(input("Enter desired replicas: "))
cpu_per_replica = float(input("Enter CPU per replica: "))


replicas_to_add = desired_replicas - current_replicas
total_required_cpu = desired_replicas * cpu_per_replica

print("\n=== Deployment Profile ===")
print(f"Engineer: {engineer_name}")
print(f"Service: {service_name}")
print(f"Environment: {environment_name}")
print(f"Current replicas: {current_replicas}")
print(f"Desired replicas: {desired_replicas}")
print(f"Replicas to add: {replicas_to_add}")
print(f"CPU per replica: {cpu_per_replica} cores")
print(f"Total required CPU: {total_required_cpu} cores")
