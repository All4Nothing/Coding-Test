def date_to_days(date: str) -> int:
    year, month, day = map(int, date.split('.'))
    days = (year-2000) * 28 * 12 + month * 28 + day
    return days

def solution(today, terms, privacies):
    answer = []
    today_days = date_to_days(today)
    terms_dict = {}
    for term in terms:
        typ, month = term.split()
        terms_dict[typ] = int(month) * 28
        
    for idx, privacy in enumerate(privacies):
        date, typ = privacy.split()
        
        if date_to_days(date) + terms_dict[typ] <= today_days:
            answer.append(idx+1)
    
    return answer