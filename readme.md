# activar entorno virtual en powershell .\venv\Scripts\activate.ps1 

# dos formas de ejcutar fastapi
    1.-uvicorn main:app 
   
    (requiere de importación ) 
        ** from fastapi import FastAPI
    
    ejecución 
        ** app = FastAPI()
    
    2.-python main.py
       agregar las lineas de codigo a lo anterior:    
       
       importación:
       import uvicorn 

       if __name__ == "__main__":
             uvicorn.run("main:app", port=8000) 
