# Hotel-Management-System
Hotel Management System for managing general activities of a hotel like booking of rooms, billing etc.

Hotel Reservation Management System
In this app services like multiple Bookings in certain hotels are carried out. 
In each hotel there are multiple tasks about specific rooms. 
So basically a customer can book a room in the respected hotel.
Processes and services:Room is booked by a Customer with an option to vacate on the desired date.
If a new customer is trying to book a specific room which is already booked by some other customer then the new customer will be alerted with an error and the room will not be available until the existing customer vacates it.
I have implemented the concept of post_save so that as soon the room is vacated and the room is shown available for the upcoming booking customers.
A customer can book only one room at a time.
To run this in your system:Clone this repo in your system:git clone https://github.com/patrickikhidero/Hotel-Management-System.gitGet inside the repo, type this is terminal:cd  Hotel-Management-SystemCreate a virtual environment inside the repo:python3 -m venv .venvAfter that activate the virtual environment by typing:source .venv/bin/activate.

Next step is to install all the dependencies into your virtual environment:pip3 installDjango==3.2.9Next get into the project directory by typing:cd hrmsType 3 commands in order before for the project to run:python3 manage.py makemigrations python3 manage.py migrate Now to access the admin page before running the server create a superuser:python3 manage.py createsuperuser fill the details :username: <ur choice>email: <optional>password: <password>confirm password: <confirm the password>After filling all these to run the project:python3 manage.py runserverthe app runs in the template mode. Open http://127.0.0.1:8000 to view it in the browser.

GitHub - rub9542/Hotel-Reservation-Management-System: Web Applictaion designed for Hotel Reservation Management System Using Django, REST API

Web Applictaion designed for Hotel Reservation Management System Using Django, REST API - GitHub - rub9542/Hotel-Reservation-Management-System: Web Applictaion designed for Hotel Reservation Manage...

