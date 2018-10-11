--
-- File generated with SQLiteStudio v3.2.1 on qua set 26 23:52:48 2018
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: core_exercicio
DROP TABLE IF EXISTS core_exercicio;
CREATE TABLE "core_exercicio" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(100) NOT NULL, "musculo_id" integer NOT NULL REFERENCES "core_musculo" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (1, 'Supino reto', 1);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (2, 'Elevação lateral', 2);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (3, 'Caminhada', 3);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (4, 'Supinio inclinado com barra', 1);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (5, 'Cruxifixo reto', 1);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (6, 'Supino reto com barra', 1);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (7, 'Voador', 1);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (8, 'Françes deitado com halteres', 5);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (9, 'Corda cross', 5);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (10, 'Barra Cross', 5);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (11, 'Triceps testa', 5);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (12, 'Levantamento terra', 6);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (13, 'Pulley frontal', 6);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (14, 'Pulley atraz', 6);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (15, 'Remada baixa', 6);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (16, 'Serrote', 6);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (17, 'Rosca alternada com banco inclinado', 8);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (18, 'Rosca scott barra W', 8);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (19, 'Rosca direta barra reta', 8);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (20, 'Martelo em pé', 8);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (21, 'Rosca punho', 7);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (22, 'Leg press 45°', 9);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (23, 'Extensor de pernas', 9);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (24, 'Flexora sentada', 9);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (25, 'Adutora', 9);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (26, 'Abdutora', 9);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (27, 'Stiff', 9);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (28, 'Desenvolvimento nuca com barra', 2);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (29, 'Desenvolvimento maquina', 2);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (30, 'Elevação frontal com halteres em pé', 2);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (31, 'Elevação lateral com halteres sentado', 2);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (32, 'Encolhimento com halteres', 10);
INSERT INTO core_exercicio (id, nome, musculo_id) VALUES (33, 'Encolhimento com barra', 10);

-- Table: core_musculo
DROP TABLE IF EXISTS core_musculo;
CREATE TABLE "core_musculo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(50) NOT NULL, "descricao" varchar(100) NULL);
INSERT INTO core_musculo (id, nome, descricao) VALUES (1, 'Peitoral', 'Peitoral ...');
INSERT INTO core_musculo (id, nome, descricao) VALUES (2, 'Ombro', 'Onbros Dentroid');
INSERT INTO core_musculo (id, nome, descricao) VALUES (3, 'Corpo Todo', 'Corpo completo');
INSERT INTO core_musculo (id, nome, descricao) VALUES (5, 'Triceps', 'Musculo superior do braço');
INSERT INTO core_musculo (id, nome, descricao) VALUES (6, 'Costas', NULL);
INSERT INTO core_musculo (id, nome, descricao) VALUES (7, 'Antebraço', NULL);
INSERT INTO core_musculo (id, nome, descricao) VALUES (8, 'Biseps', NULL);
INSERT INTO core_musculo (id, nome, descricao) VALUES (9, 'Pernas', NULL);
INSERT INTO core_musculo (id, nome, descricao) VALUES (10, 'Trapézio', 'Musculo entre o pescoço e ombros');

-- Index: core_exercicio_musculo_id_81f00a80
DROP INDEX IF EXISTS core_exercicio_musculo_id_81f00a80;
CREATE INDEX "core_exercicio_musculo_id_81f00a80" ON "core_exercicio" ("musculo_id");

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
