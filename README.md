# creating-a-rest-api-with-django

##  Setup Instructions:  
  
1. Clone repository:  
  
```console  
$ git clone git@github.com:saibottrenham/online_pajak.git
```    
    
1. Install requirements:  
  
```console  
$ pip install -r requirements.txt  
```  

2. Go to `tax_data`:    
  
```console   
$ cd tax_data   
```   

3. Set up DB:   
   
```console  
$ python manage.py makemigrations   
$ python manage.py migrate   
```  
   
4. Run the app:   
  
```console   
$ python manage.py runserver  
```   

## How to use for the required tasks

In case the data is not already present in the DB, please navigate to the root of the repo and run 

```python
python data-import.py
```

Once the data is imported, we can inspect it using the django admin view. 
A test admin user has been created with the following credentials 

USER:   toby
PW:     test

If the admin use is not present, follow the django documentation guide on how to set up a admin user and proceed to the next steps. 
https://docs.djangoproject.com/en/1.8/intro/tutorial02/

```console
http://localhost:8000/admin/api_app/taxdatamodel/
```

In order to search for organisations by name, consider the following. A name can be entered in natural language in the latest
vesion in google chrome using the address bar. For example, `PD Gunarto Rajata Tbk` will resolve to the following url endpoint when pressing enter after copy pasting it into the search bar. In a request from another api, we would consider query parsing and encoding but it is not needed to test the endpoint using described method. 

```console
http://localhost:8000/third-party/?q=PD Gunarto Rajata Tbk -(will become)->  http://localhost:8000/third-party/?q=PD%20Gunarto%20Rajata%20Tbk
```

For the scoring endpoint, consider the following. In order to identify if a transaction happend between an organisation and a vendor, we extact company_id and vendor_id, for example from the admin view or our records. Like the first endpoint, we will be using query parameters of the url in order to find the matching parties.

```console
http://localhost:8000/commercial-rel-scoring/?company_id=adcfdc36-2967-4d22-b195-c0eb340b99fc&vendor_id=3ef3676f-9f07-4332-b764-187961c294f4
```

This concludes the required usecases of the application. The scoring mechanism is presented in a simple addition. Consideration of a improved scoring intelligence could be weighting of transaction amount, frequency in a set period of time, for example the last quarter, accounting of revisions (revised invoices could be identified as douplicate records), how often invoices have been paid on time, how much discount has been given and how often, total transaction value. Furthermore, we could split invoices in different categories, for example high value transactions, low value, high frequency transactions. Regular transactions (stable returns are a good planning foundation). 