# Résumé

<!-- v:backend -->
Ingénieur logiciel et physicien spécialisé en développement backend Python, systèmes distribués et optimisation. Expérience en production avec FastAPI, MySQL, RabbitMQ et Docker, et en modélisation mathématique et optimisation discrète.
<!-- /v -->

<!-- v:or -->
Ingénieur logiciel et physicien, spécialisé en modélisation mathématique et optimisation discrète. Je conçois des outils d'aide à la décision — ordonnancement, planification de production — en Python et MiniZinc, et je les mène jusqu'en production : services backend FastAPI, APIs REST, RabbitMQ, MySQL, Docker.
<!-- /v -->

# Expérience

## Margaux Systems — Fondateur, Recherche Opérationnelle
*Mar 2026 – Présent*

- R&D indépendante en recherche opérationnelle : modélisation d'ordonnancement et de planification de production en Python et MiniZinc, documentée par des études de cas publiées ; prospection directe auprès d'industriels.

## SNAPP' — Ingénieur Backend Python (Contractuel)
*Fév. 2025 – Mar. 2026*

- Unifié le contrôle d'accès d'une API bancaire dans une dépendance unique : session, scopes JWT et autorisations en base, à partir du code « action:domaine:privilège » déclaré par chaque route — ajouter une route devient une déclaration, pas un cas particulier. Étendu avec l'impersonation, la 2FA TOTP, le blocage de compte et l'audit des tentatives échouées. <!-- v:backend,fintech -->
- Repris un flux de change au comptant (FIX 4.2 sur WebSocket, 56 paires) dont ni l'intégration existante ni la réécriture d'un prestataire n'étaient exploitables, et reconstruit à partir de la spécification : codec, cycle de vie des sessions, reconnexion avec réabonnement, normalisation des prix. Architecture asynchrone mono-thread, pour que l'ordre des messages reste déterministe ; le flux se rétablit seul après une coupure.
- Conception d'APIs REST asynchrones FastAPI et de middlewares d'authentification, services communiquant via RabbitMQ RPC, sur trois bases MySQL (SQLAlchemy, Alembic) avec suite de tests pytest.
- Co-conception du moteur de traitement des demandes : workflows typés, audit, documents et messagerie interne.

## SIAL — Technicien de Laboratoire
*Mar 2024 – Mar 2025*

- Analyses en laboratoire, gestion des données expérimentales et de la logistique.

## Développeur Logiciel Indépendant
*Oct 2022 – Mar 2024*

- Applications web et outils logiciels conçus et déployés en autodidacte ; plusieurs figurent dans les projets sélectionnés.

## Développeur Frontend — Remote
*Mar 2022 – Oct 2022*

- Développement de fonctionnalités d'application web avec React, Next.js, TypeScript et Chakra UI.

# Formation

## Universidad de los Andes — B.Sc. Physique (cum laude)
*Mérida, Venezuela — 2018*

Formation en modélisation mathématique et méthodes computationnelles ; passage vers l'ingénierie logicielle via plus de 70 cours en autodidacte : algorithmique, architecture, compilateurs, optimisation discrète et machine learning.

# Compétences

**Langages :** Python, SQL, JavaScript/TypeScript, C++

**Backend :** FastAPI, Python asynchrone, APIs REST, RabbitMQ, SQLAlchemy, Alembic

**Bases de données & infrastructure :** MySQL, Docker, Git, Linux

**Optimisation :** MiniZinc, optimisation discrète, modélisation mathématique, algorithmes

**Langues :** Français (courant), Anglais (bilingue), Espagnol (langue maternelle)

**Autorisation de travail :** France — droit de travailler sans démarche de l'employeur

# Projets Sélectionnés

[**Starisk**](https://starisk.matiasagelvis.com) — Notes de cours recalculées à partir des avis les mieux votés : crawler et scoring Python sans dépendances, pondération par racine du nombre de votes, calibrée contre un classement humain (ρ = 0,70 contre 0,42). 426 cours, site Astro.

[**Significado Total**](https://semioteca.vercel.app) — Application de recherche linguistique construite avec Python et Svelte

[**OmegaInt**](https://github.com/matiasagelvis/omegaint) — Bibliothèque C++ d'entiers à précision arbitraire
