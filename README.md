# Base Template for my django projects

### How to use this repository!
###### *This is done with Mac commands*

1. Make sure to have python installed in your computer
2. Click Use this template
3. Make your own repository using this
4. Make folder for this project and *cd* into it
5. Clone that repository into that folder(I personally use Github Desktop cause it is so much easier!)
```
git clone https://github.com/<Username>/<Name of Repo>.git>
```
5. Create a venv and activate it
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```
6. Install all project dependencies
```
pip install -r requirements.txt
```
7. Create the database
```
python manage.py migrate
```
8. Create a superuser
```
python manage.py createsuperuser
```
9. Be sure to add your own Secret Key and Email credentials in Settings.py

 
