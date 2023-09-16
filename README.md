1. ## Installation

To set up and use the JWT Authentication System, follow these steps:

### 1. Set up the virtual environment

- Install Pipenv if you haven't already:

  ````

  pip install pipenv



  ````
- Navigate to the project directory and create a virtual environment:

  ````

  pipenv shell


  ````

### 2. Clone the repository

- Clone the repository from GitHub using the following command:

  ````

  git clone https://github.com/GmalFari/JWT_auth_system.git

  ````

### 3. Create a PostgreSQL database

- Install PostgreSQL if you haven't already.
- Create a new database using your preferred .
- Note down the following details for the database:

  - Database name (DB_NAME)
  - Database user (DB_USER)
  - Database password (DB_PASSWORD)
  - Database host (DB_HOST)
  - Database port (DB_PORT)

### 4. Set up environment variables

- Create a `.env` file in the project's root directory.
- Add the following variables to the `.env` file and replace the placeholders with the appropriate values:

  ````

  DEBUG=<debug_value>

  DB_NAME=<db_name>

  DB_USER=<db_user>

  DB_PASSWORD=<db_password>

  DB_HOST=<db_host>

  DB_PORT=<db_port>

  ```


  ````

### 5. Install project dependencies

- Run the following command to install the project dependencies using Pipenv:

  ````

  pipenv install

  ````

### 6. Run database migrations

- Apply the database migrations using the following command:

  ````

  python manage.py migrate
  ````

### 7. Start the development server

- Start the development server using the following command:

  ````

  python manage.py runserver


  ````
- The server will start running at `http://localhost:8000/`.

### 8. Access the authentication app

- Open a web browser and navigate to `http://localhost:8000/` to access the authentication app.

Please note that you need to replace the `<db_name>`, `<db_user>`, `<db_password>`, `<db_host>`, `<db_port>`, `<email_host_user>`, and `<email_host_password>`

placeholders with the actual values corresponding to your setup.

---

   
2. Custom User Model

   ---

   A custom user model has been implemented to provide enhanced functionality and additional fields for user accounts. The custom user model includes the following fields:

   ...
3. Groups and Permissions

   ---

   The user types in the application have been organized into groups, allowing for easier management of permissions and access levels. Groups such as "Regular User" and "Admin User" have been created to represent different user roles.

   ...
4. Serializers and Views

   ---

   Serializers have been created to handle the conversion of user account data to and from JSON format. Separate serializers have been implemented for each user type to ensure accurate representation and validation of user data.

   ...
5. Endpoints

   ---

   The following endpoints are available for user-related operations:

   ...
6. Access and Refresh Tokens

   ---

   To authenticate and authorize API requests, access tokens and refresh tokens are used. The access token is included in the Authorization header of the HTTP request using the Bearer scheme. The refresh token is used to obtain a new access token when the current access token expires.


   1. Access Token:

      ---

      The access token should be included in the Authorization header of the HTTP request using the Bearer scheme. Here's an example:


      ```

      Authorization: Bearer <access_token>

      ```
   2. Refresh Token:

      ---

      To obtain a new access token using a refresh token, send a POST request to the `/api/token/refresh` endpoint with the refresh token included in the request body. Here's an example:


      ```

      POST http://localhost:8000/api/token/refresh


      Request Body:

      {

        "refresh": "<refresh_token>"

      }

      ```

      Upon successful refresh token validation, a new access token will be returned in the response.
7. Integration with User Account Creation

   ---

   When a new user account is created, you can automatically add the user's profile to the `UserProfile` model using the `UserAccountSerializer`. The exact implementation may depend on your specific project structure and requirements.


   1. After creating the user account using the custom user model, retrieve the user's profile details.
   2. Serialize the profile data using the `UserAccountSerializer` to convert it into JSON format.
   3. Create a new instance of the `UserProfile` model using the serialized data.
   4. Save the `UserProfile` instance to persist it in the database.

   Make sure to handle any validation or error scenarios appropriately based on your project's needs.

Please make sure to replace the placeholders and example URLs with the appropriate values for your project.
