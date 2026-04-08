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



