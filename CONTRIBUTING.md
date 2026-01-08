# 🤝 Contributing to Resume ATS Stack

First of all — thank you.
Anyone voluntarily contributing to an over-engineered résumé delivery system already has my respect and possibly my concern.

This project is powered by frustration with ATS systems, hiring pipelines, and job market absurdity. Contributions that make this stack more employable are highly welcome.

---

## 🧭 Ground Rules

Before submitting code, docs, memes, or unsolicited DevOps advice, please observe:

✔ Pull Requests welcome
✔ Humor welcome
✘ Broken pipelines discouraged
⚠ Kubernetes debates optional but dangerous
📝 Explanations required if changes improve job-search success rate

If a contribution fixes recruiters ghosting me, it will be merged immediately.

---

## 🧱 Architecture Overview (for Orientation & Sanity)

This stack uses:

- **Ansible** — deployment automation
- **Docker Compose** — container orchestration glue
- **Reactive Resume** — UI + ATS formatting engine
- **Postgres** — metadata & schema
- **Redis** — session cache
- **MinIO** — S3-compatible asset storage (profile photos, etc.)
- **Browserless Chrome** — PDF rendering farm
- **Homelab** — yes, really

If your contribution breaks PDF generation, you owe the maintainer coffee (or employment).

---

## 🧪 Branching Model

We use a lightweight Git flow style:

```
main          = stable deployment
feature/*     = new features
fix/*         = bug fixes
docs/*        = documentation
```

Example:

```sh
git checkout -b feature/chrome-pdf-scaling-fix
```

Nothing fancy. No 14-step release guild ceremonies.

---

## ✔ Submitting a Pull Request

Your PR should include:

- **Summary of change**
- **Motivation**
  e.g. “PDF alignment now respects human dignity”
- **Testing notes**
- **Screenshots (if applicable)**
  particularly for UI or PDF output
- **No hardcoded credentials** (unless you’re testing in homelab mode, no judgment)

PRs that make the system more ATS-friendly are highly valued.

PRs that make the system more dev-friendly are saintly.

PRs that fix actual employment prospects will be immortalized in the README.

---

## 🧰 Development Environment

### Required:

- `docker`
- `docker compose`
- `ansible`
- `python3`

### Optional (but comfy):

- `mc` (MinIO Client)
- `pgcli`
- `redis-cli`

Optional tooling may improve happiness by up to **37%**, according to no reputable study.

---

## 🚀 Running the Local Stack

Local launch:

```sh
docker compose up --build
```

Test Chrome PDF rendering service:

```sh
curl -I http://localhost:9222
```

If you receive `403 Forbidden`, great — Chrome is alive and silently judging you.

---

## 📌 Code Style & Conventions

Keep things tidy:

✔ YAML uses **2 spaces**, always
✔ Ansible tasks must be **idempotent** (no fire-and-pray)
✔ Shell scripts should be POSIX-friendly where possible
✔ No hardcoded credentials — use `.env`, vars, or vaults
✔ Avoid reinventing the wheel unless the wheel is funnier

---

## 🧹 Cleanup Commands

Clean local stack & volumes:

```sh
docker compose down -v
```

Clean MinIO buckets:

```sh
mc rm --recursive --force minio/resumes
```

Clean emotional state:
Not implemented yet. PRs welcome.

---

## 👋 Final Note

This project was built during peak hiring market existentialism.

If you contribute — thank you.
If you fork it — excellent taste.
If you hire the author — even better.

