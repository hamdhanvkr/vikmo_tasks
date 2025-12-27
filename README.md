1. Project Tile 

          Sales Order & Inventory Lite


2. Project Overview

          A backend application built using Django REST Framework that handles product management, inventory tracking, and sales order processing for a simplified B2B system.
          This project was developed as part of an assignment to demonstrate API design, database modeling, and Django best practices.


3. Features Implemented

          1. Product CRUD APIs

          2. Inventory management

          3. Dealer-based order creation

          4. Order items with quantity & pricing

          5. Stock deduction on order confirmation

          6. Token-based authentication

          7. RESTful API architecture


4. Tech Stack

          1. Backend: Django 4.2

          2. API: Django REST Framework

          3. Database: PostgreSQL

          4. Auth: DRF Token Authentication

          5. Language: Python 3.10+

          6. Testing: Postman


5. Setup Instructions


          1. Clone Repository
                  git clone https://github.com/hamdhanvkr/vikmo_tasks.git
                  cd vikmo_sales
   
          2. Create Virtual Environment
                  python -m venv venv
                  Activate:
                  venv\Scripts\activate

          3. Run Migrations
                  python manage.py makemigrations
                  python manage.py migrate

          4. Create Superuser
   
                  python manage.py createsuperuser 

                  username:XXXXXX
                  email:abc@gmail.com
                  password:XXXXXXX

          5. Generate API Token
                  python manage.py drf_create_token <your username>

          6. Start Server
                  python manage.py runserver


7. API Documentation


   1. Product API
  
   
  
   | Method | Endpoint              | Description                       |
   | ------ | --------------------- | --------------------------------- |
   | GET    | `/api/products/`      | List all products with stock info |       
   | POST   | `/api/products/`      | Create a new product              |
   | GET    | `/api/products/{id}/` | Get product details               |
   | PUT    | `/api/products/{id}/` | Update product                    |
   | DELETE | `/api/products/{id}/` | Delete product                    |


   GET METHOD
   
   Inital you get a product its should be empty []

   After create a product using POST Method the response will be look like

   [
    {
        "id": 1,
        "sku": "SKU001",
        "name": "Brake Pad",
        "description": "",
        "price": "500.00",
        "is_active": true,
        "created_at": "2025-12-27T06:32:49.866989Z",
        "updated_at": "2025-12-27T06:32:49.867260Z"
    },
    {
        "id": 2,
        "sku": "SKU002",
        "name": "Brake Disc Pad",
        "description": "",
        "price": "1500.00",
        "is_active": true,
        "created_at": "2025-12-27T07:27:11.766586Z",
        "updated_at": "2025-12-27T07:27:11.766616Z"
    },

 

   POST METHOD 

   Example request for POST Method

   {
   "sku":"SKU003",
   "name":"Drum Pad",
   "price":800
    }

   Example response for POST Method
   
   {
    "id": 4,
    "sku": "SKU004",
    "name": "Drum Pad",
    "description": "",
    "price": "1000.00",
    "is_active": true,
    "created_at": "2025-12-27T09:51:13.241475Z",
    "updated_at": "2025-12-27T09:51:13.241492Z"
}



PUT METHOD 


The 1st product id is 1 that product price will be updated 500 to 900

{
        "sku": "SKU001",
        "name": "Brake Pad",
        "description": "",
        "price": "900.00"
}



 DELETE METHOD 


  just trigger this api http://127.0.0.1:8000/api/products/5/                  5 is id primary key






2. Dealer API


| Method | Endpoint             | Description                    |
| ------ | -------------------- | ------------------------------ |
| GET    | `/api/dealers/`      | List all dealers               |
| POST   | `/api/dealers/`      | Create a new dealer            |
| GET    | `/api/dealers/{id}/` | Get dealer details with orders |
| PUT    | `/api/dealers/{id}/` | Update dealer                  |



GET METHOD
   
   Inital you get a product its should be empty []

   After create a dealer using POST Method the response will be look like

 {
        "id": 1,
        "dealer_code": "D001",
        "name": "vikmo",
        "email": "vikmo@gmail.com",
        "phone": "9874561230",
        "address": "bangalore",
        "created_at": "2025-12-27T06:43:00.323557Z"
  }               


POST METHOD 

   Example request for POST Method
   
     {
        "dealer_code": "D002",
        "name": "vikmo",
        "email": "vikmo@gmail.com",
        "phone": "9874561230",
        "address": "Bangalore"
    }

  Example response for POST Method

    {
    "id": 2,
    "dealer_code": "D002",
    "name": "vikmo",
    "email": "vikmo@gmail.com",
    "phone": "9874561230",
    "address": "Bangalore",
    "created_at": "2025-12-27T09:56:45.891527Z"
}


PUT METHOD 


The 1st Dealer id is 1 that dealer email will be updated vikmo to elements

{
    "id": 1,
    "dealer_code": "D001",
    "name": "vikmo",
    "email": "elements@gmail.com",      // Email updated
    "phone": "9874561230",
    "address": "BLR",
    "created_at": "2025-12-27T06:43:00.323557Z"
}



3. Order API


| Method | Endpoint                    | Description                     |
| ------ | --------------------------- | ------------------------------- |
| GET    | `/api/orders/`              | List all orders with filters    |
| POST   | `/api/orders/`              | Create new draft order          |
| GET    | `/api/orders/{id}/`         | Get order with items            |
| PUT    | `/api/orders/{id}/`         | Update draft order              |
| POST   | `/api/orders/{id}/confirm/` | Confirm order (validates stock) |
| POST   | `/api/orders/{id}/deliver/` | Mark order as delivered         |




GET METHOD
   
   Inital you get a order its should be empty []

   After create a order using POST Method the response will be look like


     {
        "id": 3,
        "items": [
            {
                "id": 3,
                "product": 1,
                "quantity": 50,
                "unit_price": "500.00",
                "line_total": "25000.00"
            }
        ],
        "order_number": "ORD-20251227-0003",
        "status": "DRAFT",
        "total_amount": "25000.00",
        "created_at": "2025-12-27T06:53:47.845608Z",
        "updated_at": "2025-12-27T06:53:47.851907Z",
        "dealer": 1
    }


    POST METHOD 

     Example request for POST Method


     {
    "dealer":"1",
       "items":[
        {    "product":1,
            "quantity":8
        }
        ]
    }


      Example response for POST Method
      
    {
    "id": 5,
    "items": [
        {
            "id": 12,
            "product": 1,
            "quantity": 8,
            "unit_price": "900.00",
            "line_total": "7200.00"
        }
    ],
    "order_number": "ORD-20251227-0005",
    "status": "DRAFT",
    "total_amount": "7200.00",
    "created_at": "2025-12-27T10:08:18.407692Z",
    "updated_at": "2025-12-27T10:08:18.422225Z",
    "dealer": 1
}




PUT METHOD 

http://127.0.0.1:8000/api/orders/5/          5 th id using only draft order only edit access other wise this error          "Only DRAFT orders can be modified"


{
    "id": 5,
    "items": 
        id": 14,
        "product": 1,  
        "quantity": 4,                     // Quamtity will be updated 8 to 4 
        "unit_price": "900.00",
        "line_total": "3600.00"
    }
  
    "order_number": "ORD-20251227-0005",
    "status": "DRAFT",
    "total_amount": "3600.00",
    "created_at": "2025-12-27T10:08:18.407692Z",
    "updated_at": "2025-12-27T10:11:51.233908Z",
    "dealer": 1


POST METHOD        for order CONFIRMED and DELIVERED


http://127.0.0.1:8000/api/orders/5/confirm/                   this api 5th id trigger DRAFT to Changed CONFIRMED

http://127.0.0.1:8000/api/orders/5/deliver/                   this api 5th id trigger CONFIRMED to Changed DELIVERED


4. Inventory API            //   Note :  ONLY ACCESS FOR ADMIN RIGHTS ITS WORKS ONLY Authorized using token create after access  //


| Method | Endpoint                       | Description                     |
| ------ | ------------------------------ | ------------------------------- |
| GET    | `/api/inventory/`              | List all inventory levels       |
| PUT    | `/api/inventory/{product_id}/` | Manual stock adjustment (admin) |


GET METHOD
   
   Inital you get a inventory its should be empty []

   After create a inventory using POST Method the response will be look like


   {
        "product_id": 3,
        "sku": "SKU002",
        "product_name": "Brake Disc Pad",
        "quantity": 0,
        "updated_by": "",
        "updated_at": "2025-12-27T07:27:11.778220Z"
    }


PUT METHOD 


http://127.0.0.1:8000/api/inventory/3/        3 id in api i updated quantity 


{
    "quantity":5 
}

{
    "product_id": 3,
    "sku": "SKU002",
    "product_name": "Brake Disc Pad",
    "quantity": 5,                                        // QUANTITY will be updated 0 to 5
    "updated_by": "hamdhan",
    "updated_at": "2025-12-27T10:23:53.867101Z"
}





7. Diagram




+------------------+                                           
|      Dealer      |
+------------------+
| id (PK)          |
| dealer_code (U)  |
| name             |
| email (U)        |
| phone            |
| address          |
| created_at       |
+------------------+
        |
        | 1 ────< Many
        |
+------------------+
|       Order      |
+------------------+
| id (PK)          |
| order_number (U) |
| status           |
| total_amount     |
| dealer_id (FK)   |
| created_at       |
| updated_at       |
+------------------+
        |
        | 1 ────< Many
        |
+------------------+
|    OrderItem     |
+------------------+
| id (PK)          |
| order_id (FK)    |
| product_id (FK)  |
| quantity         |
| unit_price       |
| line_total       |
+------------------+
        |
        | Many ──── 1
        |
+------------------+
|     Product      |
+------------------+
| id (PK)          |
| sku (U)          |
| name             |
| description      |
| price            |
| is_active        |
| created_at       |
| updated_at       |
+------------------+
        |
        | 1 ──── 1
        |
+------------------+
|    Inventory     |
+------------------+
| id (PK)          |
| product_id (FK)  |
| quantity         |
| updated_by       |
| updated_at       |
+------------------+




Relationship Explanation 

    

1.Dealer → Order

One Dealer can place many Orders

Order.dealer → ForeignKey(Dealer)

2. Order → OrderItem

One Order contains multiple OrderItems

OrderItem.order → ForeignKey(Order)

3️. OrderItem → Product

Many OrderItems can reference one Product

OrderItem.product → ForeignKey(Product)

4️. Product → Inventory

Each Product has exactly one Inventory record

Inventory.product → OneToOneField(Product)


      



By 
Mohamed Hamdhan J



