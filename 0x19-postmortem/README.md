Issue Summary:
On May 9th, 2023, from 12:00 PM to 2:30 PM EST, members of our web application were unable to access the platform. The outage affected all members attempting to log in and make contributions to their saving groups, resulting in a 100% outage for those members.

Timeline:
12:00 PM: The outage was detected by our monitoring system, which alerted our engineering team.
12:05 PM: The team began investigating the outage by checking the web server logs and database server logs for any errors or anomalies.
12:15 PM: Initial investigation showed that there were no issues with the web server or database server, and the issue was assumed to be caused by a network connectivity issue.
12:30 PM: The network team was contacted to investigate potential issues with the network connectivity.
1:00 PM: The network team reported that there were no network connectivity issues and suggested that the issue could be with the load balancer.
1:15 PM: The load balancer was checked for any issues, but no errors or anomalies were found.
2:00 PM: After exhaustive investigation, it was discovered that the root cause of the outage was a misconfigured firewall rule that was blocking access to the web application for all members.
2:30 PM: The issue was resolved by correcting the misconfigured firewall rule.

Root Cause and Resolution:
The root cause of the outage was a misconfigured firewall rule that was blocking access to the web application for all members. This rule was mistakenly put in place during routine maintenance, which caused all incoming traffic to be blocked. The issue was resolved by removing the misconfigured firewall rule, allowing members to access the platform once again.

Corrective and Preventative Measures:
To prevent similar issues in the future, we will implement the following measures:

1. Improve our change management process to ensure that all changes to our system are thoroughly tested before deployment.
2. Implement additional monitoring to detect issues with firewall rules and network connectivity.
3. Conduct a review of our firewall rules to identify any potential misconfigurations.

Tasks to address the issue:

1. Conduct a thorough review of our firewall rules to ensure that they are properly configured.
2. Implement additional monitoring to detect issues with firewall rules and network connectivity.
3. Update our change management process to include additional testing before deployment.

In conclusion, the outage that occurred on May 9th, 2023, was caused by a misconfigured firewall rule, which was resolved by removing the rule. To prevent similar issues in the future, we will implement additional measures to improve our change management process, enhance our monitoring capabilities, and conduct a review of our firewall rules.