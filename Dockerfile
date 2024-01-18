FROM python:3.8
RUN pip install pandas scikit-learn streamlit 
COPY src/* /app/
COPY model/* /app/model/pet_model.pkl
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]