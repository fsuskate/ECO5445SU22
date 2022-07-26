# Assignment07

For this assignment, you are going to implement the LASSO regression covered in class.

You will need to reference your previous submission. We will use the previous data and your previous models.

1.  This time, I want you to separate your data into testing and training. For this exercise, randomly extract 100 for testing different models, and save the other 900 for training your models.
2.  Run your final model you had in the previous assignment to the training data
3.  With the same model in part 2, run the standard LASSO regression model on the training data.
4.  Now using the same model in part 2, run a 10-fold cross-validated LASSO on the training data
5.  Lastly, using the testing data, I want you to calculate the RMSE for each of the lambda's selection methods discussed (AIC, BIC, AICc, cv.min, cv.1se) and the the model in part 2. Which method performed the best in prediction the home price?
