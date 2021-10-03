import requests
import datetime
import smtplib

MY_LAT = 50.747234
MY_LON = 25.325382

response_ISS = requests.get("http://api.open-notify.org/iss-now.json")
response_ISS.raise_for_status()
data_ISS = response_ISS.json()
print(data_ISS)
ISS_lat = float(data_ISS["iss_position"]["latitude"])
ISS_lon = float(data_ISS["iss_position"]["longitude"])
print(ISS_lon, ISS_lat)


parameters = {
    "lat":MY_LAT,
    "lng":MY_LON ,
    "formatted": 0
}
response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()
data_sun = response_sun.json()
sunrise = response_sun.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response_sun.json()["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = int(sunrise)
sunset = int(sunset)
print(data_sun)
print(sunrise, sunset)

now = datetime.datetime.now()
current_hour = now.hour
UTC_current_time = current_hour-3

if UTC_current_time > sunset or UTC_current_time < sunrise:
    if MY_LAT - ISS_lat < 5 and MY_LON - ISS_lon < 5:
        sender_email = "yura.atreusovich@gmail.com"
        sender_password = "SmertMoskalam1"
        with smtplib.SMTP("mail.google.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            connection.sendmail(from_addr=sender_email, to_addrs="yura.fedonyuk@gmail.com",
                                msg="Subject: Look Up!👆\n\nLook! The ISS is just above your location and you can see it!")
