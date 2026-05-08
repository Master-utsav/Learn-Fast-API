# FastAPI Project Setup

## Clone the Repository

```bash
git clone "https://github.com/Master-utsav/Learn-Fast-API"
```

---

## Open the Project

```bash
cd Learn-Fast-API
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

---

## Activate the Virtual Environment

### Windows PowerShell

Go inside:

```txt
venv/Scripts/
```

Copy the path of:

```txt
Activate.ps1
```

Then execute it in the terminal.

Example:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Setup Environment Variables

Create a `.env` file and add your PostgreSQL URL:

```env
DB_URL=postgresql://USERNAME:PASSWORD@localhost:5432/DATABASE_NAME
```

---

## Run the Server

```bash
python main.py
```

---

## Open Swagger Docs

Visit:

```txt
http://HOST:PORT/docs
```

Example:

```txt
http://127.0.0.1:5000/docs
```

Now you can test all the API endpoints directly from Swagger UI.
