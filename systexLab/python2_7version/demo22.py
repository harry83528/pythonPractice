#encoding=UTF-8
print '==={:<10}==='.format('OK')
print '==={:_<10}==='.format('OK')
print '==={:*<10}==='.format('OK')
print '==={:\'<10}==='.format('OK')
print '==={:"<10}==='.format('OK')
print '==={:^>10}==='.format('OK')
print '==={:^^10}==='.format('OK')
print '==={:.6}==='.format('OKOKOKOKOK')
print '===%.6s==='%('WELCOMEWELCOME')
print '==={:.6}==='.format('這是中文的內容')
print '===%.6s==='%('這是中文的內容')
print u'==={:.6}==='.format(u'這是中文的內容')
print '===%.6s==='%(u'這是中文的內容')
print '==={:.7}==='.format('這是中文的內容')
print '===%.8s==='%('這是中文的內容')