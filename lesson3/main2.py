import datetime
import schedule

i = 1


def job():
    global i
    print(f'запуск {i}', end=' ')
    i += 1
    print(datetime.datetime.now())


schedule.every(5).seconds.do(job)
while True:
    schedule.run_pending()
