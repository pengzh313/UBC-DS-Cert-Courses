The below discussion bewteen Peng and the course instructor was for Assignment 4 Q2.4

**Question**: t has been over halfway for the Data Visualization course. So far I think it is quite straight-forward to write codes and generate simple to moderately complex plots by following the course materials, Altair documentations, and other references. However, sometimes I still felt not very clear when interpreting the visualization. Take assignment 4, Q2.4 as an example:

The question is to find any columns that appear to have a positive relationship with the vote_average column. If we only review the matrix plots from Q2.3, I would say all three columns, 'runtime', 'revenue', and 'vote_count', have shown a slightly positive relationship with the 'vote_average' column. Especially, I cannot tell difference between 'revenue' and 'vote_count' by comparing the two plots visually.

Thanks to the following section of correlation coefficients and the plot from Q2.5, the values of correlation coefficients indicate that 'runtime' and 'vote_count' have more calculated strength of the relationship than 'revenue'. Till now, it seems that we have more confidence to give the answer of 'runtime' and 'vote_count' to Q2.4 and exclude 'revenue'. 

After completing the Q2.4 and Q2.5, another confusion came to my mind: Actually, there is no threshold or referenced correlation coefficients for us to determine the positive relationship. Why we should exclude the column of 'revenue'?

**Answer**: Question 2.4 is a hidden test. I will say that the answer in the question description is just an example to show how to format your list object. Your thoughts are correct, run_time and vote_count are the most positively correlated based on the graphs. Revenue does look slightly positive, but without actually calculating the correlations would be difficult to determine.

Based on Question 2.5 you can see that most of the values have some positive correlation, which is anything between 0 and 1. In this case you need to decide what constitutes a meaningful correlation, and this is where it gets a little blurry.

Usually, correlation coefficients also come with a p-value to help you decide if the correlation value is meaningful. For our variables in the graph in 2.5, looking at just coefficients, there is no hard and fast rule of what is a good cut-off. Obviously anything above 0.5 and close to 1 is a stronger correlation, and anything below is a lower positive correlation. (Negative correlations are between -1 and 0).

To a certain degree this is specific to different disciplines - I know in psychology that they do sometimes pay very close attention to very small correlations or 0.1 because they know with the type of question they are asking, and from the experience of having lots of data for the question they are asking they as a field have determined that small correlation values can have significant meaning.

To conclude, anything above zero is a positive correlation, every thing below zero is a negative, the specific range from 0 to 1 is hard to classify on if it is a notable correlation.

Here is a resource I was provided in my work for better understanding correlations. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6107969/
