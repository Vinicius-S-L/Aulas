function pais() {
        var nacionalidade = document.getElementById("pais");
        var nacionalidade = nacionalidade.value;
        var pessoa = document.getElementById("pessoa");
        if (nacionalidade == "brasil") {
          pessoa.innerHTML = "É Brasileira";
        } else if (nacionalidade == "EUA") {
          pessoa.innerHTML = "É estadunidense";
        } else {
          pessoa.innerHTML = "É Chinessa";
        }
      }