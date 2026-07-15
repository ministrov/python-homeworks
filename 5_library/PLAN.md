# План: library.py — filter/sort по CLI-аргументу

Задача: программа работает с каталогом `books` (название → автор) и в
зависимости от `action` (`sys.argv[1]`) либо фильтрует книги, либо
сортирует список.

## Статус

- [x] Шаг 1 — разбор аргументов командной строки (сделано,
      `action`/`argument` уже читаются из `sys.argv`)
- [x] Шаг 2 — общая функция форматирования (сделано, `format_entry`)
- [x] Шаг 3 — ветка `action == "filter"` (сделано)
- [x] Шаг 4 — ветка `action == "sort"` (сделано)
- [x] Шаг 5 — диспетчеризация (`if/elif`) и финальная проверка
      (сделано, план закрыт)

## Шаг 1. Разбор аргументов командной строки (готово)

- `sys.argv[0]` — имя скрипта, не используется.
- `action = sys.argv[1]` — режим работы (`"filter"` или `"sort"`).
- `argument = sys.argv[2]` — второй параметр, смысл зависит от `action`:
  - для `"filter"` — список названий книг одной строкой, через запятую
    (например `"Идиот,Нос"`);
  - для `"sort"` — поле сортировки: `"book"` или `"author"`.
- Проверка `if len(sys.argv) < 3: ... sys.exit(1)` — защита от
  `IndexError`, если аргументы не переданы.

## Шаг 2. Общая часть — форматирование строки книги

Обеим веткам нужна одна и та же трансформация: пара `(книга, автор)` →
строка `"Книга — Автор"`.

- Вынести в отдельную именованную функцию, например
  `format_entry(title: str, author: str) -> str`, а не дублировать
  лямбду дважды — она понадобится и в `filter`-ветке, и в `sort`-ветке.
- Формат строки: `f"{title} — {author}"` (тире `—`, как в остальных
  демо-файлах).

## Шаг 3. Ветка `action == "filter"`

1. [x] Раздели `argument` по запятой в список нужных названий (сделано:
   `titles = [t.strip() for t in argument.split(",")]`).
2. [x] Примени `filter()` к `books.items()`: лямбда проверяет, что `title`
   (первый элемент пары) входит в список нужных названий из шага 1
   (сделано: `filtered = filter(lambda pair: pair[0] in titles, books.items())`).
3. [x] Результат `filter` — пары `(title, author)`. Примени `map()` с
   `format_entry`, распаковывая пару (сделано:
   `result = list(map(lambda pair: format_entry(*pair), filtered))`).
4. [x] Выведи результат построчно (сделано:
   `for line in result: print(line)`).
5. [x] Крайний случай: если после `filter` список пуст — выведи
   отдельное сообщение, а не пустой список (сделано: `print(...)` +
   `sys.exit(1)`, без `raise` — это не программная ошибка, а обычный
   исход поиска).

## Шаг 4. Ветка `action == "sort"`

1. [x] Через `map()` по `books.items()` с `format_entry` собери список
   строк `"Книга — Автор"` (map — первым, как указано в задаче;
   сделано: `pair_strings = list(map(lambda pair: format_entry(*pair),
   books.items()))`; временный `print(pair_strings)` оставлен для
   проверки, уберётся при переходе к диспетчеризации).
2. [x] Отсортируй список `sorted()`, передав `key` в зависимости от
   `argument` (сделано: `if/elif` выбирает `sort_key_index` — 0 для
   `"book"`, 1 для `"author"` — и он передаётся в
   `s.split(" — ")[sort_key_index]`).
3. [x] Крайний случай: если `argument` не `"book"` и не `"author"` —
   вывести сообщение о неизвестном параметре сортировки (сделано:
   `else: print(...) + sys.exit(1)`, как в `filter`-ветке).
4. [x] Выведи отсортированный список (сделано:
   `for line in sorted_strings: print(line)`).

## Шаг 5. Диспетчеризация действия (готово)

- [x] `if action == "filter": ... elif action == "sort": ... else: ...` —
  `else` печатает сообщение о неизвестном `action` (сделано, см.
  `library.py`). `format_entry` осталась общей, вне веток.
- (Опционально, стретч-цель: заменить на dispatch table словарём
  `{"filter": ..., "sort": ...}`, как в теме 7 `07_functions_as_objects_demo.py`
  — не обязательно для этой задачи, не сделано.)

## Типизация под Pylance strict

- `books: dict[str, str]` уже аннотирован — `.items()` в `filter`/`map`
  обычно даёт `tuple[str, str]` без доп. усилий.
- Если увидишь `reportUnknownLambdaType` — аннотируй промежуточную
  переменную явно, например
  `filtered: list[tuple[str, str]] = list(filter(...))`.

## Проверка вручную

```
python homeworks/5-library/library.py filter "Идиот,Нос"
python homeworks/5-library/library.py sort book
python homeworks/5-library/library.py sort author
```
