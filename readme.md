Сделал полезные для начала работы с NHANES программки:

(1) "download.py" закачивает все файлы с данными исследований из всех NHANES от 1999 до 2019 года, в структурированном порядке, а также NHANES III.
Это всё весит примерно 22 гигабайта.

(2) "analyse-glucose.py" - показывает простой пример работы с этими скачанными базами данных. Вытаскивает из всех их данные по глюкозе и возрасту и строит два графика — график всех точек (возраст, глюкоза) и изменение с возрастом 10/20/30/.../90 процентных персентилей глюкозы в популяции.

Обе программки можно скачать здесь https://disk.yandex.ru/d/JXrLil3uq2YaIA 
Подробные инструкции по тому, как видоизменить программку "analyse-glucose.py" для работы с другими анализами из баз NHANES написал здесь:
https://rizzoma.com/topic/0178555743735eb69cb366683cd0b9ee/0_b_c495_br98b/ (инструкции рассчитаны на человека, который умеет программировать, и просто рассказывают, как найти в базах данных нужные анализы).

Был бы очень рад получить от кого-нибудь
(а) базы названий переменных для разных NHANES по годам (типа глюкоза называется 'LBXGLUSI' для первых двух NHANES и 'LBDGLUSI' для следующих, а в NHANES III она на полях 1871-1876)
(б) базы названий файлов для разных NHANES (типа данные по глюкозе находятся в файлах 'LAB10AM', 'L10AM_B', 'L10AM_C', 'GLU_D', 'GLU_E' ... для разных NHANES, а в NHANES III она в lab.dat)
Пусть даже в сыром виде, я разберусь. А то там жуткое количество муторной работы, всё это выписывать.
