from django.shortcuts import render


def patient_list(request):
    patients = [
        {'id': 24, 'name': 'Ковалев Алексей Сергеевич', 'age': 43, 'last': '05.10.2026', 'status': 'success'},
        {'id': 31, 'name': 'Кузнецова Мария Андреевна', 'age': 37, 'last': '02.10.2026', 'status': 'success'},
        {'id': 47, 'name': 'Ким Дмитрий Александрович', 'age': 51, 'last': '28.09.2026', 'status': 'warning'},
        {'id': 52, 'name': 'Иванов Иван Иванович',      'age': 45, 'last': None,         'status': 'neutral'},
        {'id': 25, 'name': 'Петрова Анна Сергеевна',    'age': 38, 'last': None,         'status': 'neutral'},
    ]
    return render(request, 'patients/list.html', {'patients': patients})