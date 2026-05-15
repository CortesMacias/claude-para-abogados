#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extractor y verificador de referencias legislativas.

Analiza todos los archivos CLAUDE.md y SKILL.md del proyecto y extrae
referencias a legislación española y europea. Agrupa por módulo,
deduplica y señala referencias que parecen incompletas.

Uso: python3 verificar-legislacion.py [--modulo NOMBRE] [--solo-incompletas]

Patrones que busca:
  - "art." / "arts." / "artículo" / "artículos" seguidos de números
  - Leyes: "Ley", "Ley Orgánica", "Real Decreto", "Real Decreto-ley"
  - Códigos: "Código Civil", "Código Penal", "Código de Comercio", etc.
  - Normativa UE: "RGPD", "Reglamento (UE)", "Directiva"
  - Normativa específica: "LOPDGDD", "LSC", "LEC", "LECrim", "LJCA",
    "ET", "LRJSP", "LPAC", "LGT", "LIVA", "LIRPF", "LIS", etc.

Código de salida: 0 siempre (informativo), 1 si hay incompletas con --solo-incompletas.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

# Directorio raíz del proyecto
RAIZ = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------
# Patrones de búsqueda de legislación
# -----------------------------------------------------------------------

# Artículos sueltos (art. 23, arts. 1 a 5, artículo 12.3)
PATRON_ARTICULO = re.compile(
    r"\b(arts?\.\s*\d[\d\s.,a-záéíóú]*"
    r"|artículos?\s+\d[\d\s.,a-záéíóú]*)",
    re.IGNORECASE,
)

# Leyes con nombre completo (Ley 1/2020, Ley Orgánica 3/2018, etc.)
PATRON_LEY = re.compile(
    r"\b(Ley\s+Orgánica\s+\d+/\d{4}[^.\n]{0,80}"
    r"|Ley\s+\d+/\d{4}[^.\n]{0,80}"
    r"|Ley\s+(?:General\s+)?(?:de|del)\s+[A-ZÁÉÍÓÚÑ][^.\n]{0,80})",
    re.IGNORECASE,
)

# Real Decreto, Real Decreto Legislativo, Real Decreto-ley
PATRON_RD = re.compile(
    r"\b(Real\s+Decreto(?:-ley|[\s-]+Legislativo)?\s+\d+/\d{4}[^.\n]{0,80})",
    re.IGNORECASE,
)

# Reglamentos y Directivas UE
PATRON_UE = re.compile(
    r"\b(Reglamento\s+\((?:UE|CE)\)\s+\d+/\d{4}[^.\n]{0,60}"
    r"|Directiva\s+\(?\s*(?:UE|CE)\s*\)?\s*\d+/\d{1,4}[^.\n]{0,60}"
    r"|Directiva\s+\d{4}/\d+/(?:UE|CE)[^.\n]{0,60})",
    re.IGNORECASE,
)

# Códigos
PATRON_CODIGO = re.compile(
    r"\b(Código\s+(?:Civil|Penal|de\s+Comercio|Mercantil))",
    re.IGNORECASE,
)

# Siglas legislativas conocidas
SIGLAS = [
    "RGPD", "LOPDGDD", "LSC", "LEC", "LECrim", "LJCA", "LRJSP", "LPAC",
    "LGT", "LIVA", "LIRPF", "LIS", "ET", "LISOS", "LOPJ", "LOTC",
    "TRLGSS", "TREBEP", "TRLIS", "TRLSC", "TRLGDCU", "CNMV", "AEPD",
    "LAU", "LAR", "LPH", "LOE", "LSRL", "TRLGSS", "LGSS", "LETA",
    "LJS", "LRJS", "LOREG", "RIA", "IA Act",
]

PATRON_SIGLA = re.compile(
    r"\b(" + "|".join(re.escape(s) for s in SIGLAS) + r")\b"
)

# Patrón para detectar referencias incompletas
# "art." sin número después, "Ley" sin número, etc.
PATRON_INCOMPLETA_ART = re.compile(r"\bart\.(?:\s*$|\s+[^0-9])", re.MULTILINE)
PATRON_INCOMPLETA_LEY = re.compile(
    r"\bLey\s+(?:Orgánica\s+)?(?:de[l]?\s+)?$", re.MULTILINE
)


def detectar_modulos() -> list[Path]:
    """Devuelve los módulos del proyecto."""
    return sorted(
        d for d in RAIZ.iterdir()
        if d.is_dir() and (d / ".claude-plugin").is_dir()
    )


def extraer_referencias(texto: str) -> tuple[list[str], list[str]]:
    """Extrae referencias legislativas de un texto.
    Devuelve (referencias, incompletas)."""
    refs = set()
    incompletas = []

    # Artículos
    for m in PATRON_ARTICULO.finditer(texto):
        ref = m.group(1).strip().rstrip(",.")
        refs.add(ref)

    # Leyes
    for m in PATRON_LEY.finditer(texto):
        ref = m.group(1).strip().rstrip(",.")
        # Limpiar: truncar en la primera coma o punto que no sea parte de la referencia
        ref = re.split(r"[,;]", ref)[0].strip()
        refs.add(ref)

    # Reales Decretos
    for m in PATRON_RD.finditer(texto):
        ref = re.split(r"[,;]", m.group(1).strip())[0].strip().rstrip(".")
        refs.add(ref)

    # Normativa UE
    for m in PATRON_UE.finditer(texto):
        ref = re.split(r"[,;]", m.group(1).strip())[0].strip().rstrip(".")
        refs.add(ref)

    # Códigos
    for m in PATRON_CODIGO.finditer(texto):
        refs.add(m.group(1).strip())

    # Siglas
    for m in PATRON_SIGLA.finditer(texto):
        refs.add(m.group(1))

    # Detectar incompletas
    for m in PATRON_INCOMPLETA_ART.finditer(texto):
        # Contexto: 40 caracteres alrededor
        inicio = max(0, m.start() - 20)
        fin = min(len(texto), m.end() + 20)
        contexto = texto[inicio:fin].replace("\n", " ").strip()
        incompletas.append(f"art. sin número: \"...{contexto}...\"")

    return sorted(refs), incompletas


def main() -> int:
    # Parsear argumentos
    modulo_filtro = None
    solo_incompletas = False
    args = sys.argv[1:]

    if "--modulo" in args:
        idx = args.index("--modulo")
        if idx + 1 < len(args):
            modulo_filtro = args[idx + 1]
        else:
            print("Error: --modulo requiere un nombre de módulo", file=sys.stderr)
            return 2

    if "--solo-incompletas" in args:
        solo_incompletas = True

    modulos = detectar_modulos()
    if modulo_filtro:
        modulos = [m for m in modulos if m.name == modulo_filtro]
        if not modulos:
            print(f"ERROR: Módulo '{modulo_filtro}' no encontrado", file=sys.stderr)
            return 2

    # Recopilar todas las referencias
    todas_las_refs: set[str] = set()
    refs_por_modulo: dict[str, set[str]] = defaultdict(set)
    incompletas_por_modulo: dict[str, list[str]] = defaultdict(list)
    archivos_analizados = 0

    for modulo in modulos:
        nombre = modulo.name

        # Archivos a analizar: CLAUDE.md y todos los SKILL.md
        archivos: list[Path] = []
        claude_md = modulo / "CLAUDE.md"
        if claude_md.exists():
            archivos.append(claude_md)

        skills_dir = modulo / "skills"
        if skills_dir.is_dir():
            archivos.extend(skills_dir.rglob("SKILL.md"))

        for archivo in archivos:
            archivos_analizados += 1
            texto = archivo.read_text(encoding="utf-8")
            refs, incompletas = extraer_referencias(texto)

            for ref in refs:
                todas_las_refs.add(ref)
                refs_por_modulo[nombre].add(ref)

            for inc in incompletas:
                archivo_rel = f"{nombre}/{archivo.relative_to(modulo)}"
                incompletas_por_modulo[nombre].append(f"{archivo_rel}: {inc}")

    # -------------------------------------------------------------------
    # Salida
    # -------------------------------------------------------------------
    print(f"\n{'='*70}")
    print(f"  Referencias legislativas — {len(modulos)} módulos, {archivos_analizados} archivos")
    print(f"{'='*70}\n")

    if not solo_incompletas:
        # Por módulo
        for modulo in modulos:
            nombre = modulo.name
            refs = refs_por_modulo.get(nombre, set())
            if refs:
                print(f"  {nombre} ({len(refs)} referencia(s)):")
                for ref in sorted(refs):
                    print(f"    - {ref}")
            else:
                print(f"  {nombre}: sin referencias detectadas")
            print()

        # Lista global deduplicada
        print(f"{'='*70}")
        print(f"  Lista global deduplicada ({len(todas_las_refs)} referencia(s) únicas)")
        print(f"{'='*70}\n")

        for ref in sorted(todas_las_refs, key=lambda r: r.lower()):
            # Indicar en cuántos módulos aparece
            n_modulos = sum(
                1 for refs in refs_por_modulo.values() if ref in refs
            )
            sufijo = f" [{n_modulos} módulo(s)]" if n_modulos > 1 else ""
            print(f"  - {ref}{sufijo}")

    # Incompletas
    total_incompletas = sum(len(v) for v in incompletas_por_modulo.values())
    if total_incompletas > 0:
        print(f"\n{'='*70}")
        print(f"  ADVERTENCIA: {total_incompletas} referencia(s) posiblemente incompleta(s)")
        print(f"{'='*70}\n")
        for nombre, incs in sorted(incompletas_por_modulo.items()):
            for inc in incs:
                print(f"  ⚠ {inc}")

    elif not solo_incompletas:
        print(f"\n  ✓ No se detectaron referencias incompletas.\n")

    if solo_incompletas:
        return 1 if total_incompletas > 0 else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
