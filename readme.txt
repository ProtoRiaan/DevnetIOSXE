Playing around with Netconf Client preparing for Devnet Cert Exam.

Ran into some issues connecting to the 'reccommended' code sandbox. Verified it was having an authentication error with some SSH testing. Reached out to the Devnet team for assist. The verified the sandbox was undergoing maintenance
They provided a link and new credentials to use on the "latest" code sandbox. Tested today and it is working well. 

Thus far I am able to get and print a list of the capabiliteis and also grab and print the running config in xml and print it to a file for review.

Next step is to pick a data model from the capabilities list and pull the schema with .get_schema, From here we can create a fileter for our config xml replies.
For now I am printing the Schema into file for easy review and study. These can all also be found online and possibly in the yang explorer tool on developer.cisco.com.

Made some good progress practicing how to pass in a filter string to specify a specific confg item to retrieve. Still working on how to pull a a larger element then itterate through the children.