-- ================================
-- CUSTOMER ANALYSIS AIRBNB DATA
-- ================================

USE airbnb;

-- Top 10 Most Expensive Neighbourhoods
SELECT neighbourhood,
ROUND(AVG(price), 2) AS avg_price
FROM cleaned_listings
GROUP BY neighbourhood
ORDER BY avg_price DESC
LIMIT 10;

-- Average price by host type
SELECT host_type,
ROUND(AVG(price), 2)
FROM merged_featured
GROUP BY host_type;

-- Average price by room type
SELECT room_type,
ROUND(AVG(price), 2)
FROM merged_featured
GROUP BY room_type;

-- Average available days by price category
SELECT 
    price_category,
    ROUND(AVG(available_days), 1) AS avg_available_days
FROM merged_featured
GROUP BY price_category;

-- Neighborhoods with the most listings
SELECT neighbourhood,
COUNT(*) AS listing_count
FROM merged_featured
GROUP BY neighbourhood
ORDER BY listing_count DESC;

-- Top host 
SELECT host_name,
COUNT(*) AS listing_count
FROM merged_featured
GROUP BY host_name
ORDER BY listing_count DESC; 