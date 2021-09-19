# Python Developer Test

Thank you for your interest in Online Pajak. As part of our hiring process, the **Data Department** likes to ask candidates to complete a test.
It is designed to allow candidates to show their analytical thinking, their ability to communicate findings and their technical skills.

## Background

One of our key products at Online Pajak is eFaktur, which helps businesses accuratly generate Tax Invoices.
Commercial transactions in Indonesia are subject to a Value-Added Tax (VAT), on the diffrence between the purchase price of a good, and its resale price.
VAT is withheld by the seller from the from the amount invoiced to the buyer and paid to the State Treasury.
In many cases, _both_ the buyer and the seller are required to file their own Tax Invoice, which declares the value of the transaction, with the tax office.



We have provided a collection of generated Tax Invoice data, similar to the ones recorded on our systems, in a Parquet file.
Each record has been stored following the same structure and here is the data dictionary:


+---------------------------+---------+-------------------------------------------------------------+
|          Column           |  Type   |                         Description                         |
+---------------------------+---------+-------------------------------------------------------------+
| user_id                   | string  | Identifier of user reporting the transaction                |
| company_id                | string  | Identifier of company reporting the transaction             |
| company_name              | string  | Official name of company reporting the transaction          |
| npwp                      | string  | Offical tax identifier of company reporting the transaction |
| email                     | string  | Email of company reporting the transaction                  |
| address                   | string  | Address of company reporting the transaction                |
| city                      | string  | City name of company reporting the transaction              |
| region                    | string  | Region name of company reporting the transaction            |
| post_code                 | integer | Postal code of company reporting the transaction            |
| invoice_id                | string  | Identifier of transaction                                   |
| vendor_id                 | string  | Identifier of third-party reported in transaction           |
| vendor_name               | string  | Name of third-party reported in transaction                 |
| commercial_invoice_number | string  | Identifier of commercial invoice                            |
| transaction_type          | string  | Type of transaction                                         |
| status_start              | string  | Initial status of transaction                               |
| status_tax_summary        | string  | Status of tax reported for related transaction              |
| invoice_date              | date    | Date of transaction                                         |
| due_date                  | date    | Payment due date of transaction                             |
| item_name                 | string  | Description of transaction line item                        |
| unitprice                 | integer | Unit price of transaction line item                         |
| quantity                  | integer | Volume of items transacted                                  |
| discount                  | integer | Discount amount applied to transacted items                 |
| gross_amount              | integer | Total gross amount of transacted items                      |
| tax_amount                | integer | Taxable amount for transacted items                         |
| total_amount              | integer | Total net amount of transacted items                        |
| tax_period                | string  | Tax period where transaction was reported                   |
| revision                  | integer | Revision of reported transaction                            |
| reported_date             | date    | Date of tax report                                          |
| reported_status           | string  | Status of tax report                                        |
| reported_status_desc      | string  | Description of tax report status                            |
| tax_type                  | string  | Name of tax reported                                        |
| tax_document_number       | string  | Identifier of taxable transaction                           |
| tax_document_date         | date    | Date of taxable transaction                                 |
| approved_date             | date    | Date of transaction approval                                |
+---------------------------+---------+-------------------------------------------------------------+

Note: The information contained in this dataset is artificially generated and doesn't contain real data.

## Technical Test

One objective of the Data team is to find new streams of revenue by monetising the data we have collected. One potential type of service we can provide is to verify some information from a partner. For instance a fintech lender may want to verify if a company that want to get a loan is genuine and is really transacting with other companies. 

You are tasked to design and build a Django application that will serve the following API endpoints:
- verification of third-parties: this endpoint will be used to verified if a third-party company is a user of our platforms using solely its name. 
- scoring of commercial relationship between companies: this endpoint will be used to assess how frequent 2 companies can be confirmed to be transacting with one another

Note: you don't need manage authentication. You can assumed this is handled by an upstream process. So you can focus solely on the business logics.

Expected Deliverables:
- Code (or github repository) of Django application built
- Documentation presenting the application design and how to use API endpoints
