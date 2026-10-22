import sys


def count_paths(n: int, m: int) -> int:
    dp = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        dp.append(row)

    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i >= 2 and j >= 1:
                dp[i][j] += dp[i - 2][j - 1]
            if i >= 1 and j >= 2:
                dp[i][j] += dp[i - 1][j - 2]

    return dp[n - 1][m - 1]

def main() -> None:
    """
    Точка входа. Читает имена файлов из аргументов командной строки
    (по умолчанию input.txt / output.txt), считает ответ и записывает его.
    В конце печатает в stdout сообщение об успехе или причину ошибки.
    Возвращает ненулевой код выхода при ошибке (через sys.exit).
    """
    # --- 1. Разбор аргументов командной строки ---
    input_name = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    output_name = sys.argv[2] if len(sys.argv) > 2 else "output.txt"

    # --- 2. Чтение входного файла с обработкой ошибок ---
    try:
        with open(input_name, "r", encoding="utf-8") as f:
            data = f.read().split()
    except FileNotFoundError:
        print(f"Ошибка: входной файл '{input_name}' не найден.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Ошибка: нет прав на чтение файла '{input_name}'.", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Ошибка чтения файла '{input_name}': {e}", file=sys.stderr)
        sys.exit(1)

    # --- 3. Проверка корректности входных данных ---
    if len(data) < 2:
        print(f"Ошибка: в файле '{input_name}' должно быть два числа N и M.", file=sys.stderr)
        sys.exit(1)

    try:
        n, m = int(data[0]), int(data[1])
    except ValueError:
        print(f"Ошибка: '{data[0]}' и/или '{data[1]}' не являются целыми числами.", file=sys.stderr)
        sys.exit(1)

    if not (1 <= n <= 50 and 1 <= m <= 50):
        print(f"Ошибка: N и M должны быть в диапазоне 1..50 (получено N={n}, M={m}).", file=sys.stderr)
        sys.exit(1)

    # --- 4. Вычисление ответа ---
    answer = count_paths(n, m)

    # --- 5. Запись результата с обработкой ошибок ---
    try:
        with open(output_name, "w", encoding="utf-8") as f:
            f.write(str(answer))
    except PermissionError:
        print(f"Ошибка: нет прав на запись в файл '{output_name}'.", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        # Возникает, если родительская папка для output_name не существует
        print(f"Ошибка: путь к файлу '{output_name}' не существует.", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Ошибка записи файла '{output_name}': {e}", file=sys.stderr)
        sys.exit(1)

    # --- 6. Сообщение об успехе в stdout ---
    print(f"Успешно: прочитано из '{input_name}', результат {answer} записан в '{output_name}'.")


if __name__ == "__main__":
    main()
    