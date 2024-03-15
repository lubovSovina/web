import schedule

i = 1


def job(name):
    global i
    print(f'запуск {i} name={name}')
    i += 1
    if i == 5:
        return schedule.CancelJob


schedule.every(1).to(3).seconds.do(job, name='Yandex')
while True:
    schedule.run_pending()
