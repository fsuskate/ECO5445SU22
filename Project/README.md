# Project Stage 01
 
This project will follow a paper published in the American Economic Review. The purpose of the paper was to test for the presence of racial discrimination in the mortgage approval process. The dataset provided contains records of the 2,380 applicants for mortgages in Boston.

1) Create a folder called "Project"
2) Read the [paper](https://github.com/JoshuaEubanksUCF/ECO5445/blob/main/Project/Documents/Mortgage%20Lending%20in%20Boston%2C%20Interpreting%20the%20HMDA%20Data.pdf) as it provides a detailed discussion of the data and insight on the determinants of the probability of being approved. 
3) Bring in the [dataset](https://github.com/JoshuaEubanksUCF/ECO5445/blob/main/Project/Data/hmda_sw.csv) provided within my repository. The variables in the dataset do not have intuitive names (e.g., the meaning of S3 is unclear). Referencing the [data description](https://github.com/JoshuaEubanksUCF/ECO5445/blob/main/Project/Documents/hmda_data_description.pdf) and the AER paper, identify the qualitative dependent that
you will be modeling and the set of co-variates that you intend to include in your various models, and rename the variables so that they have (somewhat) intuitive names. Be certain that the debt-to-income ratio, race, self-employed, marital status, and education indicator variables are included, among other variables.
4) Generate summary statistics on the set of variables selected, and explain the composition of the sample and of the characteristics of an average (representative) applicant. In the process, you should also generate and histograms and frequency counts on particular variables of interest, which can be referenced in your explanation of the composition of the sample and of a representative applicant.
5) What is the baseline probability of an individual being approved for a mortgage?
6) Based on the data you read in, create a table with the following structure (values will not be the same as the example):

    | Applicant Race | Approved | Not Approved | Total |
    -----------------|----------|--------------|-------|
    American Indian or Alaskan Native | 5 |	13 | 18 |
    Asian or Pacific Islander |	21 | 12 | 33 |
    Black |	23 | 32 | 55 |
    Hispanic | 33 |	46 | 79 |
    White |	75 | 25	| 100 |
    Total |	157 | 128 |	285 |

7) From the table you create in 6, calculate the following:

    $P(Approved|White)$

    $P(NotApproved|Black)$

