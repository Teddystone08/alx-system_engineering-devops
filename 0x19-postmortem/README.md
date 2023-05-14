# Load balancer Server Outage Incident Report (Created)
> By Ernest T. Lartey - (https://github.com/Teddystone08)

## Issue Summary:
On May 4, 2023, starting at 2:05 PM GMT, users experienced a partial outage of our online sport website. This lasted for 2 hours and impacted 100% of our users, resulting in significant revenue loss, agitation and dissatification.

## Timeline:
- 2:05 PM: The issue was detected when our monitoring system sent an alert to our on-call engineer about the website.
- 2:07 PM: The on-call engineer checked the website and confirmed that it was malfunctioning.
- 2:09 PM: The engineer initiated investigations into the root cause of the issue.
- 2:12 PM: The engineer found that the website's load balancer server was down and attempted to restart it.
- 2:15 PM: The website was still malfuctioning, and the engineer escalated the issue to the backend team.
- 2:20 PM: The database team started investigating the issue and found that the geographically distributed node algorithm was not functioning.
- 3:00 PM: The backend team redesigned and programmed the script and restart the server.
- 3:40 PM: The root cause was identified as a node distant distribution  script that has stopped responding to geographical request.

## Root Cause and Resolution:
The root cause of the issue was a malfunction geographically distributed node that was not designed correctly, causing it not to distribute geographical response which result to reducing user experience.

## Corrective and Preventative Measures:
To prevent similar issues from happening in the future, we will be taking the following corrective and preventative measures:
- frequent update of the distribution node algorithm to ensure effective distant distribution.
- Implement frequent monitoring to detect and prevent node issues before they impact our services.
- We will review and improve our incident response process to ensure faster and more effective resolution of issues.
- We will conduct a thorough review of all our systems to identify any other potential sources of similar issues and take appropriate actions to mitigate them.

## Tasks to Address the Issue:
- Update the geographical distribution node algorithm to ensure effective distribution.
- Review and improve our incident response process.
- Conduct a thorough review of all our systems to identify potential sources of similar issues and take appropriate actions.

----
## Author
* **Ernest T. lartey**(https://github.com/Teddystone08)
