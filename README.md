# Nearby-hostel-finder
# Indian Hostel Finder 🏠📍

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=Leaflet&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EBC6F?style=for-the-badge&logo=OpenStreetMap&logoColor=white)

The **Indian Hostel Finder** is a web application designed to help users search for hostels across various cities in India. It provides a user-friendly interface to search for hostels by location, filter results by radius, and sort them by price, rating, or distance. The app also integrates a map to visually display hostel locations and allows users to view hostel details.

---

## Features ✨

1. **Search Hostels by Location**:
   - Enter a city or area to find hostels within a specified radius (5 km, 10 km, 20 km, or 50 km).
2. **Use My Location**:
   - Automatically detect the user's current location and search for nearby hostels.
3. **Sort Results**:
   - Sort hostels by:
     - Price (Low to High)
     - Rating (High to Low)
     - Distance (Near to Far)
4. **Interactive Map**:
   - Hostels are displayed as markers on a map powered by **Leaflet.js** and **OpenStreetMap**.
   - Click on a hostel marker to view its name and price.
5. **Hostel Details**:
   - View hostel details such as name, price, rating, distance, address, amenities, and contact information.
6. **Reset Functionality**:
   - Reset the search and map to the default view.
7. **Responsive Design**:
   - The app is optimized for both desktop and mobile devices.

---

## Technologies Used 🛠️

- **Frontend**:
  - HTML, CSS, JavaScript
  - [Leaflet.js](https://leafletjs.com/) for interactive maps
  - [OpenStreetMap](https://www.openstreetmap.org/) for map tiles
- **Backend**:
  - [Streamlit](https://streamlit.io/) for rendering the web app
- **APIs**:
  - [Nominatim (OpenStreetMap)](https://nominatim.openstreetmap.org/) for geolocation and reverse geocoding

---

## Setup Instructions 🚀

### Prerequisites

1. **Python 3.7 or higher** installed on your system.
2. **Streamlit** installed. If not, install it using:
   ```bash
   pip install streamlit
   Steps to Run the Project

Clone the Repository:
bash
Copy
git clone https://github.com/your-username/Nearby-hostel-finder.git
cd indian-hostel-finder
Run the Streamlit App:
bash
Copy
streamlit run hostel_finder.py
Access the App:
Open your browser and navigate to the URL provided in the terminal (usually http://localhost:8501).
How to Use 🕹️

Search for Hostels:
Enter a city or area in the search bar and select a radius.
Click the Search button to view hostels within the specified radius.
Use My Location:
Click the Use My Location button to automatically detect your current location and search for nearby hostels.
Sort Results:
Use the dropdown menu to sort hostels by price, rating, or distance.
View on Map:
Click the Show on Map button on any hostel card to center the map on that hostel and scroll the page to the map.
Reset:
Click the Reset button to clear the search and reset the map to the default view.
Project Structure 📂

Copy
indian-hostel-finder/
├── hostel_finder.py       # Main Streamlit app file
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies (if any)


Future Enhancements 🔮

Integration with a Backend API:
Replace hardcoded hostel data with a backend API to fetch real-time hostel information.
User Authentication:
Allow users to create accounts, save favorite hostels, and leave reviews.
Advanced Filters:
Add filters for amenities (e.g., WiFi, AC, laundry) and hostel types (e.g., male-only, female-only).
Booking System:
Integrate a booking system to allow users to reserve hostels directly from the app.
Contributing 🤝

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push them to your fork.
Submit a pull request with a detailed description of your changes.
License 📜

This project is licensed under the MIT License. See the LICENSE file for details.

Contact 📧

For any questions or feedback, feel free to reach out:

Email: hemantchaudhary1236@gmail.com
GitHub: hemant6939
Enjoy using the Indian Hostel Finder! 🚀
