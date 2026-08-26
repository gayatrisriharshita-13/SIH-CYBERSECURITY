# API Schema

## POST /api/scan

### Request

{
  "scan_id": "string",
  "sender": "string",
  "subject": "string",
  "sanitized_text": "string",
  "urls": [],
  "origin_ip": "string",
  "authentication": {
    "spf": "string",
    "dkim": "string",
    "dmarc": "string"
  },
  "attachments": [
    {
      "filename": "string",
      "sha256": "string"
    }
  ]
}

## Response

{
  "scan_id": "string",
  "risk_score": 0,
  "risk_level": "LOW",
  "reasons": [],
  "recommendation": "string"
}
