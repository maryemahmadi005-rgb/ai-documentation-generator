-- =====================================================================
-- SCHEMA DE BASE DE DONNEES
-- Projet : backend2 (analyseur de dépôts Git / générateur de documentation)
-- Moteur cible : MySQL 8.x / MariaDB 10.6+ (InnoDB, utf8mb4)
-- Généré à partir de l'analyse du code réel : models.py, app.py, pipeline.py,
-- utils/db_helpers.py
--
-- IMPORTANT : aucune table, colonne ou fonctionnalité n'a été inventée.
-- Ce script correspond EXACTEMENT aux deux modèles SQLAlchemy existants :
--   - Utilisateurs
--   - Historique
-- Voir le rapport (rapport_conception_bdd.md) pour le détail des choix
-- et les écarts/manques détectés dans le code.
-- =====================================================================

-- ---------------------------------------------------------------------
-- 1. CREATION DE LA BASE
-- ---------------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS backend2_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE backend2_db;

-- ---------------------------------------------------------------------
-- 2. TABLE : utilisateurs
-- Correspond au modèle SQLAlchemy `Utilisateurs` (models.py, lignes 10-23)
-- ---------------------------------------------------------------------
CREATE TABLE utilisateurs (
    id                  INT AUTO_INCREMENT PRIMARY KEY,
    nom                 VARCHAR(100)    NOT NULL,
    email               VARCHAR(100)    NOT NULL,
    mot_de_passe        VARCHAR(255)    NOT NULL,
    theme_preference    VARCHAR(20)     NOT NULL DEFAULT 'dark',
    date_inscription    DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uq_utilisateurs_email UNIQUE (email),
    CONSTRAINT chk_utilisateurs_theme
        CHECK (theme_preference IN ('light', 'dark'))
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- 3. TABLE : historique
-- Correspond au modèle SQLAlchemy `Historique` (models.py, lignes 26-89)
-- Une "analyse" de dépôt = une ligne de cette table.
-- ---------------------------------------------------------------------
CREATE TABLE historique (
    id                          INT AUTO_INCREMENT PRIMARY KEY,
    utilisateurs_id             INT             NOT NULL,

    -- Informations saisies à la création de l'analyse (route /analyser)
    url                         VARCHAR(500)    NOT NULL,
    statut                      VARCHAR(20)     NOT NULL DEFAULT 'en_cours',

    -- Informations du dépôt (remplies par pipeline.py::executer_analyse
    -- via le scanner du dépôt cloné)
    repo_name                   VARCHAR(200),
    author                      VARCHAR(200),
    branch                      VARCHAR(100),
    commits                     INT             NOT NULL DEFAULT 0,
    stars                       INT             NOT NULL DEFAULT 0,
    description                 TEXT,
    licence                     VARCHAR(100),
    langages                    TEXT,               -- liste JSON sérialisée (json.dumps)
    fichiers_count               INT             NOT NULL DEFAULT 0,

    -- Résultat de la détection d'architecture (architecture/*)
    architecture                VARCHAR(100),
    confiance_architecture       VARCHAR(20),        -- ex: "85%"

    -- Résultats de génération de documentation (generation/*)
    resume_ia                   TEXT,
    documentation_preview        TEXT,
    chemin_doc                  VARCHAR(500),        -- chemin disque du dossier documenté
    chemin_site_html             VARCHAR(500),        -- chemin disque du site mkdocs généré

    -- Arborescence du dépôt scanné, sérialisée en JSON
    tree_json                   LONGTEXT,

    -- Suivi utilisateur / erreurs
    consulte                    TINYINT(1)      NOT NULL DEFAULT 0,
    date_analyse                 DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    message_erreur               TEXT,

    CONSTRAINT fk_historique_utilisateur
        FOREIGN KEY (utilisateurs_id) REFERENCES utilisateurs(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT chk_historique_statut
        CHECK (statut IN ('en_cours', 'termine', 'erreur'))
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- 4. INDEX
-- Reprend exactement les index déclarés dans __table_args__ de Historique
-- (models.py, lignes 28-31), plus un index utile pour le tri par défaut
-- utilisé dans app.py::dashboard (order_by date_analyse DESC).
-- ---------------------------------------------------------------------
CREATE INDEX idx_historique_utilisateur ON historique (utilisateurs_id);
CREATE INDEX idx_historique_statut       ON historique (statut);
CREATE INDEX idx_historique_date_analyse ON historique (date_analyse);

-- =====================================================================
-- FIN DU SCRIPT
-- =====================================================================