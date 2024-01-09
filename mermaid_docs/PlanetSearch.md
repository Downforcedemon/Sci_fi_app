graph TD
    A[Data Retrieval<br>Use MAST API to retrieve light curve data] -->|Automate| B[Automate Download & Storage<br>Scheduled job and trigger]
    B -->|Scripts with LightKurve| C[Preprocessing<br>Flatten curve, remove outliers, normalize flux]
    C -->|Apply BLS algorithm| D[Transit Signal Detection<br>Implement filters for false positives]
    D -->|Use ML models| E[Candidate Validation<br>Features: transit parameters, etc.]
    E -->|Store in DB, provide web interface| F[Catalog & Review<br>Review candidates]
    F -->|Create alerts| G[Notification System<br>For high probability candidates]
    F -->|Automate requests| H[Observatory Integration<br>For follow-up observations]

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

    %% Styling
    classDef default fill:#f9f,stroke:#333,stroke-width:2px;
    classDef resources fill:#bbf,stroke:#33f,stroke-width:2px;
    class A,B,C,D,E,F,G,H default;
    class R1,R2,R3 resources;

