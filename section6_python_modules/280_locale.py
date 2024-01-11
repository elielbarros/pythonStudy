"""
# English
- Internationalization
How convert Python Information from English to a locale
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps
  &viewFallbackFrom=win10-ps

Categories:
 - LC_ALL
 - LC_TIME
 - LC_CTYPE
 - LC_COLLATE
 - LC_NUMERIC
 - LC_MESSAGES
 - LC_MONETARY

To use System Default Regional Configuration, let the second parameter with an empty string
 - locale.setlocale(locale.LC_ALL, '')

To use another type of 'locale', the operational system must have the regional configuration available,
if not it will not be possible

It is possible to know which regional configuration is available on ubuntu with the command 'locale'

To list every regional configuration on ubuntu use the command: 'locale -a'

# Portuguese
- Internacionalizacao
Como converter as informacoes Python de Ingles para local
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps
  &viewFallbackFrom=win10-ps

Categorias:
 - LC_ALL
 - LC_TIME
 - LC_CTYPE
 - LC_COLLATE
 - LC_NUMERIC
 - LC_MESSAGES
 - LC_MONETARY

Para usar configuracao regional padrao do sistema, deixar o segundo parametro com uma string vazia
 - locale.setlocale(locale.LC_ALL, '')

Para usar outro tipo de 'locale' o sistema operacional precisa ter a configuracao regional disponivel, se nao tiver nao
serah possivel.

Eh possivel saber qual configuracao regional esta disponivel no ubuntu com o comando: locale

Para listar as configuracoes regionais usar o comando: locale -a

"""
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'en_BW.utf8')

print(calendar.calendar(2024))
