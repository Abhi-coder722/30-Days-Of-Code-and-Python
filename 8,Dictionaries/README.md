<h4>Objective</h4>
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

<h4>Task</h4>
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.<br>

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

<h4>Input Format</h4>

The first line contains an integer, n, denoting the number of entries in the phone book.<br>
Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line. The first value is a friend's name, and the second value is an 8-digit phone number.

After the n lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.<br>

Note: Names consist of lowercase English alphabetic letters and are first names only.


<h4>Output Format</h4>

On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise, print the full name and phoneNumber in the format name=phoneNumber.

<h4>Sample Input</h4>

3<br>
sam 99912222<br>
tom 11122222<br>
harry 12299933<br>
sam<br>
edward<br>
harry<br>

<h4>Sample Output</h4>

sam=99912222<br>
Not found<br>
harry=12299933<br>