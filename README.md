# Forex Mock App

The application is deployed on Azure and consists of several interconnected components. Here's a summary of the architecture:

1. **User/Application Interaction:**
   - **API Client/User:** Users or applications interact with the system via an API exposed through Azure API Management (APIM).
   - **Azure App Service:** Serves as the hosting platform for the API, handling incoming requests.

2. **Forex Data Handling:**
   - **Mock Forex API (Azure Function):** A serverless function on Azure that generates or fetches forex data from an external forex data source.
   - **Azure Data Factory (ADF):** Ingests data from the Mock Forex API and stores it in Azure Blob Storage in JSON format. This serves as a data ingestion pipeline.

3. **Data Storage and Processing:**
   - **Azure Blob Storage:** Stores the ingested forex data as JSON files, which can be processed or accessed by other components.
   - **MongoDB Atlas Cloud:** Stores the processed forex data. MongoDB Atlas is used as the main database, accessible through the microservices.

4. **Microservices and Caching:**
   - **Java Spring Boot Application (AKS):** Deployed on Azure Kubernetes Service (AKS), this microservice processes and exposes forex data to the API client. It queries MongoDB for data and uses Redis for caching.
   - **Redis Database:** Used for caching the forex data to improve performance and reduce latency for repeated queries.

5. **Event-Driven Processing:**
   - **Azure Function (Blob Trigger):** This function is triggered when new data is added to Azure Blob Storage. It processes the data, possibly transforming it or moving it to another service.
   - **Azure Function (Event Hub Trigger):** Listens to events from Azure Event Hub, which may involve real-time processing of forex data or triggering downstream processes.

6. **Logging and Monitoring:**
   - **Application Insights:** Integrated with various components, Application Insights is used for monitoring and logging, ensuring that the application's health and performance are maintained.

7. **Configuration Management:**
   - **Azure App Configuration:** Centralized management of configuration settings, including connection strings, API keys, and other environment-specific settings for the application.

8. **Security and API Management:**
   - **Azure API Management (APIM):** Manages the API endpoint exposed to users. It secures the API, handles authentication, and enforces policies.

9. **Event Hub:**
   - **Azure Event Hub:** Acts as a highly scalable data streaming platform to ingest and process large amounts of event data, such as real-time forex data feeds.

This architecture leverages various Azure services to create a scalable, secure, and highly available application for fetching and processing forex exchange rates. The design ensures that the system is robust, with built-in monitoring, caching, and configuration management.