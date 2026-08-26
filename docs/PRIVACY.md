# Privacy Design

## Core Principle

The system follows a privacy-first, data-minimization approach.

## Data Access

- Email scanning is explicitly initiated by the user.
- The extension focuses on the currently selected email.
- Unrelated mailbox data should not be collected.
- Browsing history, cookies and unrelated account information are not required.

## Local Processing

Where practical, preprocessing and minimization should happen locally before data is sent to the backend.

## Data Minimization

Only security-relevant information should be sent for deeper analysis.

Examples include:
- URLs
- domains
- authentication results
- relevant email headers
- originating IP where available
- attachment metadata
- attachment SHA-256 hashes
- sanitized email text required for analysis

## Sensitive Information

Unnecessary personal information should be minimized or redacted where practical without removing security-relevant evidence.

## Attachments

Prefer generating a SHA-256 hash locally and checking the hash through threat-intelligence services rather than uploading the original attachment when possible.

## Backend Storage

MongoDB should store only information required for security analysis, investigation and audit.

## Analyst Access

Sensitive content should be minimized/redacted by default and disclosed only when required for investigation.

## Secrets

API keys, database credentials and other secrets must be stored in environment variables and must never be committed to GitHub.

## Important Limitation

The project should only claim privacy protections that are actually implemented and tested.
