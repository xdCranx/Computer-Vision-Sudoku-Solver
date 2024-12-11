
# Computer-Vision-Sudoku-Solver
Project designed and implemented as engineering thesis.

The repository consists a system capable of detecting, recognising and solving a Sudoku puzzle from a uploaded image.
System is split into two parts: 

- Core written in Python that acts as a REST API (backend)
- Webapp interface written using Next.js framework (frontend)




## Instalation and starting

### Prerequisites
(Developed and tested with)
- Python v3.12.7
- Node.js v23.3.0


### API
To install all the required packages you need to create a Python virtual environment and using pip download dependencies defined in ``requirements.txt``.

```bash
pip install -r requirements.txt
```

afterwards, while being in the root directory of the API (``sudoku-solver-api/``) run the following command:
```bash
uvicorn main:app
```
the API shoud start and run on ``localhost`` using port 8000.


### Webapp interface
The web application is implemented using the Next.js framework, so to run it you need to have Node.js installed (https://nodejs.org/en).

While being in the root of the web application(``sudoku-solver-webapp/``), run following commands:
- to install all the dependencies:
```bash
npm install
```
- to build the app:
```bash
npm run build
```
- to start the application:
```bash
npm run start
```
- (opt) to run in dev mode which does not require building beforehand:
```bash
npm run dev
```

Afterwards teh app should be running on ``localhost`` using por 3000.

To access the web application open http://localhost:3000 in your browser.


## Usage
While both API and Web application are running, go to http://localhost:3000 in your browser.
The web app serves as a graphic interface to allow simple usage of the system's core functionalities. It allows you to drag&drop the picture on a specified field or by clicking on it opens a file explorer to choose a image file containing the Sudoku puzzle. 

In case of succesful detection of the puzzle, after loading circle dissapears the solution should be displayed.
If the picture is not clear enough for the system to recognize the puzzle, it will return its "guess" of the puzzle without actual solution. This allows to chceck which numbers were not recognized or mistook as different ones.

Any other errors would result in erro mesage being displayed.

There is also a "RESET" button that refreshes the interface and allows to upload a new picture. 
