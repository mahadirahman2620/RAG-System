
# API Documentation — Multilingual RAG System (FastAPI)

## Base URL

```
http://localhost:8000
```

---

## Endpoint: `/ask`

**POST** `/ask`

### Description:
Accepts a user query in either **Bangla** or **English**, retrieves relevant information from the `HSC26-Bangla1st-Paper.pdf`, and generates an answer based on context.

---

## Request Body

```json
{
  "question": "অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?"
}
```

| Field     | Type   | Description                                 |
|-----------|--------|---------------------------------------------|
| question  | string | The user’s question (Bangla or English)     |

---

## Response Body

```json
{
  "answer": "Based on the context: '...অনুপম তাঁর লেখায় শম্ভুনাথকে সুপুরুষ হিসেবে বর্ণনা করেছেন...', the answer to your question 'অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?' is likely found there."
}
```

| Field   | Type   | Description                               |
|---------|--------|-------------------------------------------|
| answer  | string | Generated answer based on document context |

---

## Sample Test Cases

| Input Query (Bangla)                               | Expected Output   |
|----------------------------------------------------|-------------------|
| অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?             | শম্ভুনাথ           |
| অনুপমের ভাগ্যদেবতা কাকে বলা হয়েছে?                | মামা              |
| কল্যাণীর বিয়ের সময় বয়স কত ছিল?                     | ১৫ বছর            |

---

## API Usage Guide

1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

2. Open in browser:
   ```
   http://localhost:8000/docs
   ```

3. Use Swagger UI to test your queries interactively.

---

## OpenAPI/Swagger UI

- FastAPI automatically provides a Swagger-based UI.
- Access it at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Error Handling

| Error Code | Description                   |
|------------|-------------------------------|
| 422        | Validation Error (e.g. missing `question` field) |
| 500        | Server Error (e.g. PDF not loaded, vector issue) |
