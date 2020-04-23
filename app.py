
import json
import requests
def cases(state,district):
    global lst
    source=requests.get('https://api.covid19india.org/v2/state_district_wise.json').json()
   
    for i in range(len(source)):
        if(source[i]['state']==state):
            lst=source[i]['districtData']
            for j in range(len(lst)):
                if(lst[j]['district']==district):
                    ans=lst[j]['confirmed']
                    #print(ans)
                    return ans
                
def statewise(state_code):
    url = "https://covid19india.p.rapidapi.com/getStateData"+'/'+state_code
    
    headers = {
        'x-rapidapi-host': "covid19india.p.rapidapi.com",
        'x-rapidapi-key': "216dd782cdmsh7f86900ecb6882dp14269fjsndf6ecc7de5a9"
        }
    
    r = requests.request("GET", url, headers=headers).json()
    x=r['response']['confirmed']
    return x
#cases('Kerala','Kollam')
def state_data():
    
    lst=pd.read_html('https://www.mohfw.gov.in/')
    dfs=lst[0]
    dfs.drop(columns=['S. No.'],inplace=True)
    dfs=dfs.rename(columns={'Name of State / UT':'State','Total Confirmed cases (Including 76 foreign Nationals)':'Cases',
                         'Cured/Discharged/Migrated':'Cured','Death':'Death'})
    dfs.replace("Nagaland#","Nagaland",inplace=True)
    dfs.drop(index=[33,34,35],inplace=True)
    data=dfs[dfs['Cases'].astype(str).astype(int) > 300]
    return data