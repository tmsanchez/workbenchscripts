 
# Schema Report for database: sakila 
- actor 
- address 
- category 
- city 
- country 
- customer 
- film 
- film_actor 
- film_category 
- film_text 
- inventory 
- language 
- payment 
- rental 
- staff 
- store 
 
 
### Table: actor 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|actor_id|SMALLINT|Yes|Yes|No|||
|first_name|VARCHAR(45)|Yes|No|No|||
|last_name|VARCHAR(45)|Yes|No|No|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: address 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|address_id|SMALLINT|Yes|Yes|No|||
|address|VARCHAR(50)|Yes|No|No|||
|address2|VARCHAR(50)|No|No|No|NULL||
|district|VARCHAR(20)|Yes|No|No|||
|city_id|SMALLINT|Yes|No|Yes|||
|postal_code|VARCHAR(10)|No|No|No|NULL||
|phone|VARCHAR(20)|Yes|No|No|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: category 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|category_id|TINYINT|Yes|Yes|No|||
|name|VARCHAR(25)|Yes|No|No|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: city 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|city_id|SMALLINT|Yes|Yes|No|||
|city|VARCHAR(50)|Yes|No|No|||
|country_id|SMALLINT|Yes|No|Yes|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: country 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|country_id|SMALLINT|Yes|Yes|No|||
|country|VARCHAR(50)|Yes|No|No|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: customer 
 Table Comments: Table storing all customers. Holds foreign keys to the address table and the store table where this customer is registered.

Basic information about the customer like first and last name are stored in the table itself. Same for the date the record was created and when the information was last updated. 
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|customer_id|SMALLINT|Yes|Yes|No|||
|store_id|TINYINT|Yes|No|Yes|||
|first_name|VARCHAR(45)|Yes|No|No|||
|last_name|VARCHAR(45)|Yes|No|No|||
|email|VARCHAR(50)|No|No|No|NULL||
|address_id|SMALLINT|Yes|No|Yes|||
|active|TINYINT(1)|Yes|No|No|TRUE||
|create_date|DATETIME|Yes|No|No|||
|last_update|TIMESTAMP|No|No|No|CURRENT_TIMESTAMP||
 
 
### Table: film 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|film_id|SMALLINT|Yes|Yes|No|||
|title|VARCHAR(255)|Yes|No|No|||
|description|TEXT|No|No|No|||
|release_year|YEAR|No|No|No|||
|language_id|TINYINT|Yes|No|Yes|||
|original_language_id|TINYINT|No|No|Yes|NULL||
|rental_duration|TINYINT|Yes|No|No|3||
|rental_rate|DECIMAL(4,2)|Yes|No|No|4.99||
|length|SMALLINT|No|No|No|NULL||
|replacement_cost|DECIMAL(5,2)|Yes|No|No|19.99||
|rating|ENUM('G','PG','PG-13','R','NC-17')|No|No|No|'G'||
|special_features|SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes')|No|No|No|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: film_actor 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|actor_id|SMALLINT|Yes|Yes|Yes|||
|film_id|SMALLINT|Yes|Yes|Yes|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: film_category 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|film_id|SMALLINT|Yes|Yes|Yes|||
|category_id|TINYINT|Yes|Yes|Yes|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: film_text 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|film_id|SMALLINT|Yes|Yes|Yes|||
|title|VARCHAR(255)|Yes|No|No|||
|description|TEXT|No|No|No|||
 
 
### Table: inventory 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|inventory_id|MEDIUMINT|Yes|Yes|No|||
|film_id|SMALLINT|Yes|No|Yes|||
|store_id|TINYINT|Yes|No|Yes|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: language 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|language_id|TINYINT|Yes|Yes|No|||
|name|CHAR(20)|Yes|No|No|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: payment 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|payment_id|SMALLINT|Yes|Yes|No|||
|customer_id|SMALLINT|Yes|No|Yes|||
|staff_id|TINYINT|Yes|No|Yes|||
|rental_id|INT|No|No|Yes|NULL||
|amount|DECIMAL(5,2)|Yes|No|No|||
|payment_date|DATETIME|Yes|No|No|||
|last_update|TIMESTAMP|No|No|No|CURRENT_TIMESTAMP||
 
 
### Table: rental 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|rental_id|INT|Yes|Yes|No|||
|rental_date|DATETIME|Yes|No|No|||
|inventory_id|MEDIUMINT|Yes|No|Yes|||
|customer_id|SMALLINT|Yes|No|Yes|||
|return_date|DATETIME|No|No|No|||
|staff_id|TINYINT|Yes|No|Yes|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: staff 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|staff_id|TINYINT|Yes|Yes|No|||
|first_name|VARCHAR(45)|Yes|No|No|||
|last_name|VARCHAR(45)|Yes|No|No|||
|address_id|SMALLINT|Yes|No|Yes|||
|picture|BLOB|No|No|No|||
|email|VARCHAR(50)|No|No|No|NULL||
|store_id|TINYINT|Yes|No|Yes|||
|active|TINYINT(1)|Yes|No|No|TRUE||
|username|VARCHAR(16)|Yes|No|No|||
|password|VARCHAR(40)|No|No|No|NULL||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
### Table: store 
 Table Comments:  
|Name |Data Type |Nullable |PK |FK |Default |Comment |
--- | ---| --- | --- | --- | --- | ---
|store_id|TINYINT|Yes|Yes|No|||
|manager_staff_id|TINYINT|Yes|No|Yes|||
|address_id|SMALLINT|Yes|No|Yes|||
|last_update|TIMESTAMP|Yes|No|No|CURRENT_TIMESTAMP||
 
 
 
