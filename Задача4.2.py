import utils

utils.parsing_courses

utils.recalculating_course

if __name__ == '__main__':
    import sys

    source_currensy = sys.argv[1]
    destination_currency = 'RUB'
    amount = float('1')
    time_current_course,exchange_rate = utils.recalculating_course(source_currensy, amount)
    print('Актуальный курс на:', time_current_course)
    print(f'{source_currensy} = {exchange_rate} {destination_currency}')