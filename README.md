# Tibia Rune and Arrow Maker - Python 3.7+
Tibia bot for rune and diamond arrows makers . Made with python <3

_Disclaim:
Work only on win10 with python 3.7+_


## Requirements:

1. Create an .env file based on .env.example.
2. Set your tibia %appdata% package path on .env file. ex: C:\Users\%user%\AppData\Local\Tibia\
3. Run 'pip install -r requirements.txt' to install all packages needed.
4. Finally, run 'python main.py' and voilá.

_Now, if you dont know portuguese, "do your jumps" cuz im not in moody to translate this last part_

## O script tenta identificar as hotkeys nos atalhos da action bar. Food, blank rune, strong mana potion, hotkey de magia, essas hotkeys tem que estar lá!!!

1. O bot utiliza o modo software no 'graphic settings', dessa forma ele burla a tela preta do jogo. Mas fica tranquilo que ele muda isso sozinho ao abrir o jogo por ele. Caso você queira fazer isso na mão, vai ter que abrir o jogo, configurar o graphic settings, fechar o jogo e abrir novamente (Eu costumo sempre abrir o jogo direto pelo script já que ele loga pra mim automaticamente)
2. O open cv tenta identificar imagens semelhantes, então pode ocorrer alguns falsos positivos (como no caso de rings). Um dia eu pego pra arrumar isso, mas não é minha prioridade! Mantenha o jogo aberto sempre no monitor principal (caso você utilize mais de um monitor), senão não vai funcionar
3. Todos os prints contidos na pasta ./images são os utilizados para reconhecer as imagens na tela. Eu testei com um druid pra runar avalanche (então lá tem um print de avalanche) e com um paladin pra fazer diamond arrow. A resolução do meu monitor é 1920x1080, pode ser que não funcione pra voce, ok? Mas Sr. Digonalha, qual a solução nesse caso então? Abre o jogo no modo software do graphic settings, e tira print das suas htks na action bar (isso mesmo, de tudo que você for usar), e salva nos respectivos locais na pasta ./images
4. Por enquanto só ta fazendo avalanche, se quiser fazer great fire ball só trocar a imagem htkrune.png lá na pasta ./images/ para a imagem da hotkey da gfb, por exemplo.


### Só respondo issues se for de bug. Não me venha pedindo ajuda com coisa boba, ok? Tu ta no github, o código fonte ta todo ai pra tu estudar (e ainda ta todo em python, qualquer criança entende). Ah, eu valorizo muito o esforço e aceito pull requests.

## SÓ LEMBRANDO QUE EU NÃO ME RESPONSABILIZO POR EVENTUAIS PERDAS. USA ISSO POR SUA CONTA E RISCO. COMO DIRIA OMAR LITTLE, "ALL IN THE GAME, YO"
