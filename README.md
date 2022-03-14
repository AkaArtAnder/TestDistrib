# Test norm distribution
Программа проверки последовательности на нормальность
## Особенности запуска
В корне должна быть директория `result/`. Там будут находиться результаты работы программы.

Файл с последовательностью, которая будет подвергнута проверке должна, так же находиться в корне.

Для открытия справки 
```
python test.py -h
```

### Пример
```
python test.py -fr new_norm.txt
```
В директории `/result` будут находиться результаты проверки.
1. `hist.png` - гистограмма значений;
2. `param_data.xls` - мат. ожидание и дисперсия проверенной последовательности;
3. `qqplot.png` - квантиль-квантиль график;
4. `test_result` - результаты проверки последовательности на нормальность по 3 основным статистическим критериям.
