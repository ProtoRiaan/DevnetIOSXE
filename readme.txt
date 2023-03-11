Playing around with Netconf Client preparing for Devnet Cert Exam.

Ran into some issues connecting to the 'recommended' code sandbox. Verified it was having an authentication error with some SSH testing. Reached out to the Devnet team for assist. The verified the sandbox was undergoing maintenance
They provided a link and new credentials too use on the "latest" code sandbox. Tested today and it is working well. Unfortunately basically only about 1% of the code samples from the CBT nuggets course actually works. 
I had to spend a significant amount of time on github and in manuals to figure out why, I guess that is where a live instructor/mentor can save some time. I do feel like I learn more trying to understand why things don't work compared
to understanding why they do. 

Thus far I am able to get and print a list of the capabilities and also grab and print the running config in xml and print it to a file for review. I see now why netconf-yang is such a big improvement. I basically only get a single 
element when I use netconf to pull the config from my old 3750G. Stark contrast to IOSXE where you get to pull an entire Element Tree. Plans for a future practice project would be to build a scipt that can use the limited netconf filters
on the 3750 G and build one of the Yang data structures, prob ietf-interfaces

Next step is to pick a data model from the capabilities list and pull the schema with .get_schema, From here we can create a filter for our get and get_config xml replies.
For now I am printing the Schema into file for easy review and study. These can all also be found online and possibly in the yang explorer tool on developer.cisco.com.

Made some good progress practicing how to pass in filter strings to specify config item to retrieve. Still working on pulling a larger element then iterating through the children.

I ran into some trouble parsing the netconf responses today. Took a little detour to get a bit more familiar with the XML libraries and their capabilities. xml.etree and lxml.etree cannot handle the netconf XML output without first writing to a file. 
As with my first foray in parsing data, xmltodict was smooth as silk. Either way, I have a better working understanding of XML now. 
I was able to pull various size segments of config, parse and iterate through them, then print some ordered config data to screen.

The last step for this quick project remains : pushing config to the device and verify it sticks. I will have to loop around to this later. Next up: practical Ansible and Docker