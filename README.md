# Phishing Detection and File Permissions Management

## Description

This project includes two key components:

**Phishing Detection**: A Python script that identifies potential phishing URLs. The script checks for suspicious keywords, known phishing domains, and unusual patterns such as embedded credentials or IP addresses.

**File Permissions Management**: A guide on managing file permissions within Linux systems to ensure proper access control and enhance security for various files and directories.

**Additionally**, I implemented a real-world scenario where I automated the process of updating IP-based access permissions for restricted files within a healthcare company.


---

## Language Used

- **Python**

---

## Program Walk-through

### Phishing Detection

The `main.py` file includes a function that detects phishing URLs based on:

- **Keyword Detection**: Identifies URLs containing suspicious keywords like `login`, `account`, etc.
- **Domain Analysis**: Flags common phishing domains such as `phishing-site.com`.
- **Pattern Recognition**: It identifies unusual URL patterns, such as URLs containing embedded credentials or raw IP addresses.

#### Usage Example

```python
from phishing_detector import is_phishing_url

url = "http://example.com/login"
if is_phishing_url(url):
    print(f"The URL {url} is potentially a phishing site.")
else:
    print(f"The URL {url} appears to be safe.")
```
IP-Based Access Control Automation
In this scenario, I was tasked to maintain and regularly update a file responsible for granting access to restricted patient records at a healthcare company. Employees are restricted access by their IP address.

Step-by-Step Explanation
1. **Assign the File Name to a Variable:**
I started by assigning the name of the file (which contains the list of allowed IP addresses) to a variable for easy reference:
```python
file_name = "allow_list.txt"
```
2. **Open the File Using the with Statement:**
I used the with statement to open the file in read mode ("r"). This ensures that the file is properly closed after reading, even if an error occurs:
```python
with open(file_name, "r") as file:
    ip_addresses = file.read()
```
The open() function reads the contents of the file.

The as keyword assigns the file object to the variable file.

The .read() method reads the entire file content as a string and stores it in the ip_addresses variable.

3. **Convert the File Content into a String:**
The .read() method outputs the file content as a string, which is stored in the ip_addresses variable:
```python
ip_addresses = file.read()
```
5. **Iterate Through the List Using a for Loop:**
I used a for loop to iterate through each IP address in the ip_addresses list. The in keyword is used to loop through the sequence, and each value is assigned to the loop variable element:
```python
remove_list = ["192.168.1.10", "10.0.0.5"]  # Example of IPs to remove
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)
```
A conditional statement checks if the current element is in the remove_list.

If it is, the .remove() method removes the IP address from the ip_addresses list.

6. **Convert the List Back into a String:** <br>
After updating the list, I converted it back into a string using the .join() method. This method combines all items in the list into a single string, with a space (" ") as the separator:
```python
updated_ips = " ".join(ip_addresses)
```
7. **Write the Updated List Back to the File:** <br>
Finally, I used another with statement to open the file in write mode ("w"). The .write() method writes the updated string of IP addresses back to the file, replacing its previous content:
```python
with open(file_name, "w") as file:
    file.write(updated_ips)   `
```
**Summary:** <br>
I created an algorithm to automate the updating of access permissions for a restricted file. The process involved:

**1.** Opening the file and reading its contents.

**2.** Converting the content into a list for manipulation.

**3.** Iterating through the list to remove outdated IP addresses.

**4.** Converting the list back into a string and updating the file.

This ensures that only authorized employees (based on their IP addresses) have access to the restricted patient records.

