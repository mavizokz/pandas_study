# Inventory Management System

This project simulates an inventory management system for tracking products' stock levels and restocking needs based on sales data. The system calculates the **Reorder Point** for each product, which is the threshold stock level required to avoid running out while waiting for new inventory to arrive. It also identifies products that need restocking based on current stock levels and restocking time.

## Features:
- **Reorder Point Calculation**: Calculates the reorder point for each product based on its daily sales and restock time.
- **Stock Monitoring**: Identifies products that require restocking.
- **Data Visualization**: Visualizes the products' current stock levels and highlights which products need restocking using a bar plot.

## How it Works:
1. It generates a simulated dataset of products, including information about sales, current stock, and restocking time.
2. It calculates the reorder point for each product.
3. It identifies products that need restocking and visualizes the data in an easy-to-understand graph.

## Technologies Used:
- Python
- Pandas
- Matplotlib & Seaborn (for visualization)

## Usage:
1. Run the code to simulate and analyze inventory data.
2. Visualize products that require restocking.
