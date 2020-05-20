#!/usr/bin/env python


def formatHour(n):
    if (n >= 10):
        return str(n)
    else:
        return "0" + str(n)

s_h, s_m = map(int, input().split(':'))
e_h, e_m = map(int, input().split(':'))

half_delta = (((e_h - s_h) * 60) - s_m + e_m) / 2
delta_in_hours = int(half_delta / 60)
m_h = s_h + delta_in_hours
m_candidate = int(s_m + half_delta - (delta_in_hours * 60))

if (m_candidate < 60):
    m_m = m_candidate
else:
    m_m = m_candidate - 60
    m_h = m_h + 1

print(formatHour(m_h) + ":" + formatHour(m_m))
