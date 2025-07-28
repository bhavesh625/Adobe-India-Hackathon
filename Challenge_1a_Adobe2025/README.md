# Adobe India Hackathon – Round 1A

## 🚀 Overview
This solution extracts document structure (Title, H1, H2, H3) from PDFs using `pdfminer.six` and outputs JSONs per Adobe schema.

## 🧠 Approach
- Analyze layout using `pdfminer.six`
- Detect font sizes dynamically
- Rank font frequencies to classify heading levels

## 🐳 Docker Build & Run

```bash
docker build --platform=linux/amd64 -t pdf-processor .
docker run --rm \
  -v $(pwd)/sample_dataset/pdfs:/app/input:ro \
  -v $(pwd)/sample_dataset/outputs:/app/output \
  --network none pdf-processor
```

## ✅ Constraints Met
- No internet access
- ≤ 10s for 50-page
- ≤ 200MB, runs on CPU
