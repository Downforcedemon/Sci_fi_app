sequenceDiagram
    participant ReactApp as React Frontend
    participant JavaServer as Java Backend Server
    participant PythonService as Python Data Processing Service
    participant FileSystem as File System/Storage

    ReactApp->>JavaServer: HTTP Request (initiate data processing)
    JavaServer->>PythonService: Invoke Python script
    PythonService->>FileSystem: Generate diagrams and save files
    FileSystem->>PythonService: Return file paths
    PythonService->>JavaServer: Send back file paths/Base64 strings
    JavaServer->>ReactApp: Send image URLs/Base64 encoded images
    ReactApp->>JavaServer: Request diagrams (if URLs provided)
    JavaServer->>FileSystem: Retrieve diagrams
    FileSystem->>JavaServer: Return image files
    JavaServer->>ReactApp: Send image files to frontend
    ReactApp-->>ReactApp: Render diagrams in UI

// to use this flowchart
<script src="https://cdn.jsdelivr.net/npm/mermaid@8.13.5/dist/mermaid.min.js"></script>
<script>mermaid.initialize({ startOnLoad: true });</script>


// add mermaid syntax  within div
<div class="mermaid">
    <!-- Mermaid syntax goes here -->
</div>


