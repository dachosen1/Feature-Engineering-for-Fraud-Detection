

### Summary

Anomaly detection helps in the early detection of critical outliers in a system. Based on the context, these outliers can be detrimental and result in loss of resources, and time through errors, fraud, manipulation of stocks, and other such malicious activities. Outliers can also be beneficial for example in investing, and arbitrage. Business decisions that leverage anomaly detection, which used to require intense human resource and capacity can now be completed in a short time through versatile models and automation. In this project I implemented the findings of the Feature Engineering for Credit Card Fraud research paper to create both supervised and unsupervised models for fraud detection. 


### Feature Engineering for Credit Card Fraud Paper Summary 

In the feature engineering for credit card fraud paper, the author examines a new approach for developing features for machine learning algorithms. They address the cost-sensitivity, and the features are preprocessing to achieve improved fraud detection and savings.  Typical models only use raw transactional features, such as time, amount, place of the transaction. However, these approaches do not take into account the spending behavior of the customer, which is expected to help discover fraud patterns. 

The Feature engineering strategies for credit card fraud detection was an essential framework in creating features to analyze credit card transaction data. 

1.	A more compressive way for feature creation is to derive some features using a transaction aggregation strategy.

2.	The derivation of the aggregation features consists in grouping the transactions made during the last given number of hours, first by card or account number, then by transaction type, merchant group, country or other, followed by calculating the number of transactions or the total amount spent on those transactions. 

3.	When aggregating customer transactions, there is an essential question on how much to accumulate, in the sense that the marginal value of new information may diminish as time passes. Indeed, when time passes, information loses their value, in the sense that customer spending patterns are not expected to remain constant over the years. In particular, Whitrow et al. define a fixed time frame to be 24, 60, or 168. 

When using the aggregated features, there is still some information that is not completely captured by those features. The issue when dealing with the time of the transaction, specifically, when analyzing a feature such as the mean of transaction time, is that it is easy to make the mistake of using the arithmetic mean, it does not take into account the periodic behavior of the time feature. 
For the experiment, they used three cost-sensitive classification algorithm: Decision Tree, Logistics Regression, Random Forest, Bayes minimum risk model, a cost-sensitive decision tree algorithm, and measured the results. 

The paper shown the importance of using features that analyze the consumer behavior of individual cardholders when constructing a credit card fraud detection model.  We show that by preprocessing the data to include their cent consumer behavior,the performance increases by more than 200% compared to using only the raw transaction information.


## Modeling Approaches: 

### Supervised 

**Auto ML**
**Random Forest**
**Isolation Forest**

### Unsupervised

**DBSCAN**
**Mean Shift**
**K Means**

