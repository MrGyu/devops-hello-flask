DevOps – Hello World webalkalmazás Flask (Python) használatával

Ez a projekt egy egyszerű „Hello DevOps” Flask webalkalmazást futtat, amelyen keresztül bemutatom az alapvető DevOps lépéseket:

program forráskód

verziókezelés (trunk-alapú fejlesztés)

buildelés

konténerizálás (Dockerrel)

CI pipeline + Docker Hub registry-be feltöltés

1. Alkalmazás

Az alkalmazás egy minimális Flask webszolgáltatás, amely HTTP-n keresztül érhető el, és egyszerű szövegeket jelenít meg.

Elérhetősége futtatás esetén:
http://localhost:8080

Nyilvános DockerHub repo:

https://hub.docker.com/r/mrgyu/devops-hello-flask

Forráskód az alkalmazáshoz:

app.py

2. Buildelés és futtatás lokálisan
2.1 Virtuális környezet létrehozása

Windows:

python -m venv venv
venv\Scripts\activate


Linux / macOS:

python -m venv venv
source venv/bin/activate

2.2 Dependenciák telepítése
pip install -r requirements.txt

2.3 Alkalmazás futtatása
python app.py

3. Docker használata

A projekt tartalmaz egy működő Dockerfile-t, amely lehetővé teszi az alkalmazás konténerizálását.

3.1 Docker image buildelése
docker build -t devops-hello-flask:v1 .

3.2 Docker konténer futtatása (8080-as port)
docker run -p 8080:8080 devops-hello-flask:v1

4. Git – Trunk-alapú fejlesztés

A projekt GitHub repója:
https://github.com/MrGyu/devops-hello-flask

A fejlesztés trunk-based modell szerint történt:

main → stabil, élesre szánt ág

fejlesztések → rövid életű feature brancheken

a kész munkák merge-elve kerülnek vissza a main-re

Példafolyamat:
# módosítások az app.py-ben
git checkout -b feature/update-message
git add app.py
git commit -m "Üzenet frissítése"
git checkout main
git merge feature/update-message
git push

5. CI – GitHub Actions és Docker Hub integráció

A projekt automatikus CI folyamatot használ:
.github/workflows/ci.yml

A pipeline automatikusan lefut:

minden push esetén a main ágra

minden pull request esetén a main ágra

A pipeline fő lépései:

Repository checkout

Python környezet beállítása

Dependenciák telepítése

Docker Hub bejelentkezés (GitHub Secrets használatával)

Docker image build

Docker image push Docker Hubra

Publikus Docker image:
mrgyu/devops-hello-flask:latest

Image letöltése és futtatása:
docker pull mrgyu/devops-hello-flask:latest
docker run -p 8080:8080 mrgyu/devops-hello-flask:latest

6. Projekt struktúrája
devops-hello-flask/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
└── .github/
    └── workflows/
        └── ci.yml

7. Egyéb megjegyzések

A Flask fejlesztői szerver nem produkciós környezetre készült.

Konténerben futtatva az alkalmazás automatikusan elindul.

A CI pipeline minden push után új Docker image-et generál.

A Docker Hub-on tárolt image teljes mértékben reprodukálható.

A trunk-based fejlesztési módszer átlátható és könnyen követhető.

A .gitignore segít kizárni a nem kívánt vagy generált fájlokat.

Az alkalmazás végpontjai:

/ – alap „Hello DevOps” üzenet

/info – információk az alkalmazásról

/egeszseg – egyszerű működés-visszajelzés (health check)

8. Fejlesztői konténer (VSCode Dev Container - opcionális)

A projekt tartalmazhat VSCode DevContainer konfigurációt, amely lehetővé teszi, hogy a teljes fejlesztői környezet konténerben fusson.

Használata:

Nyisd meg a projektet VSCode-ban.

Telepítsd a "Dev Containers" bővítményt.

Az alul megjelenő értesítésnél válaszd: Reopen in Container

A konténerben nyiss egy terminált és futtasd:

python app.py