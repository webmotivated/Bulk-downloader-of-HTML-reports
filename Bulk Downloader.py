
import requests #download part
import sys #upload part
from requests_ntlm import HttpNtlmAuth #upload part


# Fill in your details here to be posted to the login form.
payload = {
    'loginid':  'xxxxxxxxxxxxxxxxxxx',
    'password': 'xxxxxxxxxxxxxxxxxxx'
}


# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    
    p = s.post('https://nationalgrid-so.quickbase.com/db/main?a=SignIn', data=payload, verify=False)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print (p.text)
	
   
   #Landing Page
    # r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=q&qid=20')
    # with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/2018 10 - HTML reports/Value Streams/VS LANDING.html', "w", encoding='utf-8') as file:
    #     file.write(r.text)

   #Jonas 2020 Test - Teams List
    # r = s.get('https://nationalgrid-so.quickbase.com/db/bnag2tu3w?a=td')
    # with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/2018 10 - HTML reports/Value Streams/This is Teams.html', "w", encoding='utf-8') as file:
    #     file.write(r.text)


   # #Value Streams
   #  r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&key=6&dfid=11')
   #  with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/3. HTML reports/Value Streams/Strategy and Regulation.html', "w", encoding='utf-8') as file:
   #  	file.write(r.text)
   #  r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&key=11&dfid=11')
   #  with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/3. HTML reports/Value Streams/Commercial, ESO.html', "w", encoding='utf-8') as file:
   #      file.write(r.text)
   #  r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&key=8&dfid=11')
   #  with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/3. HTML reports/Value Streams/SO Assurance.html', "w", encoding='utf-8') as file:
   #      file.write(r.text)    
   #  r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&key=4&dfid=11')
   #  with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/3. HTML reports/Value Streams/Future Markets.html', "w", encoding='utf-8') as file:
   #      file.write(r.text)    
   #  r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&key=1&dfid=11') #Previous
   #  #r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&r=b&rl=xu') 	#Antony sent new
   #  with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/3. HTML reports/Value Streams/Networks, ESO.html', "w", encoding='utf-8') as file:
   #      file.write(r.text) 
   #  r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&key=3&dfid=11')
   #  with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/3. HTML reports/Value Streams/Gas Operations, SO.html', "w", encoding='utf-8') as file:
   #      file.write(r.text) 
   #  r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&key=9&dfid=11')
   #  with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/3. HTML reports/Value Streams/SO Change.html', "w", encoding='utf-8') as file:
   #      file.write(r.text) 
   #  r = s.get('https://nationalgrid-so.quickbase.com/db/bmqsdgtdr?a=dr&key=10&dfid=11')
   #  with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/3. HTML reports/Value Streams/National Control, ESO.html', "w", encoding='utf-8') as file:
   #      file.write(r.text)       


    
    #Departments
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=8&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/2. DML DEV n COMM/1. DML comm/1. HTML reports/Departments/Commercial Operation Strategy.html', "w", encoding='utf-8') as file:
        file.write(r.text) 
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=4&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Contract for Difference, Capacity Market.html', "w", encoding='utf-8') as file:
        file.write(r.text)     
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=5&dfid=13')
    # time.sleep(3)
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Contract and Settlement.html', "w", encoding='utf-8') as file:
    	file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=14&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Electricity Market Change Delivery.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=61&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/EMR Modelling.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=51&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/EMR Stakeholder and Compliance.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=13&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Industry Frameworks and Code Governance.html', "w", encoding='utf-8') as file:
        file.write(r.text)   
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=6&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Commercial Operations ESO.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=1&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Control Support and Review.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=2&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Control System Support.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=64&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/ESO Change.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=3&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Power Systems.html', "w", encoding='utf-8') as file:
        file.write(r.text)
        r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=50&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Electricity Customer Connections.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=49&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Electricity Network Operability.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=10&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Network Access Planning.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=11&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Network Development.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=31&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/SO Assurance.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=25&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/Energy Analysis.html', "w", encoding='utf-8') as file:
        file.write(r.text)
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=42&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/ESO Regulation.html', "w", encoding='utf-8') as file:
        file.write(r.text)        
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=53&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/SO Customer and Stakeholder.html', "w", encoding='utf-8') as file:
        file.write(r.text) 
    r = s.get('https://nationalgrid-so.quickbase.com/db/bmsgkp6z8?a=dr&key=27&dfid=13')
    with open('C:/Users/Documents/OneDrive - National Grid/1. Data Basics/zzz OLD/1. DML comms/1. HTML reports/Departments/SO Strategy.html', "w", encoding='utf-8') as file:
        file.write(r.text)  

   











# #Read filename (relative path) from command line
# #'C:/Users/Desktop/Gas Operations.html' = sys.argv[1]
# fileName = sys.argv[1]
 
# #Enter your SharePoint site and target library
# sharePointUrl = 'https://teams.nationalgrid.com/CookieAuth.dll?GetLogon?curl=Z2F&reason=0&formdir=3'
# folderUrl = '/sites/SO_Data/Globally%20Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FSO_Data%2FGlobally%20Shared%20Documents%2FData%20Owner%20and%20Steward%20Html%20Files'
 
# #Sets up the url for requesting a file upload
# requestUrl = sharePointUrl + '/_api/web/getfolderbyserverrelativeurl(\'' + folderUrl + '\')/Files/add(url=\'' + fileName + '\',overwrite=true)'
 
# #Read in the file that we are going to upload
# file = open(fileName, 'rb')
 
# #Setup the required headers for communicating with SharePoint 
# headers = {'Content-Type': 'application/json; odata=verbose', 'accept': 'application/json;odata=verbose'}
 
# #Execute a request to get the FormDigestValue. This will be used to authenticate our upload request
# r = requests.post(sharePointUrl + "/_api/contextinfo",auth=HttpNtlmAuth('uk\\','Kadagiukai55'), headers=headers)
# formDigestValue = r.json()['d']['GetContextWebInformation']['FormDigestValue']
 
# #Update headers to use the newly acquired FormDigestValue
# headers = {'Content-Type': 'application/json; odata=verbose', 'accept': 'application/json;odata=verbose', 'x-requestdigest' : formDigestValue}
 
# #Execute the request. If you run into issues, inspect the contents of uploadResult
# uploadResult = requests.post(requestUrl,auth=HttpNtlmAuth('uk\\','Kadagiukai55'), headers=headers, data=file.read())




#SUCCESS SAVING SIMPLE PAGE
#import requests
#pagelink = "https://www.dragonlng.co.uk/commercial/planned-maintenance"
#page = requests.get(pagelink)
#with open('C:/Users/Desktop/example.html', "w") as file:
#    file.write(page.text)