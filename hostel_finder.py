import streamlit as st
from streamlit.components.v1 import html

# HTML and JavaScript code
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indian Hostel Finder</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
        }

        header {
            background-color: #1a73e8;
            color: white;
            padding: 1rem;
            text-align: center;
        }

        .container {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            padding: 1rem;
        }

        .search-box {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .search-form {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .form-group {
            flex: 1;
            min-width: 200px;
        }

        input, select, button {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        button {
            background: #1a73e8;
            color: white;
            border: none;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        button:hover {
            background: #1557b0;
        }

        .utility-buttons {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }

        .results {
            display: grid;
            gap: 1rem;
        }

        .hostel-card {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .hostel-card button {
            margin-top: 0.5rem;
        }

        #map {
            height: 400px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        #loading {
            display: none;
            text-align: center;
            padding: 1rem;
        }

        @media (max-width: 768px) {
            .search-form {
                flex-direction: column;
            }

            #map {
                height: 300px;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Indian Hostel Finder</h1>
    </header>

    <div class="container">
        <div class="search-box">
            <form class="search-form" id="searchForm">
                <div class="form-group">
                    <input type="text" id="location" placeholder="Enter city or area">
                </div>
                <div class="form-group">
                    <select id="radius">
                        <option value="5">5 km</option>
                        <option value="10">10 km</option>
                        <option value="20">20 km</option>
                        <option value="50">50 km</option>
                    </select>
                </div>
                <div class="form-group">
                    <select id="sortBy">
                        <option value="price">Price: Low to High</option>
                        <option value="rating">Rating: High to Low</option>
                        <option value="distance">Distance: Near to Far</option>
                    </select>
                </div>
                <div class="utility-buttons">
                    <button type="submit">Search</button>
                    <button type="button" id="shareLocation">Use My Location</button>
                    <button type="button" id="resetButton">Reset</button>
                </div>
            </form>
        </div>

        <div id="loading">Searching hostels...</div>
        <div id="map"></div>
        <div class="results" id="results"></div>
    </div>

    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <script>
        // Initialize map centered on India
        let map = L.map('map').setView([20.5937, 78.9629], 5);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

        // Custom hostel icon
        const hostelIcon = L.icon({
            iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
            iconSize: [25, 41],
            iconAnchor: [12, 41]
        });

        // Hostel data
        const hostels = [
            // Delhi
            { 
                name: "Backpacker Panda Delhi", 
                lat: 28.7041, 
                lng: 77.1025,
                price: "₹18,000", 
                rating: 4.5, 
                address: "Majnu Ka Tila, New Delhi",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "GoStops Delhi", 
                lat: 28.6139, 
                lng: 77.2090,
                price: "₹20,000", 
                rating: 4.6, 
                address: "Connaught Place, New Delhi",
                amenities: "Female Dorms, Co-working Space",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Delhi", 
                lat: 28.5355, 
                lng: 77.2590,
                price: "₹22,000", 
                rating: 4.8, 
                address: "Saket, New Delhi",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            },
            { 
                name: "Moustache Delhi", 
                lat: 28.6280, 
                lng: 77.2069,
                price: "₹19,500", 
                rating: 4.7, 
                address: "Hauz Khas, New Delhi",
                amenities: "AC Dorms, Bar, Events",
                contact: generateRandomContact()
            },
            { 
                name: "Zostel Delhi", 
                lat: 28.6542, 
                lng: 77.2373,
                price: "₹21,000", 
                rating: 4.9, 
                address: "Paharganj, New Delhi",
                amenities: "Mixed Dorms, Free Breakfast",
                contact: generateRandomContact()
            },

            // Mumbai
            { 
                name: "Zostel Mumbai", 
                lat: 19.0760, 
                lng: 72.8777,
                price: "₹24,000", 
                rating: 4.7, 
                address: "Colaba, Mumbai",
                amenities: "AC Dorms, Free WiFi, Common Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Mumbai", 
                lat: 19.1077, 
                lng: 72.8317,
                price: "₹22,500", 
                rating: 4.6, 
                address: "Andheri, Mumbai",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Mumbai", 
                lat: 19.0176, 
                lng: 72.8561,
                price: "₹23,000", 
                rating: 4.8, 
                address: "Bandra, Mumbai",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            },

            // Chennai
            { 
                name: "Zostel Chennai", 
                lat: 13.0827, 
                lng: 80.2707,
                price: "₹18,000", 
                rating: 4.5, 
                address: "Egmore, Chennai",
                amenities: "AC Dorms, Free WiFi, Common Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Chennai", 
                lat: 12.9716, 
                lng: 80.2212,
                price: "₹17,500", 
                rating: 4.4, 
                address: "Adyar, Chennai",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Chennai", 
                lat: 13.0604, 
                lng: 80.2494,
                price: "₹19,000", 
                rating: 4.7, 
                address: "T. Nagar, Chennai",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            },

            // Kolkata
            { 
                name: "Zostel Kolkata", 
                lat: 22.5726, 
                lng: 88.3639,
                price: "₹16,000", 
                rating: 4.5, 
                address: "Park Street, Kolkata",
                amenities: "AC Dorms, Free WiFi, Common Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Kolkata", 
                lat: 22.5358, 
                lng: 88.3474,
                price: "₹15,500", 
                rating: 4.4, 
                address: "Salt Lake, Kolkata",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Kolkata", 
                lat: 22.4964, 
                lng: 88.3072,
                price: "₹17,000", 
                rating: 4.6, 
                address: "Howrah, Kolkata",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            },

            // Greater Noida
            { 
                name: "Pakhi Nest", 
                lat: 28.4744, 
                lng: 77.5040,
                price: "₹25,000", 
                rating: 4.5, 
                address: "Knowledge Park III, Greater Noida",
                amenities: "AC Dorms, Free WiFi, Common Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "EZ Stays", 
                lat: 28.4595, 
                lng: 77.5276,
                price: "₹16,500", 
                rating: 4.4, 
                address: "Alpha Commercial Belt, Greater Noida",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "Stanza Living", 
                lat: 28.4702, 
                lng: 77.4987,
                price: "₹20,000", 
                rating: 4.6, 
                address: "Tech Zone IV, Greater Noida",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            },

            // Pune
            { 
                name: "Zostel Pune", 
                lat: 18.5204, 
                lng: 73.8567,
                price: "₹19,000", 
                rating: 4.6, 
                address: "Koregaon Park, Pune",
                amenities: "AC Dorms, Free WiFi, Common Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Pune", 
                lat: 18.5167, 
                lng: 73.8562,
                price: "₹18,500", 
                rating: 4.5, 
                address: "Shivajinagar, Pune",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Pune", 
                lat: 18.5590, 
                lng: 73.7868,
                price: "₹20,000", 
                rating: 4.7, 
                address: "Hinjewadi, Pune",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            },

            // Bangalore
            { 
                name: "Zostel Bangalore", 
                lat: 12.9716, 
                lng: 77.5946,
                price: "₹21,000", 
                rating: 4.7, 
                address: "Indiranagar, Bangalore",
                amenities: "AC Dorms, Free WiFi, Common Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Bangalore", 
                lat: 12.9788, 
                lng: 77.5997,
                price: "₹20,500", 
                rating: 4.6, 
                address: "Koramangala, Bangalore",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Bangalore", 
                lat: 12.9352, 
                lng: 77.6245,
                price: "₹22,000", 
                rating: 4.8, 
                address: "Electronic City, Bangalore",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            },

            // Hyderabad
            { 
                name: "Zostel Hyderabad", 
                lat: 17.3850, 
                lng: 78.4867,
                price: "₹18,500", 
                rating: 4.6, 
                address: "Gachibowli, Hyderabad",
                amenities: "AC Dorms, Free WiFi, Common Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Hyderabad", 
                lat: 17.4375, 
                lng: 78.4482,
                price: "₹18,000", 
                rating: 4.5, 
                address: "Secunderabad, Hyderabad",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Hyderabad", 
                lat: 17.4062, 
                lng: 78.4690,
                price: "₹19,500", 
                rating: 4.7, 
                address: "Hitech City, Hyderabad",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            },

            // Patna
            { 
                name: "Zostel Patna", 
                lat: 25.5941, 
                lng: 85.1376,
                price: "₹15,000", 
                rating: 4.4, 
                address: "Fraser Road, Patna",
                amenities: "AC Dorms, Free WiFi, Common Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Patna", 
                lat: 25.6093, 
                lng: 85.1235,
                price: "₹14,500", 
                rating: 4.3, 
                address: "Kankarbagh, Patna",
                amenities: "Mixed Dorms, Cafe, Laundry",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Patna", 
                lat: 25.6154, 
                lng: 85.1356,
                price: "₹16,000", 
                rating: 4.5, 
                address: "Patliputra, Patna",
                amenities: "Private Rooms, Rooftop Cafe",
                contact: generateRandomContact()
            }
        ];

        // Helper functions
        function generateRandomContact() {
            const prefix = "+91";
            const firstDigit = Math.floor(Math.random() * 9) + 1;
            const remainingDigits = Math.floor(100000000 + Math.random() * 900000000);
            return `${prefix} ${firstDigit}${remainingDigits}`;
        }

        function calculateDistance(lat1, lon1, lat2, lon2) {
            const R = 6371;
            const dLat = (lat2 - lat1) * (Math.PI / 180);
            const dLon = (lon2 - lon1) * (Math.PI / 180);
            const a =
                Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                Math.cos(lat1 * (Math.PI / 180)) * Math.cos(lat2 * (Math.PI / 180)) *
                Math.sin(dLon / 2) * Math.sin(dLon / 2);
            const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
            return R * c;
        }

        // Search functionality
        async function searchHostels(location, radius) {
            const loading = document.getElementById('loading');
            loading.style.display = 'block';

            try {
                const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${location}`);
                if (!response.ok) throw new Error('Network error');
                const data = await response.json();
                
                if (data.length === 0) {
                    alert('Location not found');
                    return [];
                }

                const userLat = parseFloat(data[0].lat);
                const userLng = parseFloat(data[0].lon);
                
                console.log("User Location:", userLat, userLng); // Debugging log

                localStorage.setItem('lastLocation', location);
                localStorage.setItem('lastRadius', radius);

                const filteredHostels = hostels
                    .map(hostel => ({
                        ...hostel,
                        distance: calculateDistance(userLat, userLng, hostel.lat, hostel.lng)
                    }))
                    .filter(hostel => hostel.distance <= radius)
                    .sort((a, b) => a.distance - b.distance);

                console.log("Filtered Hostels:", filteredHostels); // Debugging log

                return filteredHostels;

            } catch (error) {
                console.error('Search error:', error);
                alert('Error searching hostels');
                return [];
            } finally {
                loading.style.display = 'none';
            }
        }

        // Display results
        function showResults(hostels) {
            const resultsContainer = document.getElementById('results');
            resultsContainer.innerHTML = '';

            if (hostels.length === 0) {
                resultsContainer.innerHTML = '<p>No hostels found. Try increasing search radius.</p>';
                return;
            }

            hostels.forEach(hostel => {
                const card = document.createElement('div');
                card.className = 'hostel-card';
                card.innerHTML = `
                    <h3>${hostel.name}</h3>
                    <p><strong>Price:</strong> ${hostel.price}</p>
                    <p><strong>Rating:</strong> ${hostel.rating} ★</p>
                    <p><strong>Distance:</strong> ${hostel.distance.toFixed(1)} km</p>
                    <p><strong>Address:</strong> ${hostel.address}</p>
                    <p><strong>Contact:</strong> ${hostel.contact}</p>
                    <button onclick="showOnMap(${hostel.lat}, ${hostel.lng})">Show on Map</button>
                `;
                resultsContainer.appendChild(card);
            });
        }

        // Map functions
        function updateMap(hostels) {
            map.eachLayer(layer => layer instanceof L.Marker && map.removeLayer(layer));
            hostels.forEach(hostel => {
                L.marker([hostel.lat, hostel.lng], { icon: hostelIcon })
                    .addTo(map)
                    .bindPopup(`<b>${hostel.name}</b><br>${hostel.price}`);
            });
        }

        function showOnMap(lat, lng) {
            map.setView([lat, lng], 15);
        }

        // Event handlers
        document.getElementById('searchForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const location = document.getElementById('location').value;
            const radius = parseInt(document.getElementById('radius').value);
            const hostels = await searchHostels(location, radius);
            updateMap(hostels);
            showResults(hostels);
        });

        document.getElementById('resetButton').addEventListener('click', () => {
            document.getElementById('location').value = '';
            document.getElementById('radius').value = '5';
            localStorage.removeItem('lastLocation');
            localStorage.removeItem('lastRadius');
            showResults(hostels);
            updateMap(hostels);
            map.setView([20.5937, 78.9629], 5);
        });

        document.getElementById('shareLocation').addEventListener('click', () => {
            if (!navigator.geolocation) {
                alert('Geolocation not supported');
                return;
            }

            navigator.geolocation.getCurrentPosition(async (position) => {
                const { latitude, longitude } = position.coords;
                const response = await fetch(
                    `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`
                );
                const data = await response.json();
                document.getElementById('location').value = data.address.city || data.address.town;
                document.getElementById('searchForm').dispatchEvent(new Event('submit'));
            });
        });

        document.getElementById('sortBy').addEventListener('change', function() {
            const sortBy = this.value;
            const sortedHostels = [...hostels].sort((a, b) => {
                if (sortBy === 'price') {
                    return parseFloat(a.price.replace(/\D/g, '')) - parseFloat(b.price.replace(/\D/g, ''));
                }
                if (sortBy === 'rating') return b.rating - a.rating;
                return a.distance - b.distance;
            });
            showResults(sortedHostels);
        });

        // Initial load
        window.addEventListener('load', () => {
            const lastLocation = localStorage.getItem('lastLocation');
            const lastRadius = localStorage.getItem('lastRadius');
            if (lastLocation && lastRadius) {
                document.getElementById('location').value = lastLocation;
                document.getElementById('radius').value = lastRadius;
                document.getElementById('searchForm').dispatchEvent(new Event('submit'));
            } else {
                showResults(hostels);
                updateMap(hostels);
            }
        });
    </script>
</body>
</html>
"""

# Render the HTML in Streamlit
st.title("Indian Hostel Finder")
html(html_code, height=800, scrolling=True)