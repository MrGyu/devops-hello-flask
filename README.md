# DevOps – Hello World webalkalmazás Flask (Python) használatával

Ez a projekt egy egyszerű „Hello DevOps” Flask webalkalmazást futtat, amelyen keresztül bemutatom az alapvető DevOps lépéseket:

- program forráskód  
- verziókezelés (trunk-alapú fejlesztés)  
- buildelés  
- konténerizálás (Dockerrel)  
- CI pipeline + Docker Hub registry-be feltöltés  

---

## 1. Alkalmazás

Az alkalmazás egy minimális Flask webszolgáltatás, amely HTTP-n keresztül érhető el, és egyszerű szövegeket jelenít meg.

- **Elérhetősége futtatás esetén:**  
  http://localhost:8080

- **Nyilvános DockerHub repo:**  
  https://hub.docker.com/r/mrgyu/devops-hello-flask

- **Forráskód az alkalmazáshoz:**  
  `app.py`

---

## 2. Buildelés és futtatás lokálisan

### 2.1 Virtuális környezet létrehozása

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

---

### 2.2 Dependenciák telepítése
```bash
pip install -r requirements.txt
```

---

### 2.3 Alkalmazás futtatása
```bash
python app.py
```

---

## 3. Docker használata

A projekt tartalmaz egy Dockerfile-t, amellyel az alkalmazás konténerbe csomagolható.

### 3.1 Docker image buildelése
```bash
docker build -t devops-hello-flask:v1 .
```

### 3.2 Konténer futtatása (8080-as port)
```bash
docker run -p 8080:8080 devops-hello-flask:v1
```

---

## 4. Git – Trunk-alapú fejlesztés

A projekt GitHub repója:  
https://github.com/MrGyu/devops-hello-flask

A fejlesztés trunk-alapú modell szerint történt:

- **main = stabil ág**
- a módosítások **rövid életű feature branchekben** készültek
- majd merge vissza a main-re

Példa fejlesztési folyamat:
```bash
git checkout -b feature/update-message
git add app.py
git commit -m "Üzenet frissítése"
git checkout main
git merge feature/update-message
git push
```

---

## 5. CI – GitHub Actions + Docker Hub integráció

A projekt tartalmaz egy automatikus CI pipeline-t:  
`.github/workflows/ci.yml`

A pipeline automatikusan fut:

- minden push esetén a **main** branchen
- minden pull request esetén

### A pipeline lépései:

1. Repository checkout  
2. Python környezet beállítása  
3. Dependenciák telepítése  
4. Docker Hub login (GitHub Secrets segítségével)  
5. Docker image build, majd push a Docker Hubra  

### Publikus Docker Hub image:

**mrg yu/devops-hello-flask:latest**

Letöltés és futtatás:

```bash
docker pull mrgyu/devops-hello-flask:latest
docker run -p 8080:8080 mrgyu/devops-hello-flask:latest
```

---

## 6. Projekt struktúrája

```
devops-hello-flask/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
└── .github/
    └── workflows/
        └── ci.yml
```

---

## 7. Megjegyzések

- A Flask fejlesztői szerver **nem produkciós használatra készült**.  
- Konténerben futtatva a szerver automatikusan indul.  
- A CI pipeline minden módosítás után új Docker image-et generál.  
- A Docker Hub-on tárolt image **teljes mértékben reprodukálható**.  
- A trunk-based fejlesztés egyszerű és jól követhető.  
- A `.gitignore` biztosítja, hogy felesleges fájlok ne kerüljenek a repository-ba.

---

## 8. Alkalmazás végpontok

- `/` – alap „Hello World” válasz  
- `/info` – egyszerű információ az alkalmazásról  
- `/egeszseg` – healthcheck végpont
