0x19. Postmortem

TASKS

0. MY FIRST POSTMORTEM
Outage Postmortem: July 2, 2024 - Login System Outage
Issue Summary:
Duration: The outage began at 10:15 AM UTC and was fully resolved by 1:45 PM UTC (3.5 hours).
Impact: The login service was intermittently down, causing users to experience either long delays or complete failures when trying to log in. Approximately 40% of users were affected during the outage.
Root Cause: The issue was caused by a misconfiguration in the Redis caching layer that resulted in excessive CPU usage, leading to failed login requests due to timeouts in the authentication service.

Timeline:
10:15 AM UTC: The issue was first detected via a monitoring alert indicating high latency on the authentication service.
10:20 AM UTC: The issue was initially identified as a potential database connectivity issue, and the database logs were reviewed. No anomalies were found.
10:30 AM UTC: A spike in CPU usage was detected on the Redis cluster, but the issue was dismissed as normal under high load.
11:00 AM UTC: The engineering team investigated the load balancing configuration, assuming the issue was related to an under-provisioned instance.
11:30 AM UTC: As user complaints increased, the team escalated the issue to the Site Reliability Engineering (SRE) team.
12:00 PM UTC: The SRE team confirmed that the Redis server was being overwhelmed, causing high latency in authentication requests.
12:45 PM UTC: Redis cache configuration was adjusted to offload unnecessary data and reduce CPU strain. The service began recovering.
1:45 PM UTC: The issue was fully resolved, and all users regained access to the system.

Root Cause and Resolution:
Root Cause: The primary cause was a misconfiguration in Redis, where a high volume of unnecessary authentication session data was being cached. As more users logged in, the Redis servers began to exhaust CPU resources, causing timeouts in subsequent authentication requests. This led to intermittent failures and delays in the login system.
Resolution: The Redis cache configuration was corrected by adjusting the TTL (Time-To-Live) settings for session data, limiting the volume of data being cached. Additionally, the cache eviction policy was updated to ensure older, less frequently accessed data was purged to avoid system overload. The affected Redis nodes were also restarted to clear the backlog.

Corrective and Preventative Measures:
Improvements:

Improve capacity planning for Redis clusters based on current and projected traffic.
Update cache management policies to dynamically adjust based on traffic patterns.

Action Plan:

Increase monitoring on Redis: Implement more granular monitoring for CPU usage, memory consumption, and cache hit/miss ratios on Redis servers.
Revise Redis TTL and eviction policies: Update session TTL and implement more aggressive cache eviction strategies to prevent overload during high traffic periods.
Review and optimize authentication flow: Ensure that the authentication service scales horizontally and gracefully handles spikes in load.
Improve load balancing: Update load balancing configurations to account for Redis server CPU utilization and traffic patterns.
Conduct post-mortem review: Hold a cross-functional team review to ensure that the incident response protocols are effective and that similar issues are prevented in the future.
By implementing these changes, we aim to prevent a recurrence of this issue and improve system resilience under heavy load.



1. MAKE PEOPLE WANT TO READ YOUR POSTMORTEM

Outage Postmortem: The Great Login Fiasco of July 2, 2024
Issue Summary:
Duration: The outage started at 10:15 AM UTC and was fully resolved by 1:45 PM UTC (a glorious 3.5 hours of suspense).
Impact: A large portion of the user base (about 40%) found themselves face-to-face with the infamous “401 Unauthorized” error while trying to log in.It was like a digital bouncer at the door, rejecting them for no reason other than “overload” – not even a good party reason.
Root Cause: It turns out our Redis caching layer had a little too much enthusiasm — excessive CPU usage from unnecessary session data led to our authentication service performing the digital equivalent of a faceplant.

Timeline:
10:15 AM UTC: Alert! High latency in the login service. Engineers start peeking around the logs like detectives in a mystery novel. Suspicious.
10:20 AM UTC: "Hmm, maybe the database’s got the hiccups?" Spoiler alert: It didn’t. No dice.
10:30 AM UTC: Redis starts throwing a tantrum. "Too many sessions, too little CPU!" But we thought it was just the regular holiday rush.
11:00 AM UTC: Investigating load balancers. Engineer assumes “This is it, we found the culprit!” Spoiler: Not the culprit.
11:30 AM UTC: As user complaints pile up like dirty laundry, SRE team enters the chat. “We’re on it!” 🎤
12:00 PM UTC: Redis is the culprit! Redis CPU was maxed out, unable to process all the session data like a coffee shop that ran out of beans. The SRE team tackles the issue head-on.
12:45 PM UTC: Redis gets a makeover! Old, unnecessary data is kicked out, and CPU consumption drops. Things begin to look better. Slowly but surely.
1:45 PM UTC: All services are back online! Everyone can log in, and the virtual bar is open again. 🎉

Root Cause and Resolution:
Root Cause: Redis, like that one friend who tries to take on more than they can handle, was overstuffed with session data. This made the cache servers burn through CPU resources like a hamster on a wheel. Eventually, everything started falling apart, and login attempts timed out.

Resolution: After a thorough inspection by our SRE team, we gave Redis some much-needed space. We optimized the session data and changed the TTL (time-to-live) for stored data, making sure old and unimportant data got purged kind of like cleaning out your fridge before a big party. With these adjustments and a restart of the Redis nodes, everything returned to normal.

Corrective and Preventative Measures:
Improvements:

Redis, meet more sophisticated monitoring (you’ll thank us later).
Update our caching strategies, ensuring Redis never tries to overachieve again.

Action Plan:

Increase monitoring on Redis: We’re not saying Redis needs therapy, but it could use some more detailed monitoring on CPU, memory, and cache hit/miss ratios.
Revise TTL & eviction policies: Redis needs a gentle nudge to stop hoarding session data. Let's set a reasonable expiry time for session info to avoid the overstuffed cache issue.
Review authentication flow: Let’s make sure our authentication service scales like an eager fitness enthusiast — we don’t want any of our services breaking a sweat.
Revisit load balancing: Ensure we’re not overwhelming any one service by dynamically adjusting to system load.
Post-mortem review: We'll gather the team for a virtual roundtable where we dissect what happened, ensuring our response protocols become even smoother.

The Silver Lining: While this was a bit of a digital "oops," it gave us an opportunity to fine-tune our systems, improve monitoring, and make sure this never happens again. And hey, we’re all a little wiser now just like the hero in every good underdog story.
Thanks to everyone for their hard work, quick thinking, and patience through the outage. We've now got our Redis under control and will be more prepared than ever before!
