adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

DELIMITER = "\n-------------\n"

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Task 01")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("Перетворене речення")
print(adwentures_of_tom_sawer)
print(DELIMITER)

# task 02 ==
""" Замініть .... на пробіл
"""
double_space = "  "
one_space = " "
points = "...."
print("Task 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace(points, one_space)
print("Перетворене речення")
print(adwentures_of_tom_sawer)
print(DELIMITER)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("Task 03")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace(double_space+one_space, one_space)
print(adwentures_of_tom_sawer)
print(f"Кількість подвійніх пробілів: {adwentures_of_tom_sawer.count(double_space)}")
print(DELIMITER)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Task 04")
print(f"У тексті літера 'h' зустрілась {adwentures_of_tom_sawer.count('h')} разів")
print(DELIMITER)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("Task 05")
words = [word for word in adwentures_of_tom_sawer.replace('"', " ").split() if word[0].isupper()]
number_of_words = len(words)

print(f"У тексті слів що почінаються заглавними літерами: {words}. Всього {number_of_words} такіх слів.")
print(DELIMITER)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
TOM = "Tom"
print("Task 06")
first_occurrence_index = adwentures_of_tom_sawer.find(TOM)
second_occurrence_index = adwentures_of_tom_sawer.find(TOM, first_occurrence_index+1)
print(f"Позиція на якій зустічається слово {TOM} вдруге - {second_occurrence_index}")
print(DELIMITER)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("Task 07")
adwentures_of_tom_sawer_sentences = [sentence.lstrip() for sentence in adwentures_of_tom_sawer.split(".") if sentence]
print("Список речень:")
for sentence in adwentures_of_tom_sawer_sentences:
    print(sentence)
print(DELIMITER)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 08")
print("Четверте речення:")
print(adwentures_of_tom_sawer_sentences[3])
print("Перетворене речення в нижній регістр:")
print(adwentures_of_tom_sawer_sentences[3].lower())
print(DELIMITER)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("Task 09")
start_sentence = "By the time"
sentences = [ sentence for sentence in adwentures_of_tom_sawer_sentences if sentence.startswith(start_sentence)]

if sentences:
    print(f"Речення які почінаються з '{start_sentence}' знайдени в кількости {len(sentences)}:\n {sentences}")
else:
    print(f"Речення якє почінаються з '{start_sentence}' не знайдені")

print(DELIMITER)

                    
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("Task 10")
print(f"Кількість слів останнього речення - {len(adwentures_of_tom_sawer_sentences[-1].split())}")
print(DELIMITER)