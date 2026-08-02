import base64
import urllib.request
import os

graphs = {
    "hierarchical_model.png": """graph TD
    A[Shoes] --> B[Women's Shoes]
    A --> C[Men's Shoes]
    B --> D[High Heels]
    B --> E[Bellies]
    C --> F[Sports Shoes]
    C --> G[Sneakers]
    style A fill:#dae8fc,stroke:#6c8ebf
    style B fill:#dae8fc,stroke:#6c8ebf
    style C fill:#dae8fc,stroke:#6c8ebf
    style D fill:#dae8fc,stroke:#6c8ebf
    style E fill:#dae8fc,stroke:#6c8ebf
    style F fill:#dae8fc,stroke:#6c8ebf
    style G fill:#dae8fc,stroke:#6c8ebf""",

    "network_model.png": """graph TD
    A[College] --> B[CSE Department]
    A --> C[Library]
    B --> D[Student]
    C --> D
    style A fill:#dae8fc,stroke:#6c8ebf
    style B fill:#dae8fc,stroke:#6c8ebf
    style C fill:#dae8fc,stroke:#6c8ebf
    style D fill:#dae8fc,stroke:#6c8ebf""",

    "relational_model.png": """classDiagram
    class Students {
        +RollNo
        +Name
        +Phone
        1 : Alex : 444123
        2 : Aryan : 421456
        3 : Parker : 414259
        4 : Jhon : 456785
    }""",

    "object_oriented_model.png": """graph TD
    O((OBJECT ORIENTED<br>DATABASE))
    O --- P[Poly-<br>morphism]
    O --- I[In-<br>heritance]
    O --- E[En-<br>capsulation]
    style O fill:#ffffff,stroke:#000000,stroke-width:2px
    style P fill:#ffffff,stroke:#000000
    style I fill:#ffffff,stroke:#000000
    style E fill:#ffffff,stroke:#000000""",

    "object_relational_model.png": """flowchart LR
    A[Objects in Memory] <--> B[Mapping Logic] <--> C[(Relational Database)]
    style A fill:#5a8be2,stroke:#5a8be2,color:#ffffff
    style B fill:#82b366,stroke:#82b366,color:#ffffff
    style C fill:#3972a9,stroke:#3972a9,color:#ffffff""",

    "dbms_architecture.png": """graph TD
    subgraph External Level
        E1[View 1]
        E2[View 2]
        E3[View n]
    end
    L[Logical Schema]
    P[Physical Schema]
    D[(Database)]
    E1 --> L
    E2 --> L
    E3 --> L
    L <--> P
    P <--> D
    style E1 fill:#ffffff,stroke:#000000
    style E2 fill:#ffffff,stroke:#000000
    style E3 fill:#ffffff,stroke:#000000
    style L fill:#82b366,stroke:#82b366,color:#000000
    style P fill:#82b366,stroke:#82b366,color:#000000
    style D fill:#3972a9,stroke:#3972a9,color:#ffffff"""
}

def generate_mermaid_url(graph_string):
    graphbytes = graph_string.encode("utf8")
    base64_bytes = base64.urlsafe_b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    return "https://mermaid.ink/img/" + base64_string

output_dir = "/Users/rahul/Desktop/DBMS/docs/images"
os.makedirs(output_dir, exist_ok=True)

for filename, graph in graphs.items():
    url = generate_mermaid_url(graph)
    out_path = os.path.join(output_dir, filename)
    print(f"Downloading {filename} from {url}")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(out_path, 'wb') as out_file:
        out_file.write(response.read())
    print(f"Saved to {out_path}")
