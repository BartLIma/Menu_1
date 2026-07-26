<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Links com Tooltips</title>
  <style>
    /* Estilo básico dos links */
    a {
      position: relative;
      text-decoration: none;
      color: darkblue;
      margin: 20px;
      font-size: 16px;
      cursor: pointer;
    }

    /* Caixa de tooltip */
    a .tooltip {
      visibility: hidden;
      opacity: 0;
      width: 300px;
      background-color: #333;
      color: #fff;
      text-align: left;
      border-radius: 6px;
      padding: 10px;
      position: absolute;
      z-index: 1;
      bottom: 125%; /* posição acima do link */
      left: 50%;
      margin-left: -150px;
      transition: opacity 0.3s;
      font-size: 14px;
    }

    /* Setinha do tooltip */
    a .tooltip::after {
      content: "";
      position: absolute;
      top: 100%;
      left: 50%;
      margin-left: -5px;
      border-width: 5px;
      border-style: solid;
      border-color: #333 transparent transparent transparent;
    }

    /* Mostrar tooltip ao passar o mouse */
    a:hover .tooltip {
      visibility: visible;
      opacity: 1;
    }
  </style>
</head>
<body>

  <a href="#">
    Secretaria de Saúde
    <span class="tooltip">
      Possibilita consultar endereço da secretaria de saúde, o CNPJ do fundo de saúde e dados de contato do gestor local.
    </span>
  </a>

  <a href="#">
    Transferências Financeiras
    <span class="tooltip">
      Permite acessar informações de transferências financeiras (convênios e contratos de repasses), dados baixados do Painel de Transferências Discricionárias, e visualizar o andamento do monitoramento do instrumento.
    </span>
  </a>

  <a href="#">
    Cadastro Renem
    <span class="tooltip">
      Possibilita consulta ao cadastro de equipamentos previstos na lista Renem. Segundo o FNS, a Especificação Sugerida é uma orientação técnica oferecida pelo Ministério da Saúde, com o objetivo de auxiliar na formulação de propostas de investimento.
    </span>
  </a>

  <a href="#">
    Valor Sugerido
    <span class="tooltip">
      O Valor Sugerido representa o valor de referência para o financiamento de um item, desde que este atenda à Especificação Sugerida. É importante ressaltar que as especificações e os valores sugeridos são obrigatórios apenas para os itens de Informática e as Unidades Móveis, não abrangendo os demais equipamentos.
    </span>
  </a>

</body>
</html>
