# UK Market Entry Screen: Birmingham vs London

Are IT Companies more popular in Birmingham or London?

## Question and Preliminary Findings

In London, there are roughly 15x more IT companies than in Birmingham. On the other hand, there are roughly 13.8x more active enterprises in London than in Birmingham. This is because London is a much larger city both in land mass and population. So we need to look at the data in a different way. In Birmingham, there are roughly 6.4 companies for every IT company. In London, there are 5.9 companies for every IT company. Assuming every enterprise is a company and the 2026 and 2024 values are similar. This shows that IT companies are a more popular business in London than in Birmingham.

**Confidence: medium.**

I am not extremely confident in my hypothesis. This is because the years are different. The ONS data includes sole traders and partnerships, which, if they could be accounted for, may skew the data either way and I would never know. Each number is accurate. However, when you are doing a ratio and each side is data from a different year, it's probably inaccurate.

## Comparison of Birmingham and London

| City | Total Active IT Companies | Number of Births of New Enterprises for 2024 | Number of Deaths of New Enterprises for 2024 | Number of Active Enterprises for 2024 |
|---|---|---|---|---|
| Birmingham | 6,710 | 6,500 | 5,145 | 43,175 |
| London | 100,791 | 75,550 | 61,245 | 595,280 |

## Data Sources and Definitions
| Source                                                           | Link                                                                                                               | Licence                        | Snapshot date                             | What one row means                                                                                                                                                           |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Companies House Free Company Data (`BasicCompanyDataAsOneFile`)  | https://download.companieshouse.gov.uk/en_output.html                                                              | None Stated by Companies House | 2026-10-01                                | One Company registered at Companies House ( a legal entity), with its registered address, status and up to four SIC codes. Dormant companies are included.                   |
| ONS Business Demography 2024 (Excel Workbook) | https://www.ons.gov.uk/businessindustryandtrade/business/activitysizeandlocation/bulletins/businessdemography/2024 | Open Government Licence v3.0   | Published 20 Nov 2025 ( Data is on 2024 ) | One place ( can be a country, region or local authority ) along with its count of active enterprises, as well as births or deaths for the year ( rounded to the nearest 5 ). |

ONS is 2024, Companies House is 2026.

One row represents a company, and one number represents enterprise deaths, births and number of active enterprises for a specific area.

A company is a registered company that has to fulfil requirements that an enterprise doesn't have to. An enterprise can be someone who is self employed or two self employed people in a partnership.

All industries. The numbers round to the nearest 5. An enterprise is being counted, not a business.

## Data Quality Tests
 
I have carried out two tests. The first one is in my test_duplicates.py file and it uses DuckDB and pytest to carry out an SQL query on the companies_house.csv file. It looks for company numbers that were duplicated by comparing the number of distinct company numbers to the amount of rows. If these two values are the same, every single company number is different. If there are more rows than company numbers, a company number could have been reused. After this test I ran it and it passed. Meaning every single company number is different.
 
The second test is in my test_dates.py file and it looks for null dates or any dates in the future. This test was also carried out on the companies_house.csv file and it passed, therefore proving that all of the dates are neither null (empty) nor in the future.


## Limitations

My counts of 6,710 active IT companies in Birmingham, and 100,791 active IT companies in London include dormant companies. This is because a company with the status "Active" can still be dormant.

The B postcode isn't exclusive to Birmingham City. This is because there are towns that have B postcodes but are not part of Birmingham City but are instead part of the Black Country and other surrounding areas. The companies in those towns are included in my count of 6,710 because they have a B postcode.

There are other postcodes in London, for example HA for Harrow and RM for Romford. My count of 100,791 IT companies in London does not include IT companies in these areas because my query looks for companies with postcodes in London Postal District areas.