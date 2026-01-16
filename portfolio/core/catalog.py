"""In-code catalog of projects and profile metadata.

A szerkeszthetőség kedvéért itt, egy helyen vannak a tartalmak. Nincs DB.
"""
from __future__ import annotations

import os
from typing import List

from .types import Profile, Project, SocialLink


def _env(name: str, default: str) -> str:
    val = os.environ.get(name, "").strip()
    return val or default


def build_profile() -> Profile:
    """Build the public profile shown on the hub page."""
    return Profile(
        name="Lázár András",
        tagline="Python AI fejlesztések",
        location="Herend, HU",
        email="alazar68@gmail.com",
        socials=[
            SocialLink(label="LinkedIn", url="https://www.linkedin.com/in/andras-lazar-57a283295/"),
            SocialLink(label="Facebook", url="https://www.facebook.com/andras.lazar.90?locale=hu_HU"),
            SocialLink(label="GitHub", url="https://github.com/alazar68-ship-it"),
        ],
    )


def build_projects() -> List[Project]:
    """Return the list of projects shown in the Projects section."""
    return [
        Project(
            key="digitrec",
            title="Digitrec – kézzel írott számfelismerés",
            note="28×28 canvas",
            tag="Digitrec · MNIST",
            description=(
                "Django + HTMX demó, ahol a felhasználó rajzol, a rendszer pedig MNIST-re tanított neurális hálóval "
                "azonnal predikciót ad. Osztályvalószínűségek és rejtett réteg-aktivációk vizualizációja is megjelenik."
            ),
            goal=(
                "Valós idejű ML inference web UI-ban (rajz → előfeldolgozás → predikció) úgy, hogy a felhasználó "
                "azonnali visszajelzést kapjon. Model interpretálhatóság demonstrálása (osztályvalószínűségek, "
                "rejtett réteg-aktivációk vizualizációja) anélkül, hogy a UX szétesne."
            ),
            chips=("Python", "PyTorch", "Django", "HTMX"),
            thumb_static_path="portfolio/images/Digitrec_MNIST.png",
            glow_class="glow-blue",
            demo_url=_env("DIGITREC_DEMO_URL", "https://digitrec.lazarsoft.hu"),
            github_url=_env("DIGITREC_GITHUB_URL", "https://github.com/alazar68-ship-it/Digitrec"),
        ),
        Project(
            key="tajmese",
            title="Tajmese – bekezdésenkénti mesegenerálás",
            note="CPU serving",
            tag="Tajmese · mini LLM",
            description=(
                "Tájnyelvi mesélő, reprodukálható tréning + serving projekt GPT-szerű (decoder-only) Transformerrel. HTMX-es UI "
                "bekezdésenként “mesél” a prompt alapján. Tréning oldalon seed/checkpoint/metaadatok, serving oldalon "
                "biztonságos inputkezelés."
            ),
            goal=(
                "Kis nyelvi modell (decoder-only Transformer) serving weben: felhasználói promptból bekezdésenként "
                "generált szöveg, HTMX interakcióval. A tréning/serving életciklus szemléltetése: determinisztikus futás "
                "(seed/checkpoint), kontrollált generálás (max token, stop feltételek)."
            ),
            chips=("Python", "PyTorch", "Django", "HTMX", "Tokenizálás / BPE"),
            thumb_static_path="portfolio/images/Tajmese_mini_LLM.png",
            glow_class="glow-purple",
            demo_url=_env("TAJMESE_DEMO_URL", "https://tajmese.lazarsoft.hu"),
            github_url=_env("TAJMESE_GITHUB_URL", "https://github.com/alazar68-ship-it/Tajmese"),
        ),
        Project(
            key="ragchat",
            title="RAG_Chat – “kicsi, de éles” RAG chat",
            note="BM25 + prompt",
            tag="RAG_Chat · retrieval",
            description=(
                "Production-oriented RAG chat webapp. Seholország dokumentumaiból tudásbázist épít, chunkol, "
                "BM25-szerű rangsorolással választ releváns részleteket, majd promptba injektálja. Opcionálisan "
                "Cloudflare Workers AI, de cred nélkül is determinisztikus fallback."
            ),
            goal=(
                "RAG pipeline bemutatása: dokumentum-feldolgozás (chunkolás) → retrieval → prompt-összeállítás → chat válasz. "
                "“Production-szemléletű” alapok: kis függőségi lábnyom, tiszta rétegezés, kontrollált input és válaszformátum."
            ),
            chips=("Django", "HTMX", "BM25", "Prompt assembly", "CSRF / validáció"),
            thumb_static_path="portfolio/images/RAG_Chat.png",
            glow_class="glow-teal",
            demo_url=_env("RAGCHAT_DEMO_URL", "https://ragchat.lazarsoft.hu"),
            github_url=_env("RAGCHAT_GITHUB_URL", "https://github.com/alazar68-ship-it/RAG_Chat"),
        ),
        Project(
            key="autochess",
            title="AutoChess – sakkmotorok párharca",
            note="UCI · state machine",
            tag="AutoChess · concurrency",
            description=(
                "Minimalista Django + HTMX alkalmazás: két UCI motor játszik egymás ellen. Tick jellegű végpont léptet "
                "egy fél-lépést (ply) kontrollált módon. A játékállapot DB-ben él, tranzakció és per-game lock védi a "
                "duplázott tick-eket (több tab / több néző esetén)."
            ),
            goal=(
                "Determinált állapotgép + concurrency-védelem: a meccs “tick”-ekkel léptethető, és több néző / több tab esetén "
                "se csússzon szét az állapot. UCI sakkmotor integráció demonstrálása, meccslogika és DB-persistencia mellett."
            ),
            chips=("Django", "HTMX", "UCI engine", "DB tranzakciók", "Locking"),
            thumb_static_path="portfolio/images/AutoChess.png",
            glow_class="glow-amber",
            demo_url=_env("AUTOCHESS_DEMO_URL", "https://autochess.lazarsoft.hu"),
            github_url=_env("AUTOCHESS_GITHUB_URL", "https://github.com/alazar68-ship-it/autoChess"),
        ),
    ]
