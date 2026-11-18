CREATE TABLE IF NOT EXISTS plataforma (
    id_plataforma  SERIAL       PRIMARY KEY,
    nome           VARCHAR(50)  NOT NULL UNIQUE,
    fabricante     VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS cliente (
    id_cliente     SERIAL        PRIMARY KEY,
    nome           VARCHAR(100)  NOT NULL,
    telefone       VARCHAR(20),
    email          VARCHAR(120)  UNIQUE,
    data_cadastro  DATE          DEFAULT CURRENT_DATE,
    ativo          BOOLEAN       DEFAULT TRUE,
    CONSTRAINT cliente_natural_uk UNIQUE (nome, telefone)
);

CREATE TABLE IF NOT EXISTS jogo (
    id_jogo         SERIAL         PRIMARY KEY,
    titulo          VARCHAR(150)   NOT NULL UNIQUE,
    genero          VARCHAR(40),
    ano_lancamento  INTEGER        CHECK (ano_lancamento > 1970),
    preco_diaria    NUMERIC(10,2)  CHECK (preco_diaria >= 0)
);

CREATE TABLE IF NOT EXISTS endereco (
    id_endereco  SERIAL        PRIMARY KEY,
    id_cliente   INTEGER       NOT NULL UNIQUE REFERENCES cliente(id_cliente),
    logradouro   VARCHAR(150)  NOT NULL,
    numero       VARCHAR(10),
    bairro       VARCHAR(60),
    cidade       VARCHAR(60)   NOT NULL,
    uf           CHAR(2),
    cep          VARCHAR(9)
);

CREATE TABLE IF NOT EXISTS jogos_plataforma (
    id_jogo        INTEGER  NOT NULL REFERENCES jogo(id_jogo),
    id_plataforma  INTEGER  NOT NULL REFERENCES plataforma(id_plataforma),
    PRIMARY KEY (id_jogo, id_plataforma)
);

CREATE TABLE IF NOT EXISTS emprestimo (
    id_emprestimo   SERIAL   PRIMARY KEY,
    id_cliente      INTEGER  NOT NULL REFERENCES cliente(id_cliente),
    data_retirada   DATE     NOT NULL,
    data_prevista   DATE     NOT NULL CHECK (data_prevista >= data_retirada),
    data_entregue   DATE,
    multa           NUMERIC(10,2)  DEFAULT 0  CHECK (multa >= 0),
    CONSTRAINT emprestimo_natural_uk UNIQUE (id_cliente, data_retirada)
);

CREATE TABLE IF NOT EXISTS item_emprestimo (
    id_emprestimo  INTEGER        NOT NULL REFERENCES emprestimo(id_emprestimo),
    id_jogo        INTEGER        NOT NULL REFERENCES jogo(id_jogo),
    preco_pago     NUMERIC(10,2)  NOT NULL CHECK (preco_pago >= 0),
    PRIMARY KEY (id_emprestimo, id_jogo)
);


INSERT INTO plataforma (nome, fabricante) VALUES
    ('PlayStation 5',   'Sony'),
    ('Nintendo Switch', 'Nintendo'),
    ('Xbox Series X',   'Microsoft'),
    ('PC',              NULL)            -- sem fabricante único: nulo é honesto
ON CONFLICT DO NOTHING;

INSERT INTO cliente (nome, telefone, email, data_cadastro) VALUES
    ('Ana Souza',      '(51) 99931-1042', 'ana.souza@exemplo.com',   '2026-08-14'),
    ('Bruno Lima',     '(51) 98122-7765', 'bruno.lima@exemplo.com',  '2026-08-27'),
    -- sem email: a coluna aceita nulo, e é com esta linha que o IS NULL da
    -- Aula 13 tem o que encontrar
    ('Carla Menezes',  '(51) 99604-3318', NULL,                      '2026-09-02'),
    ('Diego Rocha',    '(51) 98470-2251', 'diego.rocha@exemplo.com', '2026-09-15'),
    ('Elisa Prado',    '(51) 99215-8890', 'elisa.prado@exemplo.com', '2026-09-28')
ON CONFLICT DO NOTHING;

INSERT INTO jogo (titulo, genero, ano_lancamento, preco_diaria) VALUES
    ('God of War',             'Ação',       2018, 12.00),
    ('God of War Ragnarök',    'Ação',       2022, 18.00),
    ('The Last of Us Part II', 'Aventura',   2020, 15.00),
    ('Gran Turismo 7',         'Esporte',    2022, 14.00),
    ('Tears of the Kingdom',   'Aventura',   2023, 20.00),
    ('Mario Kart 8 Deluxe',    'Corrida',    2017, 10.00),
    ('Pokémon Scarlet',        'RPG',        2022, 16.00),
    ('Halo Infinite',          'Ação',       2021, 12.00),
    ('Forza Horizon 5',        'Corrida',    2021, 14.00),
    ('Baldur''s Gate 3',       'RPG',        2023, 22.00),
    ('Elden Ring',             'RPG',        2022, 18.00),
    ('Age of Empires IV',      'Estratégia', 2021, 11.00)
ON CONFLICT DO NOTHING;

INSERT INTO endereco (id_cliente, logradouro, numero, bairro, cidade, uf, cep)
SELECT c.id_cliente, e.logradouro, e.numero, e.bairro, e.cidade, e.uf, e.cep
FROM (VALUES
    ('Ana Souza',     'Rua dos Andradas',  '1234', 'Centro Histórico', 'Porto Alegre', 'RS', '90020-008'),
    ('Bruno Lima',    'Av. Ipiranga',      '6681', 'Partenon',         'Porto Alegre', 'RS', '90619-900'),
    ('Carla Menezes', 'Rua Gonçalo de Carvalho', '98', 'Floresta',     'Porto Alegre', 'RS', '90035-170')
) AS e(cliente, logradouro, numero, bairro, cidade, uf, cep)
JOIN cliente c ON c.nome = e.cliente
ON CONFLICT DO NOTHING;

INSERT INTO jogos_plataforma (id_jogo, id_plataforma)
SELECT j.id_jogo, p.id_plataforma
FROM (VALUES
    ('God of War',             'PlayStation 5'),
    ('God of War',             'PC'),
    ('God of War Ragnarök',    'PlayStation 5'),
    ('God of War Ragnarök',    'PC'),
    ('The Last of Us Part II', 'PlayStation 5'),
    ('Gran Turismo 7',         'PlayStation 5'),
    ('Tears of the Kingdom',   'Nintendo Switch'),
    ('Mario Kart 8 Deluxe',    'Nintendo Switch'),
    ('Pokémon Scarlet',        'Nintendo Switch'),
    ('Halo Infinite',          'Xbox Series X'),
    ('Halo Infinite',          'PC'),
    ('Forza Horizon 5',        'Xbox Series X'),
    ('Forza Horizon 5',        'PC'),
    ('Baldur''s Gate 3',       'PC'),
    ('Elden Ring',             'PC'),
    ('Elden Ring',             'PlayStation 5'),
    ('Elden Ring',             'Xbox Series X'),
    ('Age of Empires IV',      'PC')
) AS v(jogo, plataforma)
JOIN jogo       j ON j.titulo = v.jogo
JOIN plataforma p ON p.nome   = v.plataforma
ON CONFLICT DO NOTHING;

INSERT INTO emprestimo (id_cliente, data_retirada, data_prevista, data_entregue, multa)
SELECT c.id_cliente, e.retirada, e.prevista, e.entregue, e.multa
FROM (VALUES
    ('Ana Souza',     DATE '2026-10-05', DATE '2026-10-08', DATE '2026-10-07', 0.00),
    ('Ana Souza',     DATE '2026-10-09', DATE '2026-10-12', DATE '2026-10-12', 0.00),
    ('Ana Souza',     DATE '2026-10-20', DATE '2026-10-24', NULL,              0.00),
    -- devolvido DOIS dias depois do previsto: é a linha que dá multa, e é com
    -- ela que a conta "data_entregue > data_prevista" tem o que encontrar
    ('Bruno Lima',    DATE '2026-10-06', DATE '2026-10-09', DATE '2026-10-11', 9.00),
    ('Bruno Lima',    DATE '2026-10-19', DATE '2026-10-23', NULL,              0.00),
    ('Carla Menezes', DATE '2026-10-14', DATE '2026-10-17', DATE '2026-10-16', 0.00),
    ('Carla Menezes', DATE '2026-10-22', DATE '2026-10-26', NULL,              0.00)
) AS e(cliente, retirada, prevista, entregue, multa)
JOIN cliente c ON c.nome = e.cliente
ON CONFLICT DO NOTHING;

INSERT INTO item_emprestimo (id_emprestimo, id_jogo, preco_pago)
SELECT e.id_emprestimo, j.id_jogo, v.preco
FROM (VALUES
    ('Ana Souza',     DATE '2026-10-05', 'God of War',             12.00),
    ('Ana Souza',     DATE '2026-10-05', 'Mario Kart 8 Deluxe',     8.00),
    ('Ana Souza',     DATE '2026-10-09', 'Pokémon Scarlet',        16.00),
    ('Ana Souza',     DATE '2026-10-20', 'Elden Ring',             18.00),
    ('Bruno Lima',    DATE '2026-10-06', 'The Last of Us Part II', 15.00),
    ('Bruno Lima',    DATE '2026-10-19', 'Baldur''s Gate 3',       22.00),
    ('Bruno Lima',    DATE '2026-10-19', 'Elden Ring',             18.00),
    ('Carla Menezes', DATE '2026-10-14', 'Tears of the Kingdom',   20.00),
    ('Carla Menezes', DATE '2026-10-22', 'God of War Ragnarök',    18.00)
) AS v(cliente, retirada, jogo, preco)
JOIN cliente    c ON c.nome = v.cliente
JOIN emprestimo e ON e.id_cliente = c.id_cliente AND e.data_retirada = v.retirada
JOIN jogo       j ON j.titulo = v.jogo
ON CONFLICT DO NOTHING;

SELECT 'plataforma'       AS tabela, COUNT(*) AS linhas FROM plataforma
UNION ALL SELECT 'cliente',          COUNT(*) FROM cliente
UNION ALL SELECT 'jogo',             COUNT(*) FROM jogo
UNION ALL SELECT 'endereco',         COUNT(*) FROM endereco
UNION ALL SELECT 'jogos_plataforma', COUNT(*) FROM jogos_plataforma
UNION ALL SELECT 'emprestimo',       COUNT(*) FROM emprestimo
UNION ALL SELECT 'item_emprestimo',  COUNT(*) FROM item_emprestimo;
