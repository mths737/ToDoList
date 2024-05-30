// função range para fazer uma iteração
function range(size, startAt = 0) {
    return [...Array(size).keys()].map(i => i + startAt);
}

function selecionado(id, tela) {
    // pega o input escondido do formulário dos botões e atribui o id da task selecionada no valor do input
    let selecionado = document.getElementById('selecionado');
    selecionado.value = id;

    // atribui todas as task exibidas na tela
    let itens = document.getElementsByTagName('li')

    // se o item ja estiver selecionado
    if (document.getElementById(id).style.backgroundColor == "gray") {
        // Reseta o backgroundColor de todas as tasks
        for (i in range(itens.length)) {
            itens[i].style.backgroundColor = "";
        }

        // Habilita e desabilita botões no display

        if (tela == 'tasksList') {
            document.getElementById('concluido').style.display = 'none';
            document.getElementById('excluir').style.display = 'none';
            document.getElementById('novo').style.display = '';
        } else if (tela == 'tasksCompleted') {
            document.getElementById('excluir').style.display = 'none';
            document.getElementById('voltar').style.display = '';
        }
    }else {
        // Reseta o backgroundColor de todas as tasks
        for (i in range(itens.length)) {
            itens[i].style.backgroundColor = "";
        }

        // Habilita e desabilita botões no display e seleciona a task
        document.getElementById(id).style.backgroundColor = "gray";

        if (tela == 'tasksList') {
            document.getElementById('concluido').style.display = '';
            document.getElementById('excluir').style.display = '';
            document.getElementById('novo').style.display = 'none';
        } else if (tela == 'tasksCompleted') {
            document.getElementById('excluir').style.display = '';
            document.getElementById('voltar').style.display = 'none';
        }
    }
}
