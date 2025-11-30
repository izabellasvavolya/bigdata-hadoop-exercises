Exercise 1
 Q1.
How many files are there? _______________1 file_______________ 
Q2. Did number of mapper change? _________________no_____________ 
Q3. Did number of reducer changed? Yes, number of reducers becomes 6 instead of 1 (default)
Q4. Did number of output files change? Why? 
Yes, number of output files equals number of reducers
Q5. What does the value of 'Merged Map outputs' represents and how is it calculated? 
Merged map outputs is the number of temporary files created by the mappers that Hadoop merges together before sending the data to the reducer.



Exercise 2
Q1. Is your change in the mapper or in the reducer? 
Mapper. Removing commas and dots happens before producing key pairs, converting to lowercase happens before mapping, reducer stays the same

Q2. Please submit your code in GitHub
https://github.com/izabellasvavolya/bigdata-hadoop-exercises/tree/main
Is your change in the mapper or in the reducer? 
Reducer. Sorting counts and selecting only top 3 must be done in the reducer.

Q3. 
Print the output of the MapReduce and add to the project. 
Note: you should not use external pipes, sort, or filters. All should be done inside the mapReduce Python code I want to see in the screenshot that includes the command you typed: $ > hadoop fs -ls /user/hduser/gutenberg-output
 ______________________________


