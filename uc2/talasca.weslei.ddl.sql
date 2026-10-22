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
CREATE TABLE IF NOT EXISTS tipo_doce (
    id_tipo SERIAL PRIMARY KEY,
    sabor VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS item_pedido (
    total_pago NUMERIC(10,2) NOT NULL,
    troco NUMERIC(10,2)
);
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

