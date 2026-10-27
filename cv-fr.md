# Résumé

<!-- v:backend -->
Ingénieur logiciel et physicien spécialisé en développement backend Python, systèmes distribués et optimisation. Expérience en production avec FastAPI, MySQL, RabbitMQ et Docker, et en modélisation mathématique et optimisation discrète.
<!-- /v -->

<!-- v:or -->
Ingénieur logiciel et physicien, spécialisé en modélisation mathématique et optimisation discrète. Je conçois des outils d'aide à la décision — ordonnancement, planification de production — en Python et MiniZinc, et je les mène jusqu'en production : services backend FastAPI, APIs REST, RabbitMQ, MySQL, Docker.
<!-- /v -->

<!-- v:fintech -->
Ingénieur backend spécialisé en systèmes financiers. Sur une plateforme bancaire, j'ai reconstruit une intégration FIX 4.2 en production (56 paires de devises) et unifié le contrôle d'accès — sessions, permissions, 2FA.
<!-- /v -->

# Expérience

## Margaux Systems — Fondateur, Recherche Opérationnelle
*Mar 2026 – Présent*

- R&D indépendante en recherche opérationnelle : modélisation d'ordonnancement et de planification de production en Python et MiniZinc, documentée par des études de cas publiées ; prospection directe auprès d'industriels.

## SNAPP' — Ingénieur Backend Python (Contractuel)
*Fév. 2025 – Mar. 2026*

- Repris un flux de change au comptant (FIX 4.2 sur WebSocket, 56 paires) dont ni l'intégration existante ni la réécriture d'un prestataire n'étaient exploitables, et reconstruit à partir de la spécification : codec, cycle de vie des sessions, reconnexion avec réabonnement, normalisation des prix. Architecture asynchrone mono-thread, pour que l'ordre des messages reste déterministe ; le flux se rétablit seul après une coupure.
- Fusionné le contrôle d'accès d'une API bancaire en une dépendance unique : validation de session, permissions (scopes JWT et autorisations en base), périmètre de comptes, identité, 2FA et sessions en lecture seule — à partir du code « action:domaine:privilège » déclaré par chaque route. Ajouter une route devient une déclaration, pas un cas particulier. <!-- v:backend,fintech -->
- Développé plus de 200 endpoints REST (FastAPI, SQLAlchemy, Pydantic) et les services RabbitMQ/RPC vers les systèmes bancaires, sur trois bases MySQL avec migrations Alembic et suite de tests pytest.
- Implémenté les endpoints et le transport des données de positions et transactions titres (Swissquote, Moventum) et des taux BCE : ORM, migrations, REST et RabbitMQ vers la plateforme de l'établissement. <!-- v:fintech -->
- Développé le moteur de traitement des demandes : workflows typés, audit, documents et messagerie interne. <!-- v:backend -->

## SIAL — Technicien de Laboratoire
*Mar 2024 – Mar 2025*

- Analyses en laboratoire, gestion des données expérimentales et de la logistique. <!-- v:backend,or -->

## Développeur Indépendant
*Juil. 2019 – Mar. 2024*

- Applications web puis outils logiciels, en autodidacte ; plusieurs figurent dans les projets sélectionnés.

## RENYT Tech — Développeur Frontend
*Mar 2022 – Oct 2022*

- Applications web en React, Next.js et TypeScript.

<!-- v:or -->
## Universidad de los Andes — Assistant de Recherche, Dynamique Non Linéaire
*Mai 2017 – Juil. 2018 · Mérida, Venezuela*

- Analyse de données expérimentales et méthodes statistiques sur des systèmes dynamiques non linéaires ; revues de littérature et rédaction d'articles.
<!-- /v -->

# Formation

## Universidad de los Andes — B.Sc. Physique (cum laude)
*Mérida, Venezuela — 2018*

Formation en modélisation mathématique et méthodes computationnelles ; passage vers l'ingénierie logicielle via plus de 70 cours en autodidacte : algorithmique, architecture, compilateurs, optimisation discrète et machine learning.

**Assistant de recherche — Groupe Dynamique Non Linéaire** (2017–2018) : analyse de données et publications. <!-- v:backend,fintech -->

# Compétences

**Langages :** Python, SQL, JavaScript/TypeScript, C++

**Backend :** FastAPI, Python asynchrone, APIs REST, RabbitMQ, SQLAlchemy, Alembic

**Bases de données & infrastructure :** MySQL, Docker, Git, Linux

**Optimisation :** MiniZinc, optimisation discrète, modélisation mathématique, algorithmes

**Langues :** Français (courant), Anglais (bilingue), Espagnol (langue maternelle)

**Autorisation de travail :** France — droit de travailler sans démarche de l'employeur

# Projets Sélectionnés

[**Starisk**](https://starisk.matiasagelvis.com) — Notes de cours recalculées à partir des avis les mieux votés : crawler et scoring Python sans dépendances, pondération par racine du nombre de votes, calibrée contre un classement humain (ρ = 0,70 contre 0,42). 426 cours, site Astro.

[**Significado Total**](https://semioteca.vercel.app) — Archive sémiotique de 2 709 fiches : pipeline d'extraction (ODT → DOCX → texte, frontières de fiches, notes), étiquetage automatique par NLI zero-shot et embeddings multilingues, site SvelteKit avec recherche plein texte.
