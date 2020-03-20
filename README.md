# tvml

##**Работа с датасетами**

tvml имеет доступ к списку экспериментов Barbacane. 
Нужен для того чтобы обновлять датасеты для соответстующих экспериментов или загружать определенную версию датасета чтобы обучить модель. 


tvml.DataWorker - дает доступ к датасетам в S3. 
Объект класса DataWorker требует как минимум один обязательный параметр - коннектор к S3. Так что, если ты не знаешь конкретно к какому эксперименту хочешь подключиться, используй experiments_info(), чтобы посмотреть список доступных экспериментов


### Установка  
```sh
$ pip install tvml
```

### Создание S3 коннектора
```python
import boto3

BUCKET = 'disk-barbacane-test'  # бакет, в котором хранятся датасеты
SRC_S3 = 'dataset_storage'      # папка, в которой хранятся датасеты
S3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, 
                        aws_secret_access_key=SECRET_KEY, 
                        region_name=REGION)
```

### Инициализация эксперимента
```python
from tvml.dsworker import DataWorker

experiment = DataWorker(S3)
experiment.experiments_info()
```
Получаем список имен существующих экспериментов:

```text
# output:

# experiment_id : experiment_name
{0: 'Default',
 1: 'tech',
 2: 'imagetype',
 3: 'graphtype',
 4: 'gutenindustries',
 5: 'gutenshifts',
 6: 'gutentag',
 7: 'ssdgraph',
 8: 'trasher'}
```

### Скачать готовую модель
Допустим, тебе нужна модель, определяющая технические графики, тогда выбирай эксперимент tech. Чтобы скачать последнюю версию, используй:
```python
experiment.pull_model('tech')
```
Можно указать путь, куда сохранять модель

```python
experiment.pull_model('tech', '/home/ubuntu/models')
```

### Скачивание датасета
Итак, ты определился с экспериментом. Теперь нужно скачать датасет. Для этогонужно указать 3 вещи:
- локальный путь для сохранения
- название датасета*
- версия датасета
> название датасета не равно названию эксперимента, сейчас есть такой недочет.

|Имя эксперимента|Имя датасета|
| ------ | ------ |
|tech|EXP-TECH|
|imagetype|EXP-IMG-TYPE|
|graphtype|GRAPHIC-PICTURE|
|ssdgraph|SSD-DATASET|
|trasher|?|
|gutentag|?|

Узнать сколько версий у эксперимента пока не получится, нужно смотреть в S3. Зато можно посмотреть информацию о классах датасета в заданной версии

```python
local_path = '/content'
exp_name = 'EXP-TECH' # tech model
version = 3 

os.makedirs(os.path.join(local_path, exp_name))

experiment = DataWorker(S3, local_path, exp_name, version)
experiment.info()
```

```text
# output:

EXP-TECH
V3
	 bloom 593
	 screen 585
	 norm 3909
	 tech 4510
```
```python
# скачать датасет EXP-TECH версии 3

experiment.download()
```

### Сохранение модели
После того, как эксперимент завершился и новая модель обучена, нужно сохранить ее на S3
```python
# выгрузить модель на S3
# можно указать путь до целевой модели
# иначе осуществляется поиск модели export.pkl 
# по стандартному пути

experiment.export_model_to_s3()
```
```text
#output:

Model has been uploaded to S3!
```

Если результат текущего эксперимента достоин места в продакшене, то зарегистрируй эту модель.
Регистрирация моделей работает в связке с Mlflow. 
```current_run_id``` можно получить только если использвать обертку млфлоу-обертку для обучения. Этого пока в пакете не предусмотрено.

```python
# exp_id можно узнать через experiments_info()
# current_run_id присваивается Mlflow

experiment.register_model(run_id=current_run_id, exp_id=1)
```

##Сообщайте о багах и предложениях
Если нашел баг или есть предложения по фичам, заводи Issue!
