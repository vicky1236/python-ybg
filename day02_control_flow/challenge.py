service_name = input("Enter service name: ")
env_name = input("Enter environment name: ")
cpu_usage = int(input("Enter CPU usage percentage: "))
desired_replicas = int(input("Enter desired replicas: "))
tests_passed = input("Enter tests passed (yes or no): ") == "yes"
approval_received = input("Enter approval received (yes or no): ") == "yes"
deployment_frozen = input("Enter deployment frozen (yes or no): ") == "yes"

if deployment_frozen:
    decision = "BLOCKED"
    reason = "Deployment is frozen"
elif not tests_passed:
    decision = "BLOCKED"
    reason = "Tests failed"
elif cpu_usage >= 90:
    decision = "BLOCKED"
    reason = "High CPU usage"
elif env_name == "prod" and not approval_received:
    decision = "BLOCKED"
    reason = "Production approval was not received"
else:
    decision = "APPROVED"
    reason = "All conditions met for deployment"

print("\n=== Deployment Decision ===")
# Print service, environment, decision, and reasonprint(f"Service: {service_name}")
print(f"Service: {service_name}")
print(f"Environment: {env_name}")
print(f"Decision: {decision}")
print(f"Reason: {reason}")


if decision == "APPROVED":
    # Use range() to deploy every desired replica
    for i in range(desired_replicas):
        print(f"Deploying replica {i + 1} of {desired_replicas}")
    print("Deployment completed")
