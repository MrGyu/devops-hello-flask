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
Linux / macOS:

bash
Kód másolása
python -m venv venv
source venv/bin/activate
2.2 Dependenciák telepítése
bash
Kód másolása
pip install -r requirements.txt
2.3 Alkalmazás futtatása
bash
Kód másolása
python app.py
3. Docker használata
A projekt tartalmaz egy Dockerfile-t, amellyel az alkalmazás konténerbe csomagolható.

3.1 Docker image buildelése
bash
Kód másolása
docker build -t devops-hello-flask:v1 .
3.2 Konténer futtatása (8080-as port)
bash
Kód másolása
docker run -p 8080:8080 devops-hello-flask:v1
4. Git – Trunk-alapú fejlesztés
A projekt GitHub repója:
https://github.com/MrGyu/devops-hello-flask

A fejlesztés trunk-alapú modell szerint történt:

main = stabil ág

módosítások rövid életű feature branch-ekben

merge vissza a trunkba

Példa folyamat:

bash
Kód másolása
git checkout -b feature/update-message
git add app.py
git commit -m "Üzenet frissítése"
git checkout main
git merge feature/update-message
git push
5. CI – GitHub Actions + Docker Hub integráció
A projekt tartalmaz egy automatizált CI pipelinet:
.github/workflows/ci.yml

A pipeline automatikusan lefut:

minden push esetén a main branch-re

minden pull request esetén

A pipeline lépései:
Repo checkout

Python környezet beállítása

Dependenciák telepítése

Docker Hub login (GitHub Secrets alapján)

Docker image build

Docker image push Docker Hub-ra

Publikus Docker image:

bash
Kód másolása
mrgyu/devops-hello-flask:latest
Lehúzás és futtatás:

bash
Kód másolása
docker pull mrgyu/devops-hello-flask:latest
docker run -p 8080:8080 mrgyu/devops-hello-flask:latest
6. Projekt struktúrája
markdown
Kód másolása
devops-hello-flask/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
7. Megjegyzések
A Flask fejlesztői szerver nem produkciós célra készült.

Konténerben futtatva a szerver automatikusan indul.

A CI pipeline minden push esetén új Docker image-et készít.

A Docker Hub-on tárolt image bármikor reprodukálható.

A .gitignore kizárja a felesleges fájlokat.

8. Alkalmazás végpontok
/ – alap "Hello DevOps" üzenet

/info – metaadatok

/health – egyszerű státuszjelzés
