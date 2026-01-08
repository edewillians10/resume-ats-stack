# 🔐 Security Policy

This project currently powers résumé delivery, PDF generation, and general DevOps coping mechanisms.

While it is not (yet) deployed at a Fortune-500 scale with 3 redundant regions and FIPS-validated HSMs, we choose to treat security seriously — because the job market already causes enough chaos.

---

## 🛡 Supported Versions

| Version | Supported |
|---------|----------|
| `main`  | Yes      |
| others  | No       |

If you're running an untracked fork, you are officially your own SRE team.

---

## 📣 Reporting Vulnerabilities

If you discover a security issue affecting:

- Ansible deployment
- Docker services
- MinIO storage access
- PDF generation pipeline
- Resume data exposure
- Infrastructure configs

please **do not disclose publicly** through GitHub Issues.

Instead, report privately to:

```
edewillians10@gmail.com
```

Please include:

- a description of the issue
- reproduction steps (if available)
- impact assessment
- recommended fix (optional but appreciated)
- whether you want credit (or plausible deniability)

Responsible disclosure is appreciated. Irresponsible disclosure will result in ATS simulations of your résumé.

---

## 🚫 Out-of-Scope Threats

This stack does **not** protect against:

- ATS keyword filters
- Recruiter ghosting
- The phrase “we went with another candidate”
- LinkedIn job application black holes
- Existential DevOps crises
- Late-night Terraform refactors

These require non-technical mitigation strategies (e.g., crying, coffee, and networking).

---

## 🧱 Deployment Security Best Practices

If you deploy in your own environment, please:

✔ run behind a firewall
✔ enable HTTPS (TLS terminator or reverse proxy)
✔ change MinIO access key/secret
✔ rotate JWT secrets
✔ restrict bucket access to public assets only
✔ disable public endpoints if privacy required
✔ monitor Chrome headless usage (PDF workers get spicy)

---

## 🔏 Secrets Checklist (Rotate These Regularly)

The following values exist in plain config and should be rotated:

- `STORAGE_ACCESS_KEY`
- `STORAGE_SECRET_KEY`
- `ACCESS_TOKEN_SECRET`
- `REFRESH_TOKEN_SECRET`
- `CHROME_TOKEN`

If you're doing DevOps correctly, you already forgot where you wrote these down.

---

## 🧩 Public Bucket Disclosure

MinIO serves profile images + exported PDFs.
If public sharing is intended, set bucket policy to:

```
public
```

If private storage is desired, set:

```
private
```

Note: If you configure MinIO incorrectly, **your face might not show up on the résumé**. This is currently categorized as a P2 incident.

---

## 🔒 Authentication & Access Notes

- Chrome exposes port `9222` for PDF rendering
- MinIO Console listens on `9001`
- S3 API listens on `9000`
- Resume UI/API listens on `3000`

If exposed to the internet, wrap in:

✔ TLS
✔ auth proxy
✔ firewall rules
✔ Zero-Trust (optional flex)

---

## 🎯 Final Note

This project exists because modern job-seeking requires more engineering effort than launching a satellite.

Respect the security posture, deploy responsibly, and please do not turn my résumé pipeline into a botnet.

If you improve security, the PR will be merged faster than HR can send a rejection email.

