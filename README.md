# DRF로 구현한 포토카드 조회/판매/구매 API

## 실행방법

### 1. 가상환경 세팅
   ```python
   Windows:
   1. python -m venv venv
   2. venv\Scripts\activate.bat
   3. pip install -r requirements.txt
   
   Mac:
   1. python -m venv venv
   2. source venv\bin\activate
   3. pip install -r requirements.txt
   ```

### 2. migrate
  `python manage.py migrate`

### 3. Test Data Insert
  `python manage.py seed`

### 4. 서버실행
  `python manage.py runserver`

---

## API 명세
| http://127.0.0.1:8000/swagger/
