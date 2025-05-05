# SchemeSeva Backend

## Setup

1. Install dependencies:
   ```bash
   cd backend
   npm install
   ```
2. Create a `.env` file in the backend directory with the following content:
   ```env
   MONGODB_URL=mongodb://127.0.0.1:27017
   DB_NAME=MySchemesDB
   PORT=8000
   ```
3. Start the server:
   ```bash
   npm run dev
   ```

The server will run on [http://localhost:8000](http://localhost:8000) and expose API endpoints at `/api/schemes`. 