



# SystemAdvanced
  
Module to extend functionalities of the System section  

*Read this in other languages: [English](Manual_SystemAdvanced.md), [Português](Manual_SystemAdvanced.pr.md), [Español](Manual_SystemAdvanced.es.md)*
  
![banner](imgs/Modulo-System.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Export variables to a file
  
Export all Rocketbot variables to a files
|Parameters|Description|example|
| --- | --- | --- |
|File path  |Path and name of the file where the variables will be stored|C:/User/Usuario/Folder/file.txt|

### Set Multiple Variable
  
Set multiple variables from an iterable object
|Parameters|Description|example|
| --- | --- | --- |
|Data |Value to set||
|Set variables |Variables to set separated by comma|var1,var2,var|

### Run Backup
  
Make a new backup
|Parameters|Description|example|
| --- | --- | --- |

### Clean var(s)
  
Enter the variables to be cleaned separated by a comma
|Parameters|Description|example|
| --- | --- | --- |
|Variables|Variables to be cleaned|Variable|

### Clean var(s) by category
  
Enter the category of variables to clean
|Parameters|Description|example|
| --- | --- | --- |
|Category|Name of the category to which the variables belong to be cleaned. You can add multiple categories separated by commas.|Connection|

### Random
  
Use random library
|Parameters|Description|example|
| --- | --- | --- |
|Select method|Method of the library used||
|Value|Argument for the method (random.randrange(argument))|5,9|
|Variable|Variable where the result will be stored|Variable|

### Foreground App
  
App to the foreground
|Parameters|Description|example|
| --- | --- | --- |
|Application name|Name of the application to bring to the foreground|test.xlsx - Excel|

### Get Handle from Open windows
  
return and array with name and handle tuple from Open Window
|Parameters|Description|example|
| --- | --- | --- |
|Variable|Variable where the handle will be stored|Variable|

### Timer
  
Get time number
|Parameters|Description|example|
| --- | --- | --- |
|Variable|Variable where the number will be stored|Variable|

### Get Arguments
  
Gets the arguments that were passed when Rocketbot started.
|Parameters|Description|example|
| --- | --- | --- |
|Required arguments|List of required arguments separated by comma.|['-start', 'id', '-db']|
|Assign result to variable|Variable where the result will be stored|Variable|
