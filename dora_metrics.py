
import matplotlib.pyplot as plt

deployment_frequency = [2, 3, 4, 3, 5, 4, 6, 5, 7, 6]

lead_time = [10, 12, 8, 15, 9, 11, 7, 13, 10, 8]

total_deployments = 20
failed_deployments = 3

recovery_times = [30, 25, 40, 20, 35, 30, 25, 45, 20, 30]

average_deployment_frequency = (
    sum(deployment_frequency) / len(deployment_frequency)
)

average_lead_time = sum(lead_time) / len(lead_time)

change_failure_rate = (
    failed_deployments / total_deployments
) * 100

mttr = sum(recovery_times) / len(recovery_times)

print("DORA METRICS")

print("Average Deployment Frequency:",
      round(average_deployment_frequency, 2),
      "deployments/day")

print("Average Lead Time:",
      round(average_lead_time, 2),
      "hours")

print("Change Failure Rate:",
      round(change_failure_rate, 2), "%")

print("Mean Time to Recovery:",
      round(mttr, 2), "minutes")




metrics = [
    "Deployment Frequency",
    "Lead Time",
    "Change Failure Rate",
    "MTTR"
]

values = [
    average_deployment_frequency,
    average_lead_time,
    change_failure_rate,
    mttr
]

plt.figure(figsize=(10, 5))
plt.bar(metrics, values)
plt.title("DORA Metrics Dashboard")
plt.xlabel("Metrics")
plt.ylabel("Values")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()