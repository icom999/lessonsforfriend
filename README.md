# Lesson for my friend

Это для моего друга.

### НАЧАЛО ПИТОН 

Созданы несколько папок в них будут задания и примеры.
1. [Lesson1](./Lesson1/Lesson1.md) 




### Репозиторий

Практика работы с репозиторием. 

Все детали в этой [ссылке](GIT_GITHUB.md)

### Общеее выполнение заданий

Для нас важно не только выполнить само задание написав скрипт на Питоне , но также и уметь хорошо организовать файлы и учиться работать с версиями и репозиториями.

Мы для версий (Version Source Control - VSC git) будем всегда использовать git. 

**Мы подразумеваем** что у нас уже организован сам репозиторий и мы продолжаем выполнять задания уже в созданном репозитории!!!

1. Для выполнения задания нам необходимо создать новый файл. **Здесь** важно отметить что файл должен быть создан не в корне папки самого репозитория а во вложенной папке. Это будет лучше для организации большого количества файлов в одном репозитории. Можно также создавать много уровней вложенных папок.
2. После создания нового файла с раширением .py Питона для выполнения задания у нас в Visual Studio Code этот ![green file](/IMG/green_file.svg)файл.py подсветиться зеленым.
3. Пока этот файл подсвечиватся зеленым в Visual Studio Code означает что мы еще не сказали git отслеживать изменения(CHANGES) в этом файле. И мы можем работать с другими файлами делая изменения в них.
4. Нам не нужно добавлять git новые файлы пока мы точно не знаем что мы завершили работу.
5. Но такое может случиться что мы сказали git отслеживать изменения в каком-то файле и теперь git будет подсвечивать такой файл оранжевым. И у нас может возникнуть необходимость обновить нашу локальную папку репозитория на нашем компьютере из репозитория на github. И тут нам надо сохранить все изменения в нашей локальной репозитории сделав `git commit`.
6. ХОРОШАЯ ПРАКТИКА разработки, _которой мы будем следовать_ , говорит нам что для начала выполнения нового задания или даже до момента как мы хотим создать новый файл(даже если мы уже создали новый файл _подсвеченный зеленым_ и не сказали git отслеживать в нем изменения) нам надо создать отдельную ветку для этого задания. Выполнив команду в терминале : `git checkout -b название` или в Visual Studio Code используя сохранение версий выбрать "Checkout to..." и "Create New Branch".  
   ![vsc](/IMG/VCS_NewBranch.png)
7. Далее работаем над заданием.



