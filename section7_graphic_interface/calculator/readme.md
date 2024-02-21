### English
- To initialize the calculator it is necessary install two libraries.
- Run next commands:
<br>
```pip install pyside6```
<br>
```pip install pyqtdarktheme```
<br>

#### PyInstaller
- Use PyInstaller to generate a calculator executable.
- Run the command to install PyInstaller:
<br>
```pip install pyinstaller```<br>
- Run the command to generate the requirements.txt
```pip freeze > requirements.txt```<br>
- Use the --name parameter to name the application
```pyinstaller --name="Calculator"```<br>
- Use the --noconfirm parameter to not need to confirm anything when generating the executable
```pyinstaller --name="Calculator" --noconfirm```<br>
- Use the --onefile parameter to generate a file
```pyinstaller --name="Calculator" --noconfirm --onefile```<br>
- Use the --add-data parameter to copy the image file folder
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/'```<br>
- Use the --icon parameter to indicate the icon path that the application will have
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png'` ``<br>
- Use the --noconsole parameter so the application does not open the console
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' - -noconsole```<br>
- Use the --clean parameter to clean any junk
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' - -noconsole --clean```<br>
- Use the --log-level=WARN parameter to report alerts
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' - -noconsole --clean --log-level=WARN```<br>
- At the end add the path to the main application file
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data='section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' - -noconsole --clean --log-level=WARN section7_graphic_interface/calculator/main.py```<br>

##### Indicating the folder where build, dist and spec will be generated
- Use the --distpath parameter to specify the path where the dist folder will be generated
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data='section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' - -noconsole --clean --log-level=WARN --distpath="__localcode/dist" section7_graphic_interface/calculator/main.py```<br>
- Use the --workpath parameter to specify the path where the build folder will be generated
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data='../section7_graphic_interface/calculator/files/:files/' --icon='../section7_graphic_interface/calculator/files /icon.png' --noconsole --clean --log-level=WARN --distpath="__localcode/dist" --workpath="__localcode/build" section7_graphic_interface/calculator/main.py```<br>
- Use the --specpath parameter to specify the path where the spec file will be generated. Specify the specpath path in the --add-data and --icon parameter
```pyinstaller --name="Calculator" --noconfirm --onefile --add-data='../section7_graphic_interface/calculator/files/:files/' --icon='../section7_graphic_interface/calculator/files /icon.png' --noconsole --clean --log-level=WARN --distpath="__localcode/dist" --workpath="__localcode/build" --specpath="__localcode/" section7_graphic_interface/calculator/main. py```<br>

##### Use the spec file to generate the executable
- Run the command:
```pyinstaller __localcode/Calculadora.spec```

### Portuguese
- Para inicializar a calculadora é necessário instalar duas bibliotecas.
- Rode os seguintes comandos:
<br>
```pip install pyside6```
<br>
```pip install pyqtdarktheme```
<br>

#### PyInstaller
- Use o PyInstaller para gerar um executável da calculadora.
- Execute o comando para instalar o PyInstaller:
<br>
```pip install pyinstaller```<br>
- Execute o comando para gerar o requirements.txt
```pip freeze > requirements.txt```<br>
- Use o parâmetro --name para nomear a aplicação
```pyinstaller --name="Calculadora"```<br>
- Use o parâmetro --noconfirm para não precisar confirmar nada na geração do executável
```pyinstaller --name="Calculadora" --noconfirm```<br>
- Use o parâmetro --onefile para gerar um arquivo
```pyinstaller --name="Calculadora" --noconfirm --onefile```<br>
- Use o parâmetro --add-data para copiar a pasta de arquivo de imagem 
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/'```<br>
- Use o parâmetro --icon para indicar o caminho do ícone que a aplicação terá
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png'```<br>
- Use o parâmetro --noconsole para a aplicação não abrir console
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' --noconsole```<br>
- Use o parâmetro --clean para limpar qualquer lixo
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' --noconsole --clean```<br>
- Use o parâmetro --log-level=WARN para reportar alertas
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' --noconsole --clean --log-level=WARN```<br>
- Ao final adicione o caminho para o arquivo principal da aplicação
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data='section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' --noconsole --clean --log-level=WARN section7_graphic_interface/calculator/main.py```<br>

##### Indicando a pasta onde será gerado build, dist e spec
- Use o parâmetro --distpath para especificar o caminho onde será gerado a pasta dist
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data='section7_graphic_interface/calculator/files/:files/' --icon='section7_graphic_interface/calculator/files/icon.png' --noconsole --clean --log-level=WARN --distpath="__localcode/dist" section7_graphic_interface/calculator/main.py```<br>
- Use o parâmetro --workpath para especificar o caminho onde será o gerado a pasta build
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data='../section7_graphic_interface/calculator/files/:files/' --icon='../section7_graphic_interface/calculator/files/icon.png' --noconsole --clean --log-level=WARN --distpath="__localcode/dist" --workpath="__localcode/build" section7_graphic_interface/calculator/main.py```<br>
- Use o parâmetro --specpath para especificar o caminho onde será gerado o arquivo de spec. Indique o caminho do specpath no parâmetro --add-data e --icon
```pyinstaller --name="Calculadora" --noconfirm --onefile --add-data='../section7_graphic_interface/calculator/files/:files/' --icon='../section7_graphic_interface/calculator/files/icon.png' --noconsole --clean --log-level=WARN --distpath="__localcode/dist" --workpath="__localcode/build" --specpath="__localcode/" section7_graphic_interface/calculator/main.py```<br>

##### Use o arquivo spec para gerar o executável
- Execute o comando:
```pyinstaller --distpath __localcode/dist --workpath __localcode/build __localcode/Calculadora.spec```