# 🧰 Resume ATS Stack — Because Finding a Job Should Have a CI/CD Pipeline

Welcome to **resume-ats-stack**, a highly unnecessary yet deeply satisfying DevOps-powered ATS resume delivery system.
Because when you're looking for work, nothing screams "hire me" louder than deploying your own PDF resume pipeline with MinIO, Redis and Headless Chrome.

---

## 🎯 Why This Exists

After months of grinding job applications, ATS rejection bots, silent HR black holes, “we chose to move forward with other candidates”, and LinkedIn’s depressing “your application has been viewed”, I decided to embrace the madness.

So I deployed my own resume service. In my home lab. With Docker, MinIO, Redis, Postgres and Headless Chrome. Automated with Ansible.

Because if companies won’t deploy me in production, I will deploy myself.

---

# 🏗️ Architecture (aka the DevOps Therapy Diagram)

The stack consists of:

- **Reactive Resume** — UI for editing and managing resumes
- **Postgres** — persistent storage for resume schema + metadata
- **Redis** — cache for authentication sessions & general speed
- **MinIO (S3 compatible)** — storage for profile photos + public assets
- **Browserless Chrome** — generates ATS-compliant PDF exports
- **Docker Compose** — the glue of the universe
- **Ansible** — because SSHing manually into servers is barbaric

No Kubernetes. Because this is a resume, not a fintech unicorn.

---

# 🛠️ Deployment Requirements

This stack assumes:

✔ one Linux VM (Debian/Ubuntu recommended)
✔ at least **4GB RAM** (Chrome is needy)
✔ functional internet (Chrome pulls fonts)
✔ you appreciate overengineering

Tested in a homelab environment, because cloud credits ran out.

---

# 🚀 Deployment Pipeline (Ansible-Driven)

This stack is deployed via Ansible with **two playbooks in sequence**:

---

### **1. Preflight Playbook**

```sh
ansible-playbook preflight.yml -i inventory
What it does:

✔ updates system
✔ installs Docker + Docker Compose plugin
✔ configures directories & file paths
✔ validates system dependencies
✔ ensures everything is not on fire

2. Site Playbook

ansible-playbook site.yml -i inventory
What it deploys:

✔ full docker stack
✔ MinIO bucket
✔ MinIO policy (public)
✔ Reactive Resume backend
✔ Browserless Chrome worker

After this, you go to:

http://<host>:3000
and begin the ritual of editing your resume again for the 300th time.

🌎 Ansible Inventory Example

[resume-stack]
resume01 ansible_host=192.168.22.204 ansible_user=root

Yes, it runs in a homelab.
No regrets.

🗃️ MinIO Configuration
MinIO stores:
profile pictures
resume assets
public static exports

Bucket required:
resumes

Policy must be:
public

Otherwise your face won't render and hiring managers may assume you're being artistic.

Access via:
http://<host>:9001

Log in with:
minioadmin / minioadmin


📦 Stack Components & Ports
Service	Port	Description
Reactive Resume	3000	Web UI + API
Postgres	5432	Database
Redis	6379	Cache
MinIO Console	9001	Bucket UI
MinIO S3	9000	S3 endpoint
Headless Chrome	9222	PDF render

🧪 Testing the System
Check API health:
curl -I http://localhost:3000/api/health

Check Chrome:
curl -I http://localhost:9222

If Chrome responds 403 Forbidden, congratulations:
It's alive and silently judging you.

🖨️ ATS Compliance Level
This system produces PDFs that are:

✔ selectable text
✔ not embedded as images
✔ consistent layout
✔ machine-readable
✔ recruiter-safe

Does it guarantee a job?
No. But at least rejection will be automated and technically elegant.

💾 Persistence & Backup
Data survives via:
Postgres volume
MinIO bucket
Docker volumes

Backup example:
docker compose down
tar zcvf resume-backup.tar.gz .

Restore example:
tar zxvf resume-backup.tar.gz
docker compose up -d

📈 Homelab CI/CD Career Boost Mode
Possible future improvements:
OAuth login (GitHub / Google)
Automatic PDF push to LinkedIn EasyApply
Terraform deployment module
Helm chart (for the clinically insane)
K3s support
On-chain timestamped resumes (because why not)
Self-hosted ATS rejection simulator

🧑‍💻 Author
Built by someone who:

✔ is not a fan of Kubernetes
✔ writes playbooks for fun
✔ monitors their homelab more than their sleep schedule
✔ is currently available for hire, please!!!

If you're a hiring manager reading this:

yes, you should schedule an interview with me.

🏁 Final Thoughts
Is this overengineered?
Absolutely.

Was it necessary?
Emotionally, yes.

Should you steal it?
Also yes.

