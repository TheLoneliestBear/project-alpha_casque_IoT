DROP TABLE IF EXISTS [iterations];
DROP TABLE IF EXISTS [seances];
-- --------------------------------------------------------

--
-- Structure de la table Joueurs
--

CREATE TABLE [iterations] (
  [id] INTEGER NOT NULL,
  [idSeance] INTEGER NOT NULL,
  [distance] REAL,
  [lumiere] REAL,
  [indiceDanger] INTEGER,
  [date] timestamp NOT NULL,
  CONSTRAINT [PK_Iterations] PRIMARY KEY ([id]),
  FOREIGN KEY ([idSeance]) REFERENCES [Seances] ([id])
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- --------------------------------------------------------

--
-- Structure de la table Parties
--

CREATE TABLE [seances] (
  [id] INTEGER NOT NULL UNIQUE,
  [date] timestamp NOT NULL,
  CONSTRAINT [PK_Seances] PRIMARY KEY ([id])
);

-- --------------------------------------------------------

--
-- Index pour les clés étrangères
--
