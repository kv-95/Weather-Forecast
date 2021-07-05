<===================== READ ME =====================>

THIS IS A WEATHER FORECAST APPLICATION MADE IN PYTHON.
THE APPLICATION SENDS A SOAP REQUEST TO NDFD SERVER AND RECIEVES A SOAP RESPONSE.
THE RESPONSE WILL INCLUDE THE FORECAST DATA PROVIDED BY THE NWS.

FOR MORE INFORMATION VISIT - https://graphical.weather.gov/xml/

THE APPLICATION IS INTENDED FOR LEARNING SOAP XML REQUEST/RESPONSE. 



/* CONTENTS :

WeatherForecast.py - PYTHON APPLICATION TO SEND SOAP REQUEST TO WEATHER INFORMATION SERVER 
		     AND RETRIEVE SOAP RESPONSE AND SAVE IT ON LOCAL DEVICE.
WeatherInfo.xml    - A SAMPLE SOAP XML RESPONSE FROM SERVER.

*/

/* INSTRUCTIONS TO RUN APPLICATION

1. OPEN 'WeatherForecast.py' IN A CODE EDITOR.
2. RUN THE APPLICATION.
	THE OUTPUT WILL BE GENERATED AT THE END OF EXECUTION.
*/

/* INSTRUCTION TO VIEW XML

METHOD - USING XAMPP (APACHE)

1. RUN THE PYTHON APPLICATION
2. RUN APACHE SERVER 
3. OPEN BRWSER AND GO TO "http://localhost/WeatherInfo.xml"

METHOD - OPEN XML MANUALLY

1. OPEN CODE IN PYTHON EDITOR
2. CHANGE " location = "C:/xampp/htdocs/WeatherInfo.xml" " TO " location = "WeatherInfo.xml "
   AT LINE 88
3. XML FILE WILL BE GENERATED ON THE SAME FOLDER WHERE CODE IS PRESENT.
4. OPEN THE XML USING A BROWSER
*/

