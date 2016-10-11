## Cikibike Null Hypothesis project review

The Null hypotheisis is correctly formulated except you switch between 35 and 35 half the way into the formulation of the Null. decide if the cutodd is 30 or 35.
The mathematical formulatio of the Null is missing (e.g. H0: T_less35 - T_more35...)

The data supports the question.

If you download the data locally with
!curl -O 'https://s3.amazonaws.com/tripdata/201512-citibike-tripdata.zip'
you have to move it to the PUIDATA directory. Generally data should be stored separately from code. This also prevents me and the TAs from ending with 90 redundant copies of datasets as we grade 90 notebooks!

The data supports the question.

The question can be answered with a test of means, and since you are phrasing the question as "longer than the average users" you can use the entire dataset as a population (without removing the under 35yo users) as a population and the subset that is under 35yo as a sample, and apply a Z test.

Also notice that since you are working with a lot of data Effect size should be reported along with statistical significance.
