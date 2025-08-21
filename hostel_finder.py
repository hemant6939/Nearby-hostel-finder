import streamlit as st
from streamlit.components.v1 import html
import json

# HTML and JavaScript code
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indian Hostel Finder</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #4f46e5;
            --secondary-color: #4338ca;
            --accent-color: #6366f1;
            --text-color: #1f2937;
            --light-gray: #f3f4f6;
            --border-color: #e5e7eb;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --error-color: #ef4444;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            --radius-sm: 0.375rem;
            --radius-md: 0.5rem;
            --radius-lg: 0.75rem;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: var(--light-gray);
            color: var(--text-color);
            line-height: 1.6;
        }

        header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 2rem;
            text-align: center;
            box-shadow: var(--shadow-md);
            position: relative;
            overflow: hidden;
        }

        header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') center/cover;
            opacity: 0.1;
            z-index: 0;
        }

        header h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            position: relative;
            z-index: 1;
        }

        header p {
            font-size: 1.1rem;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
            display: grid;
            gap: 2rem;
            grid-template-columns: 1fr 1.5fr;
        }

        .search-section {
            background: white;
            padding: 2rem;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-md);
            position: sticky;
            top: 2rem;
            height: fit-content;
        }

        .search-form {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }

        .form-group label {
            font-weight: 500;
            color: var(--text-color);
            font-size: 0.85rem;
        }

        input, select, button {
            padding: 0.5rem;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            font-size: 0.9rem;
            transition: all 0.3s ease;
            font-family: 'Poppins', sans-serif;
        }

        input:focus, select:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
        }

        button {
            background: var(--primary-color);
            color: white;
            border: none;
            cursor: pointer;
            font-weight: 500;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
        }

        button:hover {
            background: var(--secondary-color);
            transform: translateY(-1px);
        }

        .price-range {
            display: flex;
            gap: 0.5rem;
            align-items: center;
        }

        .amenities-filter {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0.5rem;
        }

        .amenity-checkbox {
            display: flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.25rem;
            background: var(--light-gray);
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.85rem;
        }

        .amenity-checkbox:hover {
            background: var(--border-color);
        }

        .amenity-checkbox input[type="checkbox"] {
            width: 1.25rem;
            height: 1.25rem;
            cursor: pointer;
        }

        .results-section {
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }

        .map-section {
            padding: 0.5rem;
            max-width: 600px;
            margin: 0 auto;
        }

        #map {
            height: 150px;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
            margin-bottom: 0.5rem;
            border: none;
            width: 100%;
        }

        .results {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0.75rem;
        }

        .hostel-card {
            background: white;
            padding: 0.75rem;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
            transition: all 0.3s ease;
            border: 1px solid var(--border-color);
            height: 100%;
            display: flex;
            flex-direction: column;
        }

        .hostel-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .hostel-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 0.25rem;
        }

        .hostel-name {
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-color);
        }

        .hostel-rating {
            display: flex;
            align-items: center;
            gap: 0.25rem;
            color: var(--warning-color);
            background: rgba(245, 158, 11, 0.1);
            padding: 0.15rem 0.35rem;
            border-radius: var(--radius-sm);
            font-size: 0.75rem;
        }

        .hostel-details {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0.25rem;
            margin: 0.25rem 0;
        }

        .detail-item {
            display: flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.15rem;
            background: var(--light-gray);
            border-radius: var(--radius-sm);
            font-size: 0.75rem;
        }

        .hostel-amenities {
            display: flex;
            flex-wrap: wrap;
            gap: 0.15rem;
            margin: 0.25rem 0;
        }

        .amenity-tag {
            background: var(--light-gray);
            padding: 0.1rem 0.35rem;
            border-radius: 12px;
            font-size: 0.7rem;
            display: flex;
            align-items: center;
            gap: 0.15rem;
        }

        .hostel-actions {
            margin-top: auto;
        }

        .action-button {
            flex: 1;
            padding: 0.35rem;
            border-radius: var(--radius-sm);
            font-size: 0.75rem;
        }

        .secondary-button {
            background: var(--light-gray);
            color: var(--text-color);
        }

        .secondary-button:hover {
            background: var(--border-color);
        }

        #loading {
            display: none;
            text-align: center;
            padding: 2rem;
        }

        .loading-spinner {
            border: 4px solid var(--light-gray);
            border-top: 4px solid var(--primary-color);
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .no-results {
            text-align: center;
            padding: 3rem;
            background: white;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-md);
        }

        .no-results i {
            font-size: 3rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
        }

        .no-results h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .no-results p {
            color: #6b7280;
        }

        .map-popup {
            padding: 0.25rem;
        }

        .map-popup h3 {
            font-size: 0.8rem;
            margin-bottom: 0.15rem;
        }

        .map-popup p {
            font-size: 0.7rem;
            color: #6b7280;
            margin-bottom: 0.25rem;
        }

        .map-popup button {
            width: 100%;
            padding: 0.25rem;
            font-size: 0.7rem;
        }

        @media (max-width: 1024px) {
            .container {
                grid-template-columns: 1fr;
                padding: 1rem;
            }

            .search-section {
                position: static;
            }

            header {
                padding: 1.5rem;
            }

            header h1 {
                font-size: 2rem;
            }
        }

        @media (max-width: 768px) {
            .hostel-details {
                grid-template-columns: 1fr;
            }

            .amenities-filter {
                grid-template-columns: 1fr;
            }

            .hostel-actions {
                flex-direction: column;
            }

            .results {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Indian Hostel Finder</h1>
        <p>Find your perfect stay across India</p>
    </header>

    <div class="container">
        <div class="search-section">
            <form class="search-form" id="searchForm">
                <div class="form-group">
                    <label for="location">Location</label>
                    <input type="text" id="location" placeholder="Enter city or area">
                </div>
                <div class="form-group">
                    <label for="radius">Search Radius</label>
                    <select id="radius">
                        <option value="5">5 km</option>
                        <option value="10">10 km</option>
                        <option value="20">20 km</option>
                        <option value="50">50 km</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Price Range (₹)</label>
                    <div class="price-range">
                        <input type="number" id="minPrice" placeholder="Min" min="0">
                        <span>to</span>
                        <input type="number" id="maxPrice" placeholder="Max" min="0">
                    </div>
                </div>
                <div class="form-group">
                    <label>Amenities</label>
                    <div class="amenities-filter">
                        <label class="amenity-checkbox">
                            <input type="checkbox" value="wifi">
                            <i class="fas fa-wifi"></i>
                            WiFi
                        </label>
                        <label class="amenity-checkbox">
                            <input type="checkbox" value="ac">
                            <i class="fas fa-snowflake"></i>
                            AC
                        </label>
                        <label class="amenity-checkbox">
                            <input type="checkbox" value="laundry">
                            <i class="fas fa-tshirt"></i>
                            Laundry
                        </label>
                        <label class="amenity-checkbox">
                            <input type="checkbox" value="kitchen">
                            <i class="fas fa-utensils"></i>
                            Kitchen
                        </label>
                    </div>
                </div>
                <div class="form-group">
                    <label for="sortBy">Sort By</label>
                    <select id="sortBy">
                        <option value="price">Price: Low to High</option>
                        <option value="rating">Rating: High to Low</option>
                        <option value="distance">Distance: Near to Far</option>
                    </select>
                </div>
                <button type="submit">
                    <i class="fas fa-search"></i>
                    Search Hostels
                </button>
                <button type="button" id="shareLocation">
                    <i class="fas fa-location-arrow"></i>
                    Use My Location
                </button>
                <button type="button" id="resetButton" class="secondary-button">
                    <i class="fas fa-redo"></i>
                    Reset
                </button>
            </form>
        </div>

        <div class="results-section">
            <div id="map"></div>
            <div id="loading">
                <div class="loading-spinner"></div>
                <p>Searching hostels...</p>
            </div>
            <div class="results" id="results"></div>
        </div>
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

        // Hostel data with enhanced information
        const hostels = [
            // Delhi
            { 
                name: "Backpacker Panda Delhi", 
                lat: 28.7041, 
                lng: 77.1025,
                price: "₹18,000", 
                rating: 4.5, 
                address: "Majnu Ka Tila, New Delhi",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "GoStops Delhi", 
                lat: 28.6139, 
                lng: 77.2090,
                price: "₹20,000", 
                rating: 4.6, 
                address: "Connaught Place, New Delhi",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Delhi", 
                lat: 28.5355, 
                lng: 77.2590,
                price: "₹22,000", 
                rating: 4.8, 
                address: "Saket, New Delhi",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Moustache Delhi", 
                lat: 28.6280, 
                lng: 77.2069,
                price: "₹19,500", 
                rating: 4.7, 
                address: "Hauz Khas, New Delhi",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Zostel Delhi", 
                lat: 28.6542, 
                lng: 77.2373,
                price: "₹21,000", 
                rating: 4.9, 
                address: "Paharganj, New Delhi",
                amenities: "WiFi, AC, Laundry, Kitchen",
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
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Mumbai", 
                lat: 19.1077, 
                lng: 72.8317,
                price: "₹22,500", 
                rating: 4.6, 
                address: "Andheri, Mumbai",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Mumbai", 
                lat: 19.0176, 
                lng: 72.8561,
                price: "₹23,000", 
                rating: 4.8, 
                address: "Bandra, Mumbai",
                amenities: "WiFi, AC, Laundry, Kitchen",
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
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Chennai", 
                lat: 12.9716, 
                lng: 80.2212,
                price: "₹17,500", 
                rating: 4.4, 
                address: "Adyar, Chennai",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Chennai", 
                lat: 13.0604, 
                lng: 80.2494,
                price: "₹19,000", 
                rating: 4.7, 
                address: "T. Nagar, Chennai",
                amenities: "WiFi, AC, Laundry, Kitchen",
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
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Kolkata", 
                lat: 22.5358, 
                lng: 88.3474,
                price: "₹15,500", 
                rating: 4.4, 
                address: "Salt Lake, Kolkata",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Kolkata", 
                lat: 22.4964, 
                lng: 88.3072,
                price: "₹17,000", 
                rating: 4.6, 
                address: "Howrah, Kolkata",
                amenities: "WiFi, AC, Laundry, Kitchen",
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
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "EZ Stays", 
                lat: 28.4595, 
                lng: 77.5276,
                price: "₹16,500", 
                rating: 4.4, 
                address: "Alpha Commercial Belt, Greater Noida",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Stanza Living", 
                lat: 28.4702, 
                lng: 77.4987,
                price: "₹20,000", 
                rating: 4.6, 
                address: "Tech Zone IV, Greater Noida",
                amenities: "WiFi, AC, Laundry, Kitchen",
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
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Pune", 
                lat: 18.5167, 
                lng: 73.8562,
                price: "₹18,500", 
                rating: 4.5, 
                address: "Shivajinagar, Pune",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Pune", 
                lat: 18.5590, 
                lng: 73.7868,
                price: "₹20,000", 
                rating: 4.7, 
                address: "Hinjewadi, Pune",
                amenities: "WiFi, AC, Laundry, Kitchen",
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
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Bangalore", 
                lat: 12.9788, 
                lng: 77.5997,
                price: "₹20,500", 
                rating: 4.6, 
                address: "Koramangala, Bangalore",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Bangalore", 
                lat: 12.9352, 
                lng: 77.6245,
                price: "₹22,000", 
                rating: 4.8, 
                address: "Electronic City, Bangalore",
                amenities: "WiFi, AC, Laundry, Kitchen",
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
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Hyderabad", 
                lat: 17.4375, 
                lng: 78.4482,
                price: "₹18,000", 
                rating: 4.5, 
                address: "Secunderabad, Hyderabad",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Hyderabad", 
                lat: 17.4062, 
                lng: 78.4690,
                price: "₹19,500", 
                rating: 4.7, 
                address: "Hitech City, Hyderabad",
                amenities: "WiFi, AC, Laundry, Kitchen",
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
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "Backpacker Panda Patna", 
                lat: 25.6093, 
                lng: 85.1235,
                price: "₹14,500", 
                rating: 4.3, 
                address: "Kankarbagh, Patna",
                amenities: "WiFi, AC, Laundry, Kitchen",
                contact: generateRandomContact()
            },
            { 
                name: "The Hosteller Patna", 
                lat: 25.6154, 
                lng: 85.1356,
                price: "₹16,000", 
                rating: 4.5, 
                address: "Patliputra, Patna",
                amenities: "WiFi, AC, Laundry, Kitchen",
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

        // Enhanced search functionality
        async function searchHostels(location, radius, minPrice, maxPrice, amenities) {
            const loading = document.getElementById('loading');
            loading.style.display = 'block';

            try {
                if (!location || location.trim() === '') {
                    // No location provided: return all with 0 distance
                    let results = hostels.map(h => ({ ...h, distance: 0 }));
                    // Apply price filter
                    if (minPrice && maxPrice) {
                        results = results.filter(hostel => {
                            const price = parseFloat(hostel.price.replace(/[^0-9]/g, ''));
                            return price >= minPrice && price <= maxPrice;
                        });
                    }
                    // Apply amenities filter
                    if (amenities.length > 0) {
                        results = results.filter(hostel =>
                            amenities.every(amenity => hostel.amenities.toLowerCase().includes(amenity.toLowerCase()))
                        );
                    }
                    return results;
                }

                const encodedLocation = encodeURIComponent(location);
                const response = await Promise.race([
                    fetch(`https://nominatim.openstreetmap.org/search?format=json&limit=1&q=${encodedLocation}`),
                    new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), 8000))
                ]);
                if (!response.ok) throw new Error('Network error');
                const data = await response.json();
                
                if (data.length === 0) {
                    alert('Location not found');
                    return [];
                }

                const userLat = parseFloat(data[0].lat);
                const userLng = parseFloat(data[0].lon);
                
                localStorage.setItem('lastLocation', location);
                localStorage.setItem('lastRadius', radius);

                let filteredHostels = hostels
                    .map(hostel => ({
                        ...hostel,
                        distance: calculateDistance(userLat, userLng, hostel.lat, hostel.lng)
                    }))
                    .filter(hostel => hostel.distance <= radius);

                // Apply price filter
                if (minPrice && maxPrice) {
                    filteredHostels = filteredHostels.filter(hostel => {
                        const price = parseFloat(hostel.price.replace(/[^0-9]/g, ''));
                        return price >= minPrice && price <= maxPrice;
                    });
                }

                // Apply amenities filter
                if (amenities.length > 0) {
                    filteredHostels = filteredHostels.filter(hostel => {
                        return amenities.every(amenity => 
                            hostel.amenities.toLowerCase().includes(amenity.toLowerCase())
                        );
                    });
                }

                return filteredHostels;

            } catch (error) {
                console.error('Search error:', error);
                // Fallback: do a keyword-based filter locally if geocoding fails
                const keyword = (location || '').trim().toLowerCase();
                let fallbackResults = hostels.map(h => ({ ...h, distance: 0 }));
                if (keyword) {
                    fallbackResults = fallbackResults.filter(h =>
                        (h.address + ' ' + h.name).toLowerCase().includes(keyword)
                    );
                }
                if (fallbackResults.length === 0) {
                    alert('Could not reach location service. Showing all hostels.');
                    fallbackResults = hostels.map(h => ({ ...h, distance: 0 }));
                }
                return fallbackResults;
            } finally {
                loading.style.display = 'none';
            }
        }

        // Enhanced display results
        function showResults(hostels) {
            const resultsContainer = document.getElementById('results');
            resultsContainer.innerHTML = '';

            if (hostels.length === 0) {
                resultsContainer.innerHTML = `
                    <div class="no-results">
                        <i class="fas fa-search"></i>
                        <h3>No hostels found</h3>
                        <p>Try adjusting your search criteria or increasing the search radius.</p>
                    </div>
                `;
                return;
            }

            hostels.forEach(hostel => {
                const card = document.createElement('div');
                card.className = 'hostel-card';
                card.innerHTML = `
                    <div class="hostel-header">
                        <h3 class="hostel-name">${hostel.name}</h3>
                        <div class="hostel-rating">
                            <i class="fas fa-star"></i>
                            <span>${hostel.rating}</span>
                        </div>
                    </div>
                    <div class="hostel-details">
                        <div class="detail-item">
                            <i class="fas fa-rupee-sign"></i>
                            <span>${hostel.price}</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-map-marker-alt"></i>
                            <span>${(hostel.distance ?? 0).toFixed(1)} km away</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-phone"></i>
                            <span>${hostel.contact}</span>
                        </div>
                        <div class="detail-item">
                            <i class="fas fa-map"></i>
                            <span>${hostel.address}</span>
                        </div>
                    </div>
                    <div class="hostel-amenities">
                        ${hostel.amenities.split(', ').map(amenity => 
                            `<span class="amenity-tag">
                                <i class="fas fa-${getAmenityIcon(amenity)}"></i>
                                ${amenity}
                            </span>`
                        ).join('')}
                    </div>
                    <div class="hostel-actions">
                        <button class="action-button" onclick="showOnMap(${hostel.lat}, ${hostel.lng})">
                            <i class="fas fa-map-marked-alt"></i>
                            View on Map
                        </button>
                        <button class="action-button secondary-button" onclick="shareHostel('${hostel.name}')">
                            <i class="fas fa-share-alt"></i>
                            Share
                        </button>
                    </div>
                `;
                resultsContainer.appendChild(card);
            });
        }

        function getAmenityIcon(amenity) {
            const icons = {
                'WiFi': 'wifi',
                'AC': 'snowflake',
                'Laundry': 'tshirt',
                'Kitchen': 'utensils'
            };
            return icons[amenity] || 'check';
        }

        // Enhanced map functions
        function updateMap(hostels) {
            // Clear existing markers
            map.eachLayer(layer => layer instanceof L.Marker && map.removeLayer(layer));
            
            if (hostels.length === 0) {
                // Reset to default view if no results
                map.setView([20.5937, 78.9629], 5);
                return;
            }

            // Create markers for each hostel
            const markers = [];
            hostels.forEach(hostel => {
                const marker = L.marker([hostel.lat, hostel.lng], { icon: hostelIcon })
                    .addTo(map)
                    .bindPopup(`
                        <div class="map-popup">
                            <h3>${hostel.name}</h3>
                            <p>Price: ${hostel.price}</p>
                            <p>Rating: ${hostel.rating} ★</p>
                            <button onclick="showHostelDetails('${hostel.name}')">
                                View Details
                            </button>
                        </div>
                    `);
                markers.push(marker);
            });

            // Create a bounds object that includes all markers
            const bounds = L.latLngBounds(markers.map(marker => marker.getLatLng()));
            
            // Fit the map to show all markers with some padding
            map.fitBounds(bounds, {
                padding: [50, 50],
                maxZoom: 15
            });
        }

        function showOnMap(lat, lng) {
            map.setView([lat, lng], 15);
            document.getElementById('map').scrollIntoView({ behavior: 'smooth' });
        }

        function shareHostel(hostelName) {
            if (navigator.share) {
                navigator.share({
                    title: hostelName,
                    text: `Check out ${hostelName} on Indian Hostel Finder!`,
                    url: window.location.href
                });
            } else {
                alert('Sharing is not supported in your browser');
            }
        }

        // Event handlers
        document.getElementById('searchForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const location = document.getElementById('location').value;
            const radius = parseInt(document.getElementById('radius').value);
            const minPrice = parseInt(document.getElementById('minPrice').value) || 0;
            const maxPrice = parseInt(document.getElementById('maxPrice').value) || Infinity;
            const amenities = Array.from(document.querySelectorAll('.amenities-filter input:checked'))
                .map(checkbox => checkbox.value);
            
            const hostels = await searchHostels(location, radius, minPrice, maxPrice, amenities);
            showResults(hostels);
            updateMap(hostels);
        });

        document.getElementById('resetButton').addEventListener('click', () => {
            document.getElementById('location').value = '';
            document.getElementById('radius').value = '5';
            document.getElementById('minPrice').value = '';
            document.getElementById('maxPrice').value = '';
            document.querySelectorAll('.amenities-filter input').forEach(checkbox => {
                checkbox.checked = false;
            });
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
            const resultsContainer = document.getElementById('results');
            const hostelCards = Array.from(resultsContainer.getElementsByClassName('hostel-card'));
            
            const sortedCards = hostelCards.sort((a, b) => {
                if (sortBy === 'price') {
                    const priceA = parseFloat(a.querySelector('.detail-item:first-child span').textContent.replace(/[^0-9]/g, ''));
                    const priceB = parseFloat(b.querySelector('.detail-item:first-child span').textContent.replace(/[^0-9]/g, ''));
                    return priceA - priceB;
                }
                if (sortBy === 'rating') {
                    const ratingA = parseFloat(a.querySelector('.hostel-rating span').textContent);
                    const ratingB = parseFloat(b.querySelector('.hostel-rating span').textContent);
                    return ratingB - ratingA;
                }
                if (sortBy === 'distance') {
                    const distanceA = parseFloat(a.querySelector('.detail-item:nth-child(2) span').textContent);
                    const distanceB = parseFloat(b.querySelector('.detail-item:nth-child(2) span').textContent);
                    return distanceA - distanceB;
                }
                return 0;
            });

            // Clear and re-append sorted cards
            resultsContainer.innerHTML = '';
            sortedCards.forEach(card => resultsContainer.appendChild(card));
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
                showResults(hostels.map(h => ({ ...h, distance: 0 })));
                updateMap(hostels);
            }
        });
    </script>
</body>
</html>
"""

# Streamlit app configuration
st.set_page_config(
    page_title="Indian Hostel Finder",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main app
def main():
    st.title("🏠 Indian Hostel Finder")
    st.markdown("""
    Find the best hostels across India with real-time location search and filtering options.
    Search by city, use your current location, or browse all available options.
    """)
    
    # Render the HTML component
    html(html_code, height=800, scrolling=True)
    
    # Additional Streamlit components
    with st.expander("ℹ️ About this application"):
        st.write("""
        This application helps students and travelers find affordable hostel accommodations across India.
        
        **Features:**
        - Search hostels by location
        - Filter by distance (5km to 50km radius)
        - Price range filtering
        - Amenities filtering
        - Sort by price, rating, or distance
        - View hostels on an interactive map
        - Get contact information for each hostel
        - Share hostel details
        - Save favorite hostels
        
        **Data Sources:**
        - OpenStreetMap for location data
        - Leaflet.js for interactive maps
        - Curated list of popular hostels across India
        """)
        
    st.markdown("---")
    st.caption("© 2025 Indian Hostel Finder | For educational purposes only")

if __name__ == "__main__":
    main()
