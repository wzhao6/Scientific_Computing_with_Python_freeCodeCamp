def add_time(start, duration, day=None):
  st = start.replace(':', ' ').split()
  du = duration.split(':')
  st_h = int(st[0])
  nt_m =''
  m_to_h = 0
  nt_h =0
  day_n =0
  day_new=''
  day_new_n=0

  if st[2] == 'PM':
    st_h = int(st[0]) + 12
  
  nt_m = "{0:0=2d}".format((int(st[1]) + int(du[1]))%60)
  m_to_h = (int(st[1]) + int(du[1]))//60
  nt_h = (st_h + int(du[0]) + m_to_h)%24
  if nt_h > 12:
    nt_m += ' PM'
    nt_h -= 12
  elif nt_h == 12:
    nt_m += ' PM'
  elif nt_h >= 1:
    nt_m += ' AM'
  else: 
    nt_h += 12
    nt_m += ' AM'
  nt = str(nt_h) + ':' + nt_m
  nt_d = (st_h + int(du[0]) + m_to_h)//24

  if day != None:
    day = day.casefold()
    ls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    l = [k.casefold() == day for k in ls]
    day_n = [i for i, x in enumerate(l) if x][0]
    day_new_n = (nt_d + day_n)%7
    day_new = ls[day_new_n]
    if nt_d == 1:
      new_time = nt + ', ' + day_new + ' (next day)'
    elif nt_d > 1:
      new_time = nt + ', ' + day_new + ' ({} days later)'.format(nt_d)
    else: new_time = nt + ', ' + day_new
  
  else:
    if nt_d ==1:
      new_time = nt + ' (next day)'
    elif nt_d > 1:
      new_time = nt + ' ({} days later)'.format(nt_d)
    else: new_time = nt


  return new_time