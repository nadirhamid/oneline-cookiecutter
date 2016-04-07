Oneline Project Template
===========================================================

A cookiecutter template for Oneline projects

Usage
-----------------------------------------------------------

1. Install CookieCutter

	pip install cookiecutter


2. Use on repo 

```
	cookiecutter https://github.com/nadirhamid/oneline-cookiecutter.git	
```


```
	repo_name [ExampleModule]: OnelineModule
	description [A description for the module]: Testing a module with Oneline
	database_name [OnelineModule]: OnelineModule
	database_user [root]: root
	database_password []: Test_Password_910
	database_host [localhost]: localhost
	vendor_name [vendorname]: ABC Inc.
	package_name [example-module]: Package Name
	version [0.1.0]: 0.0.1
	author_name [Your Name]: Nadir Hamid
	url [https://github.com/...]:
	license [GPL v2]: GPL v2
```
		
	

3. Navigate to Your Repository name	

4. run 

```
	oneline --pack 'Your Repository Name'
	oneline --start
```

5. visit {{ cookiecutter.repo_name }}.html in your browser.
There should be the example module running on this page


More Information
----------------------------------------------------------------------------

+ Extending modules
More on Oneline modules, uses, and examples. 

http://github.com/nadirhamid/oneline-recipes


+ The Oneline Project
Oneline is a WebSockets project written in Python.

http://github.com/nadirhamid/oneline
 







 




