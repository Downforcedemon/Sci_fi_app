sequenceDiagram
    participant ReactApp as React Frontend
    participant JavaServer as Java Backend Server
    participant PythonService as Python Data Processing Service
    participant SearchNew as Search_new.py
    participant DiagramGen as diagram_generator.py
    participant FileSystem as File System/Storage

    ReactApp->>JavaServer: HTTP Request (initiate data processing)
    JavaServer->>PythonService: Invoke Python service
    PythonService->>SearchNew: Fetch and process star data
    SearchNew-->>PythonService: Return processed data
    PythonService->>DiagramGen: Generate diagrams from data
    DiagramGen->>FileSystem: Save diagrams and get file paths
    FileSystem->>DiagramGen: Confirm save and return paths
    DiagramGen-->>PythonService: Return file paths/Base64 strings
    PythonService->>JavaServer: Send back file paths/Base64 strings
    JavaServer->>ReactApp: Send image URLs/Base64 encoded images
    ReactApp->>JavaServer: Request diagrams (if URLs provided)
    JavaServer->>FileSystem: Retrieve diagrams
    FileSystem->>JavaServer: Return image files
    JavaServer->>ReactApp: Send image files to frontend
    ReactApp-->>ReactApp: Render diagrams in UI

