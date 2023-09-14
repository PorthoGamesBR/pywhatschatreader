# PyWhatsChatReader

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

> Funções para separar as mensagens e os dados em arquivos de conversas de whatsapp

### Ajustes e melhorias

Nada para adicionar por enquanto.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Tem `Python` 3.10.5 ou superior instalado

## 🚀 Instalando PyWhatsChatReader

Para instalar o PyWhatsChatReader, siga estas etapas:


- Faça um clone do projeto, ou baixe os arquivos diretamente desse repositório e os salve em uma pasta: [Guia para download](https://docs.github.com/pt/repositories/working-with-files/using-files/downloading-source-code-archives)


## ☕ Usando PyWhatsChatReader

Para usar PyWhatsChatReader, siga estas etapas:

- Importe o módulo para seu arquivo Python
    ```from <folder_name> import whtReader```
    ou
    ```from <folder_name>.whtReader import open_conversa,read_all_messages,list_of_messages```
- Caso já tenha uma conversa baixada, ignore esse passo: Baixe uma conversa do whatsapp seguindo o seguinte [tutorial](https://faq.whatsapp.com/1180414079177245/?cms_platform=android)
- Guarde a localização do arquivo em uma variável
    ```filepath = "...\...\Grupo da Familia.txt"```
- Siga os seguintes passos para gerar o objeto/dict
    ````
        def main():
            mensagens = ""
            with open_conversa(filepath):
                msgs_bruto = read_all_messsages(conversa)
                mensagens = list_of_mensagens(msgs_bruto)
    ```
- Os dados estarão na variável ```mensagens```, com os dados de data,hora,nome de usuário e texto de cada mensagem separado

Exemplo:
    Considere uma conversa que eu comecei com um amigo chamado Guilherme (nome salvo na lista de contatos), e ele me mandou a seguinte mensagem:
    "Essa mensagem vai ser processada pelo PywhatsChatReader"
    Se eu então usasse o método anterior na nossa conversa, poderia acessar essa mensagem do seguinte modo
    ```
    print(mensagens[0]['date-hour'])
    print(mensagens[0]['username'])
    print(mensagens[0]['text'])

    {'d':'09/01/2023','h':'19:43'}
    Guilherme
    Essa mensagem vai ser processada pelo PywhatsChatReader
    ```


## 📫 Contribuindo para PyWhatsChatReader

Para contribuir com PyWhatsChatReader, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b bugfix/formato-diferente-mensagem`.
3. Faça suas alterações e confirme-as: `git commit -m 'Adicionando checagem de formato de mensagem'`
4. Envie para o branch original: `git push origin PyWhatsChatReader / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars3.githubusercontent.com/u/31936044" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Iuri Silva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 😄 Seja um dos contribuidores

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.
(Ainda não tenho um arquivo CONTIBUTING.md. Já seria uma contribuição criar um)

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.