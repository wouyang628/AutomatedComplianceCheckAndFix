# Automated Network Configuration Compliance Check And Fix
Automated Network Configuration Compliance Check And Fix

In general, every company/operator has its own golden config. However, when a device is actually configured, it may not comply with the golden config.

By utilizing Juniper Northstar’s compliance check feature. We can automatically scan the network configuration to find uncomplied configuration based on user defined templates and then extract the information and utilize Juniper PyEZ to apply the correct configuration

Demo e.g.
If the interface has RSVP/LDP, it must has ISIS.   
Find interfaces that have RSVP/LDP but not ISIS, then configure the missed configuration Use PyEZ 




