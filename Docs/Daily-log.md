📅 Daily Progress Log

Day 1 - Project Setup

- Understood the problem statement
- Defined project goal
- Designed cloud architecture
- Created GitHub repository
- Added README and architecture diagram
- Set up project folder structure
- Added .gitignore file

Day 2 - Frontend & Backend Integration

- Created frontend UI with API integration
- Set up Flask backend with GET and POST endpoints
- Connected frontend with backend APIs
- Successfully tested full data flow (UI → API → UI)

Issues Faced & Resolved:
1. Frontend API Not Working Initially
   - Problem: API calls failed when opening HTML file directly
   - Reason: Frontend was opened using file:// protocol, which restricts API calls
   - Solution: Served frontend using python -m http.server to run on http://127.0.0.1:5500
2. CORS Issue (Frontend ↔ Backend Communication)
   - Problem: Frontend was unable to fetch data from backend (requests failing silently / blocked)
   - Reason: Frontend (running on http://127.0.0.1:5500) and backend (http://127.0.0.1:5000) are different origins, and browser blocks such cross-origin requests by default
   - Solution: Installed flask-cors and enabled CORS in backend using CORS(app)

Day 3 - Dockerization & Container Setup

- Understood Docker fundamentals (Dockerfile, Image, Container)
- Created Dockerfile for Flask backend
- Defined base image, working directory, dependencies, and startup command
- Built Docker image using docker build command
- Ran Docker container using port mapping (-p 5000:5000)
- Connected containerized backend with frontend application
- Successfully tested API via browser (http://127.0.0.1:5000/jobs)
- Achieved working flow: Frontend (5500) → Docker Backend (5000)

Issues Faced & Resolved:

- Backend Not Accessible from Browser (Docker)
- Problem: API was not reachable after running container
- Reason: Flask app was running on 127.0.0.1 inside container (only accessible internally)
- Solution: Updated app to run on host='0.0.0.0' to allow external access

Understanding Port Mapping Confusion

- Problem: Confusion between host port and container port
- Reason: Misunderstanding of how Docker exposes services
- Solution: Learned -p host_port:container_port mapping concept

Frontend Behavior Difference (file:// vs http://)

- Problem: Frontend worked when opened directly but not in server mode
- Reason: Browser treats file:// and http:// differently (CORS + request handling)
- Solution: Used python -m http.server to simulate real-world frontend hosting

🚀 Outcome:
Backend successfully containerized and running independently in Docker with proper frontend integration.

### Day 4 - Documentation Overhaul & Architectural Refinement
- **Goal:** Elevate project presentation to professional standards and bridge the gap between "Learning" and "Enterprise" design.
- **Achievements:**
    - **README Reconstruction:** Rewrote the main documentation to be "Recruiter-Ready," using industry-standard badges and clear technical service mapping.
    - **Architectural Scaling:** Refined the system diagram to include high-value security services like **CloudFront OAC** (Origin Access Control), **AWS Secrets Manager**, and **SSM**.
    - **System Design Analysis:** Authored a "Professional vs. Free Tier" comparison to demonstrate understanding of High Availability (HA) and Disaster Recovery (DR) concepts.
    - **Documentation-as-Code:** Organized a structured `docs/` hierarchy to separate architectural logic from daily execution logs.
- **Challenge:** Translating complex AWS networking concepts (NACLs, IGW, Subnets) into a clean, readable visual and written format.
- **Outcome:** A repository that not only shows code but proves architectural competency and cost-optimization awareness.

