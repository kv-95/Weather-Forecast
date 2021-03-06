import requests

# URL to which SOAP request must be send
url="https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php"

# Header tag specifying the document type
headers = {'content-type': 'text/xml'}

# The SOAP request
body = """<?xml version="1.0" encoding="UTF-8"?>
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
            <SOAP-ENV:Body>
                <ns3591:NDFDgen xmlns:ns3591="uri:DWMLgen">
                    <latitude xsi:type="xsd:string">38.99</latitude>
                    <longitude xsi:type="xsd:string">-77.01</longitude>
                    <product xsi:type="xsd:string">time-series</product>
                    <startTime xsi:type="xsd:string">2021-07-01T00:00:00</startTime>
                    <endTime xsi:type="xsd:string">2025-06-30T00:00:00</endTime>
                    <Unit xsi:type="xsd:string">e</Unit>
                    <weatherParameters>
                        <maxt xsi:type="xsd:boolean">1</maxt>
                        <mint xsi:type="xsd:boolean">0</mint>
                        <temp xsi:type="xsd:boolean">0</temp>
                        <td xsi:type="xsd:boolean">0</td>
                        <pop12 xsi:type="xsd:boolean">0</pop12>
                        <qpf xsi:type="xsd:boolean">0</qpf>
                        <sky xsi:type="xsd:boolean">0</sky>
                        <snow xsi:type="xsd:boolean">0</snow>
                        <wspd xsi:type="xsd:boolean">0</wspd>
                        <wdir xsi:type="xsd:boolean">0</wdir>
                        <wx xsi:type="xsd:boolean">0</wx>
                        <waveh xsi:type="xsd:boolean">0</waveh>
                        <icons xsi:type="xsd:boolean">0</icons>
                        <critfireo xsi:type="xsd:boolean">0</critfireo>
                        <dryfireo xsi:type="xsd:boolean">0</dryfireo>
                        <rhm xsi:type="xsd:boolean">0</rhm>
                        <apt xsi:type="xsd:boolean">0</apt>
                        <tcwspdabv34i xsi:type="xsd:boolean">0</tcwspdabv34i>
                        <tcwspdabv50i xsi:type="xsd:boolean">0</tcwspdabv50i>
                        <tcwspdabv64i xsi:type="xsd:boolean">0</tcwspdabv64i>
                        <tcwspdabv34c xsi:type="xsd:boolean">0</tcwspdabv34c>
                        <tcwspdabv50c xsi:type="xsd:boolean">0</tcwspdabv50c>
                        <tcwspdabv64c xsi:type="xsd:boolean">0</tcwspdabv64c>
                        <conhazo xsi:type="xsd:boolean">0</conhazo>
                        <ptornado xsi:type="xsd:boolean">0</ptornado>
                        <phail xsi:type="xsd:boolean">0</phail>
                        <ptstmwinds xsi:type="xsd:boolean">0</ptstmwinds>
                        <pxtornado xsi:type="xsd:boolean">0</pxtornado>
                        <pxhail xsi:type="xsd:boolean">0</pxhail>
                        <pxtstmwinds xsi:type="xsd:boolean">0</pxtstmwinds>
                        <ptotsvrtstm xsi:type="xsd:boolean">0</ptotsvrtstm>
                        <ptotxsvrtstm xsi:type="xsd:boolean">0</ptotxsvrtstm>
                        <tmpabv14d xsi:type="xsd:boolean">0</tmpabv14d>
                        <tmpblw14d xsi:type="xsd:boolean">0</tmpblw14d>
                        <tmpabv30d xsi:type="xsd:boolean">0</tmpabv30d>
                        <tmpblw30d xsi:type="xsd:boolean">0</tmpblw30d>
                        <tmpabv90d xsi:type="xsd:boolean">0</tmpabv90d>
                        <tmpblw90d xsi:type="xsd:boolean">0</tmpblw90d>
                        <prcpabv14d xsi:type="xsd:boolean">0</prcpabv14d>
                        <prcpblw14d xsi:type="xsd:boolean">0</prcpblw14d>
                        <prcpabv30d xsi:type="xsd:boolean">0</prcpabv30d>
                        <prcpblw30d xsi:type="xsd:boolean">0</prcpblw30d>
                        <prcpabv90d xsi:type="xsd:boolean">0</prcpabv90d>
                        <prcpblw90d xsi:type="xsd:boolean">0</prcpblw90d>
                        <precipa_r xsi:type="xsd:boolean">0</precipa_r>
                        <sky_r xsi:type="xsd:boolean">0</sky_r>
                        <td_r xsi:type="xsd:boolean">0</td_r>
                        <temp_r xsi:type="xsd:boolean">0</temp_r>
                        <wdir_r xsi:type="xsd:boolean">0</wdir_r>
                        <wspd_r xsi:type="xsd:boolean">0</wspd_r>
                        <wgust xsi:type="xsd:boolean">0</wgust>
                        <iceaccum xsi:type="xsd:boolean">0</iceaccum>
                        <maxrh xsi:type="xsd:boolean">0</maxrh>
                        <minrh xsi:type="xsd:boolean">0</minrh>
                    </weatherParameters>
                </ns3591:NDFDgen>
            </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>"""


# HTTP request to the server
response = requests.post(url,data=body,headers=headers)


# Processing the SOAP response received from server
text = response.text

location = "C:/xampp/htdocs/WeatherInfo.xml"


# # Response received has XML file inserted into another xml body.
# # We are only interested in the inner xml.

# # Run the code below to save and view raw xml response. 

# with open("raw.xml", "w") as raw:
#     raw.write(text)


# Remove additional xml tags provided from the server.

file = open(location,"w")
for i in range(len(text)):
    temp = "&lt"
    if(text[i]+text[i+1]+text[i+2] == temp):
        temp2 = "</dwmlO"
        for j in range(i,len(text)):
            if(text[j]+text[j+1]+text[j+2]+text[j+3]+text[j+4]+text[j+5]+text[j+6] != temp2):
                file.write(text[j])
            else:
                break
        break
    
file.close()    


with open(location) as f:
    s = f.read()
with open(location,"w") as f:
    s = s.replace("&lt;","<")
    s = s.replace("&gt;", ">")
    s = s.replace("&quot;",'"') 
    f.write(s)

