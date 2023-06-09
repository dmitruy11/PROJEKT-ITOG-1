1. [Описание проекта]()
2. [Кейс]()
3. [Краткая информация о данных]()
4. [Этапы работы над проектом]()
4. [Результаты и выводы]()

1. # Описание проекта

## Предоставлены данные государственных органов о доходах, заболеваемости, социально незащищенных слоях населения России и другие экономические и демографические данные. Задача проекта - кластеризовать регионы России и определить, какие из них наиболее остро нуждаются в помощи малообеспеченным/неблагополучным слоям населения:




# Ваша задача:
## кластеризовать регионы России и определить, какие из них наиболее
## остро нуждаются в помощи малообеспеченным/неблагополучным
## слоям населения;
## описать группы населения, сталкивающиеся с бедностью;
## определить:
## влияет ли число детей, пенсионеров и других социально уязвимых
## групп на уровень бедности в регионе;
## связаны ли уровень бедности/социального неблагополучия с
## производством и потреблением в регионе;
## какие ещё зависимости можно наблюдать относительно
## социально незащищённых слоёв населения.



# Результаты и выводы
### На основе полученных датасетов сформирована финальная таблица по срезу 2020 г.

### В качестве критериев для группировки регионов в кластеры с близкими параметрами выбраны признаки, отражающие социально-экономическое благополучие субъектов федерации. Построены рейтинги регионов по избранным показателям. Исследованы распределения выбранных признаков и корреляции между ними, произведен отбор и выполнены необходимые преобразования. Итоговый модельный датасет для проведения кластеризации включает в себя 5 независимых характеристик:

### номинальную заработную плату, нормированную на прожиточный минимум в регионе;
### валовый региональный продукт в логарифмической шкале;
### объем розничной торговли на человека, нормированный на прожиточный минимум в регионе;
### жилую площадь на человека;
### процент населения за чертой бедности.
### С помощью различных внутренних метрик кластеризации оценено оптимальное количество кластеров (четыре). Построена базовая модель (k-means). Выполнено PCA-понижение размерности (3 главных компоненты, объясняющие 90% дисперсии). Протестированы различные алгоритмы кластеризации, из них на основе метрик и визуализации признакового пространства выбран оптимальный ("гауссова смесь на PCA-компонентах"), регионам присвоены соответствующие метки

## Дано описание характерных особенностей полученных кластеров:

### бедные регионы;
### среднестатистические регионы;
### регионы "комфорт"
### бизнес-регионы.
### Проведен анализ социально-демографических групп населения, показывающий, что наиболее уязвимой группой населения по финасовым показателям являются семьи с детьми. При этом в кластере наиболее бедных регионов наблюдается аномально высокая рождаемость, необеспеченная доходами родителей, а доля детей среди всего населения на 10% больше, чем в остальных регионах. В остальных группах рождаемость слабо растет с ростом финансового благополучия. При этом процент детского населения падает от кластера бедных регионов к кластерам более богатых. В бедных регионах отмечается существенно более низкий процент населения пенсионного возраста (на 10%).


