graph TD
    subgraph Automation Flow
        A[Data Retrieval<br>Use MAST API to retrieve light curve data] -->|Automate| B[Automate Download & Storage<br>Quartz Job Scheduler]
        B -->|Scripts with LightKurve| C[Preprocessing<br>Flatten curve, remove outliers, normalize flux]
        C -->|Apply BLS algorithm| D[Transit Signal Detection<br>Implement filters for false positives]
        D -->|Use ML models| E[Candidate Validation<br>Features: transit parameters, etc.]
        E -->|Store in DB, provide web interface| F[Catalog & Review<br>Review candidates]
        F -->|Create alerts| G[Notification System<br>For high probability candidates]
        F -->|Automate requests| H[Observatory Integration<br>For follow-up observations]
    end

    subgraph Tech Stack
        TS1[Frontend<br>React, D3.js/Chart.js, Material-UI/Bootstrap] -.-> PlanetSearch
        TS2[Backend<br>Java Maven, Spring Boot, Python Integration] -.-> API
        TS3[Data Analysis<br>LightKurve, SciPy/NumPy, Scikit-learn/TensorFlow] -.-> Analysis
        TS4[Database<br>PostgreSQL] -.-> DB
        TS5[DevOps<br>Docker, Jenkins/GitHub Actions, Prometheus/Grafana] -.-> DevOps
        TS6[Security<br>Spring Security, OAuth2/JWT] -.-> Sec
        TS7[Job Scheduler<br>Quartz] -.-> JSch
    end

    %% Define resources as subgraph
    subgraph R[Resources]
        R1[Database]
        R2[Web Interface]
        R3[Security]
    end

    %% Connect resources to the Catalog & Review step
    F -.-> R1
    F -.-> R2
    F -.-> R3

    %% Connect job scheduler to the automation flow
    JSch -.-> B
    JSch -.-> H

    %% Connect tech stack to automation flow
    API --> A
    Analysis --> C
    DB --> F
    Sec --> TS6
    DevOps -.-> Deployment
    PlanetSearch -.-> F

    %% Styling
    classDef automation fill:#f9f,stroke:#333,stroke-width:2px;
    classDef techstack fill:#ccf,stroke:#33a,stroke-width:2px;
    classDef resources fill:#bbf,stroke:#33f,stroke-width:2px;
    class A,B,C,D,E,F,G,H automation;
    class TS1,TS2,TS3,TS4,TS5,TS6,TS7 techstack;
    class R1,R2,R3 resources;

