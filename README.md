# Vaccine_avaliabality
 This is a covid vaccine slot availability tracker in simple UI

 <h2>You have to input the Pincode, Date, Type of vaccine you want</h2>
 <h3> I had developed this earlier, I wish, i had released this before the Government of India blocked all of the COWIN-API </h3>
 <h1> To run this on your computer </h1>
 <ul>
    <li> You must have a good internet connection.</li>
    <li> Clone this Repository.</li>
    <li> Run these commands in the terminal</li>
</ul>

```bash

cd Vaccine_avaliabality

```
```python

pip install -r requirements.txt

streamlit run home.py
```
 <ul> 
    <li> local host "8501" opens up and you can carry on </li>
 </ul>

<h1> This shows the dummy data from some other API.</h1>
<h2> When the COWIN-API are opened for public, I will only update the fetching data</h2>

To change the dummy data to real-time data you have to change the api 
<a href="https://github.com/Prajwalprakash3722/Vaccine_avaliabality/blob/e91f354740741a62262745a8a7df7c22b524f463/request.py#L61">Change-code</a> from this 👇🏽

```python

def sample_data(pincode):
    
    try:
        url = f'https://api.postalpincode.in/pincode/{pincode}'
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            readableA_json_data = json.loads(response.text)
            for x in readableA_json_data:
                data = x['PostOffice']

        return data
    except:
        return 'No data found'
```
to this 👇🏽
```python
   
def sample_data(pincode, date):
    
    try:
        url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}'
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            readableA_json_data = json.loads(response.text)
            for x in readableA_json_data:
                data = x['sessions']

        return data
    except:
        return 'No data found'
```
 Author: Prajwal Prakash. <br/>
 Date: 13/03/2021. <br/>
 Last Updated: 16-05-2021 (README.md) <br/>
 Goal: To GET the vaccine availability slot. <br/>
 licensed under MIT <br/>
 If you want to build the same app for feel free to fork it from my repo and make the necessary changes, But attriubution
 to the handle <a href="https://github.com/Prajwalprakash3722">@Prajwalprakash3722</a> in GitHub is mandatory. <br/>
 Used API's: postal API, Cowin-API <br/>
 <img src="https://camo.githubusercontent.com/10be9e867236dd49357aac457c348b672ba199dece78db957804cc6bd0bdf14c/68747470733a2f2f7777772e726173612e636f6d2f6173736574732f696d672f736172612f736172612d6f70656e2d736f757263652d322e302e706e67" style="height:100px;width:100px;" alt="open-source-logo"/>
