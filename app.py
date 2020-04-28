
import json
import requests
import pandas as pd
def cases(state,district):
    global lst
    source=requests.get('https://api.covid19india.org/v2/state_district_wise.json').json()

    for i in range(len(source)):
        if(source[i]['state']==state):
            lst=source[i]['districtData']
            for j in range(len(lst)):
                if(lst[j]['district']==district):
                    ans=lst[j]['confirmed']
                    ans1=lst[j]['deceased']
                    ans2=lst[j]['recovered']
                    #print(ans)
                    return ans,ans1,ans2
def statewise(user_state):
    url = "https://covid19india.p.rapidapi.com/getStateData"+'/'+user_state

    headers = {
        'x-rapidapi-host': "covid19india.p.rapidapi.com",
        'x-rapidapi-key': "216dd782cdmsh7f86900ecb6882dp14269fjsndf6ecc7de5a9"
        }

    r = requests.request("GET", url, headers=headers).json()
#     print(r)
    r=json.dumps(r)
#     print(type(r))
#     print(r[130:134])
#     print(r[151:154])
#     print(r[168:171])

    return r[130:134],r[151:154],r[168:171]

def helpline(user_state):
    dfs=pd.read_html("https://www.indiatvnews.com/coronavirus/helpline-numbers")
    df=dfs[0]
    df=df['State Helpline Numbers']
    x=df.loc[lambda df: df['State/UT']=="Gujarat"]
    for i in x.values:
        return i[1]
#helpline("Gujarat")

def statewise_full(user_state):
    dfs=pd.read_html("https://www.mohfw.gov.in/")
    df=dfs[0]
    x=df.loc[lambda df : df['Name of State / UT']==user_state]
    for i in x.values:
        print(i[2])
        return i[2],i[3],i[4]
         
#user_state("Chandigarh")