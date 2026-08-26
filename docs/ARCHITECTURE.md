# System Architecture

## End-to-End Workflow

User
↓
Chrome Extension
↓
Privacy / Data Minimization
↓
FastAPI Backend
↓
AI/ML + Networking + Threat Intelligence
↓
Explainable Risk Engine
↓
MongoDB
↓
Analyst Dashboard
↓
Analyst Decision
↓
Evidence Integrity / SHA-256
↓
Blockchain / Ledger

## Major Components

### Chrome Extension
- User-triggered email scanning
- Current email extraction
- Privacy-aware preprocessing
- Sends minimized security payload

### Privacy Layer
- Data minimization
- Redaction where practical
- No unrelated mailbox collection
- Security-relevant information preserved

### FastAPI Backend
- Receives scan requests
- Coordinates all analysis modules
- Calculates final risk
- Stores results

### AI/ML
- NLP model for email language/phishing intent
- Structured ML model for metadata/anomaly analysis

### Threat Intelligence
- URL/domain analysis
- IP reputation
- IP geolocation
- SPF/DKIM/DMARC
- VirusTotal
- AbuseIPDB
- Attachment hash analysis

### Risk Engine
Combines the available signals into a 0–100 risk score.

### MongoDB
Stores security cases, analysis results, indicators and analyst decisions.

### Analyst Dashboard
Allows cybersecurity analysts to:
- View high-risk cases
- Investigate evidence
- See risk explanations
- Review related indicators
- Make a decision

### Evidence Integrity
SHA-256 is used to fingerprint important evidence.
Blockchain/ledger can be used to preserve the fingerprint for later verification.
