# 06 · Deployment & Scaling

**Objectives**
- Build and expose a simple FastAPI service.
- Understand health checks, payload validation, and logging.
- Discuss containerization (Docker) and scaling paths (Kubernetes).

**Lab (Autograded)**
- **Assignment:** “06-deploy-scale” on GitHub Classroom  
- **Tasks:**
  1. Implement a `/health` endpoint in `app/main.py` that returns `{ "status": "ok" }`.
  2. Implement a `/predict` endpoint that takes JSON input and echoes a prediction.
  3. Write tests using FastAPI’s `TestClient` to validate both endpoints.

**Quiz**
- 10 items covering FastAPI basics, API contracts, containerization, and scaling.

**Rubric**
- All tests pass (70%)  
- API contract clarity and input validation (20%)  
- Documentation (README with usage instructions) (10%)

**TalentLMS Unit Links**
- [Open the lab in GitHub Classroom](https://classroom.github.com/a/YOUR-INVITE-CODE)  
- [Take the Quiz](#)