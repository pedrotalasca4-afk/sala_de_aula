CREATE TABLE IF NOT EXISTS cliente (
	id_cliente SERIAL PRIMARY KEY,
	nome VARCHAR(80) NOT NULL,
	logradouro VARCHAR(40) NOT NULL,
	numero INTEGER NOT NULL,
	bairro VARCHAR(50) NOT NULL,
	cidade VARCHAR(50) NOT NULL,
	cep INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS cliente_telefone (
    id_telefone SERIAL PRIMARY KEY,
    numero INTEGER NOT NULL
);
ALTER TABLE cliente_telefone
    ADD COLUMN id_cliente INTEGER,
    ADD CONSTRAINT fk_id_cliente
        FOREIGN KEY(id_cliente)
        REFERENCES cliente(id_cliente);

CREATE TABLE IF NOT EXISTS pedido (
    id_pedido SERIAL PRIMARY KEY,
    data_feita DATE NOT NULL,
    data_prevista DATE NOT NULL,
    data_entregue DATE
);

CREATE TABLE IF NOT EXISTS doce (
    id_doce SERIAL PRIMARY KEY,
    preco NUMERIC(10,2) NOT NULL
);

ALTER TABLE doce
    ADD COLUMN id_tipo INTEGER,
    ADD CONSTRAINT fk_id_tipo
        FOREIGN KEY(id_tipo)
        REFERENCES tipo_doce(id_tipo);

CREATE TABLE IF NOT EXISTS tipo_doce (
    id_tipo SERIAL PRIMARY KEY,
    sabor VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS item_pedido (
    total_pago NUMERIC(10,2) NOT NULL,
    troco NUMERIC(10,2)
);

ALTER TABLE item_pedido
    ADD COLUMN id_pedido INTEGER,
    ADD CONSTRAINT fk_id_pedido
        FOREIGN KEY(id_pedido)
        REFERENCES pedido(id_pedido);

ALTER TABLE item_pedido
    ADD COLUMN id_doce INTEGER,
    ADD CONSTRAINT fk_id_doce
        FOREIGN KEY(id_doce)
        REFERENCES doce(id_doce);

CREATE TABLE IF NOT EXISTS solicitacao (

);
ALTER TABLE solicitacao
    ADD COLUMN id_cliente INTEGER,
    ADD COLUMN id_pedido INTEGER;

ALTER TABLE solicitacao
    ADD CONSTRAINT fk_id_cliente
        FOREIGN KEY(id_cliente)
        REFERENCES cliente(id_cliente);

ALTER TABLE solicitacao
    ADD CONSTRAINT fk_id_pedido
        FOREIGN KEY(id_pedido)
        REFERENCES pedido(id_pedido);

