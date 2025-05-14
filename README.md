# Calculadora-IMC

:root {
    --cor-fundo: #f4f4f4;
    --cor-texto: #333;
    --cor-header: #007bff;
    --cor-header-texto: #fff;
    --cor-botao: #28a745;
    --cor-botao-hover: #1e7e34;
    --cor-bordo: #ccc;
    --cor-background: #e9ecef;
    --cor-erro-fundo: #f8d7da;
    --cor-erro-texto: #721c24;
    --cor-erro-bordo: #f5c6cb;
    --cor-footer-texto: #777;
    }
    
    {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    }

    body {
    font-family: Arial, sans-serif;
    background-color: var(--cor-fundo);
    color: var(--cor-texto);
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    }
    
    header {
    background-color: var(--cor-header);
    color: var(--cor-header-texto);
    text-align: center;
    padding: 1rem;
    font-size: 1.5rem;
    font-weight: bold;
    }
    
    main {
    background-color: #fff;
    width: 100%;
    max-width: 400px;
    margin: 2rem auto;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .form-group {
    margin-bottom: 1rem;
    }
    
    label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    }
    
    input[type="number"],
    select {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid var(--cor-bordo);
    border-radius: 4px;
    background-color: var(--cor-background);
    font-size: 1rem;
    }
    
    button {
    width: 100%;
    background-color: var(--cor-botao);
    color: #fff;
    padding: 0.75rem;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
    }
    button:hover {
    background-color: var(--cor-botao-hover);
    }
    

    #resultado {
    margin-top: 1rem;
    padding: 0.75rem;
    background-color: var(--cor-background);
    border-radius: 4px;
    text-align: center;
    font-weight: bold;
    }
    

    #erro-mensagem {
    margin-top: 1rem;
    padding: 0.75rem;
    background-color: var(--cor-erro-fundo);
    color: var(--cor-erro-texto);
    border: 1px solid var(--cor-erro-bordo);
    border-radius: 4px;
    text-align: center;
    }
    

    footer {
    margin-top: auto;
    padding: 1rem 0;
    text-align: center;
    color: var(--cor-footer-texto);
    font-size: 0.9rem;
    }
    

    @media (max-width: 37.5rem) {
    main {
    margin: 1rem;
    padding: 1rem;
    }
    }


--------------------------------------------------------------------------------------------------------


document.addEventListener('DOMContentLoaded', () => {
  const converterBtn = document.getElementById('converter-btn');
  const valorInput   = document.getElementById('valor');
  const deSelect     = document.getElementById('moeda-de');
  const paraSelect   = document.getElementById('moeda-para');
  const resultadoDiv = document.getElementById('resultado');
  const erroDiv      = document.getElementById('erro-mensagem');
  

  const taxasDeCambio = {
    'BRL-USD': 0.19,
    'BRL-EUR': 0.18,
    'USD-BRL': 5.26,
    'USD-EUR': 0.92,
    'EUR-BRL': 5.74,
    'EUR-USD': 1.09
  };
  
  converterBtn.addEventListener('click', () => {

    resultadoDiv.textContent = '';
    erroDiv.textContent      = '';


    const valor = parseFloat(valorInput.value);
    const de    = deSelect.value;
    const para = paraSelect.value;


    if (isNaN(valor)) {
      erroDiv.textContent = 'Por favor, digite um valor numérico válido.';
      return;
    }


    if (de === para) {
      erroDiv.textContent = 'Selecione moedas de origem e destino diferentes.';
      return;
    }


    const chave = `${de}-${para}`;
    const taxa  = taxasDeCambio[chave];
    if (!taxa) {
      erroDiv.textContent = 'Conversão não disponível para estas moedas.';
      return;
    }


    const convertido = (valor * taxa).toFixed(2);
    resultadoDiv.textContent =
      `${valor.toFixed(2)} ${de} = ${convertido} ${para}`;
  }); 

}); 
