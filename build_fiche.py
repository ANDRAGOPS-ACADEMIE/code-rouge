# -*- coding: utf-8 -*-
"""Fiche incendie A4 — ABSOLUTE positioning, decorations separated from text
(evite le bug de double-positionnement de l'importateur Express)."""

logo = open('/home/user/code-rouge/logo_tiny_datauri.txt').read().strip()

HTML = r'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<title>Fiche programme — Formation Incendie EPI — ANDRAGOPS</title>
<meta name="hz:slide-selector" content=".flyer" />
<meta name="hz:canvas-width" content="794" />
<meta name="hz:canvas-height" content="1123" />
<link rel="stylesheet" href="https://use.typekit.net/zlr6esn.css">
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:#d9dcde; }
  .flyer { position:relative; width:794px; height:1123px; background:#fff; overflow:hidden;
           font-family:"roboto","Roboto",sans-serif; color:#2b2f33; }
  .bebas { font-family:"bebas-neue-v14-deprecated","Bebas Neue",sans-serif; }
  .a { position:absolute; }
  /* decorative rectangles */
  .rect { position:absolute; }

  .sectxt { position:absolute; font-size:20px; color:#263238; letter-spacing:.8px; }
  .uline  { position:absolute; height:1.5px; background:#e2e4e6; }
  .square { position:absolute; width:13px; height:13px; background:#c0392b; border-radius:2px; }

  .badge { position:absolute; width:58px; height:52px; border-radius:6px; color:#fff; text-align:center; }
  .badge .n { font-size:23px; line-height:1; margin-top:9px; }
  .badge .u { font-size:8.5px; letter-spacing:.5px; }
</style>
</head>
<body>
  <div class="flyer" data-canvas-width="794" data-canvas-height="1123">

    <!-- bands -->
    <div class="rect" style="left:0; top:0; width:794px; height:6px; background:#c0392b;"></div>
    <div class="rect" style="left:0; top:98px; width:794px; height:10px; background:#e67e22;"></div>
    <div class="rect" style="left:0; top:1035px; width:794px; height:88px; background:#263238;"></div>

    <!-- header -->
    <img class="a" style="left:44px; top:22px; width:60px; height:56px;" src="__LOGO__" alt="ANDRAGOPS" width="60" height="56" />
    <div class="rect" style="left:120px; top:34px; width:3px; height:34px; background:#e67e22;"></div>
    <div class="a" style="left:134px; top:36px; width:230px; font-size:11px; line-height:1.3; color:#56606a; font-weight:500;">Santé, sécurité au travail &amp; secours d'urgence</div>
    <div class="a bebas" style="right:44px; top:30px; width:340px; text-align:right; font-size:28px; line-height:1; color:#c0392b; letter-spacing:1px;">FICHE PROGRAMME</div>
    <div class="a" style="right:44px; top:64px; width:340px; text-align:right; font-size:10px; color:#6a727a;">Réf. INC-EPI-1H30 · v1 · 06/2026</div>

    <!-- title -->
    <div class="rect" style="left:44px; top:121px; width:3px; height:18px; background:#e67e22;"></div>
    <div class="a bebas" style="left:55px; top:120px; font-size:16px; line-height:18px; color:#c0392b; letter-spacing:2px;">SÉCURITÉ INCENDIE</div>
    <div class="a bebas" style="left:44px; top:146px; width:706px; font-size:35px; line-height:0.98; color:#263238; letter-spacing:.5px;">FORMATION INCENDIE —<br/>ÉQUIPIER DE PREMIÈRE INTERVENTION</div>
    <div class="a" style="left:44px; top:226px; width:706px; font-size:13px; color:#56606a; font-weight:500;">Manipulation des extincteurs &amp; RIA — exercices sur feux réels écologiques · Sessions de 1&nbsp;h&nbsp;30</div>

    <!-- chips -->
    __CHIPS__

    <!-- LEFT: objectifs -->
    <div class="square" style="left:44px; top:344px;"></div>
    <div class="sectxt bebas" style="left:62px; top:340px;">OBJECTIFS PÉDAGOGIQUES</div>
    <div class="uline" style="left:44px; top:366px; width:394px;"></div>
    <div class="a" style="left:44px; top:376px; width:394px;">
      <div style="position:relative; margin-bottom:9px; font-size:12.5px; line-height:1.35; color:#33383d;"><span style="color:#e67e22; font-weight:700;">&#10003;</span>&nbsp; <b>Identifier</b> un départ de feu et ses mécanismes (triangle du feu, classes de feux).</div>
      <div style="position:relative; margin-bottom:9px; font-size:12.5px; line-height:1.35; color:#33383d;"><span style="color:#e67e22; font-weight:700;">&#10003;</span>&nbsp; <b>Donner l'alerte</b> et appliquer la consigne d'évacuation de l'établissement.</div>
      <div style="position:relative; margin-bottom:9px; font-size:12.5px; line-height:1.35; color:#33383d;"><span style="color:#e67e22; font-weight:700;">&#10003;</span>&nbsp; <b>Choisir</b> l'agent extincteur adapté à la classe de feu rencontrée.</div>
      <div style="position:relative; margin-bottom:9px; font-size:12.5px; line-height:1.35; color:#33383d;"><span style="color:#e67e22; font-weight:700;">&#10003;</span>&nbsp; <b>Utiliser</b> un extincteur et un RIA en sécurité, sur flammes réelles.</div>
    </div>

    <!-- LEFT: deroule -->
    <div class="square" style="left:44px; top:524px;"></div>
    <div class="sectxt bebas" style="left:62px; top:520px;">DÉROULÉ DE LA SESSION · 1 H 30</div>
    <div class="uline" style="left:44px; top:546px; width:394px;"></div>
    __STEPS__
    <div class="a" style="left:44px; top:1006px; width:394px; font-size:10px; color:#e67e22; font-weight:600; font-style:italic;">Pédagogie active — 80 % de pratique · Méthode C.A.D.R</div>

    <!-- RIGHT: cadre -->
    <div class="square" style="left:458px; top:344px;"></div>
    <div class="sectxt bebas" style="left:476px; top:340px;">CADRE RÉGLEMENTAIRE</div>
    <div class="uline" style="left:458px; top:366px; width:292px;"></div>
    <div class="rect" style="left:458px; top:374px; width:292px; height:104px; background:#f2f3f4;"></div>
    <div class="rect" style="left:458px; top:374px; width:3px; height:104px; background:#c0392b;"></div>
    <div class="a" style="left:471px; top:384px; width:266px; font-size:11px; color:#3a4045; line-height:1.4;"><b style="color:#263238;">Code du travail, art. R.4227-28 &amp; R.4227-39 :</b> l'employeur fournit des moyens de lutte contre l'incendie et organise, <b style="color:#263238;">au moins tous les 6 mois</b>, des exercices et essais périodiques. Le personnel doit être entraîné à manipuler extincteurs et RIA.</div>

    <!-- RIGHT: contenu -->
    <div class="square" style="left:458px; top:504px;"></div>
    <div class="sectxt bebas" style="left:476px; top:500px;">CONTENU</div>
    <div class="uline" style="left:458px; top:526px; width:292px;"></div>
    <div class="a" style="left:458px; top:538px; font-size:12px; font-weight:700; color:#c0392b;">Apports théoriques</div>
    <div class="a" style="left:458px; top:560px; width:292px;">
      <div style="margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3;"><span style="color:#c0392b;">&#9679;</span>&nbsp; Consignes et plans de sécurité en place</div>
      <div style="margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3;"><span style="color:#c0392b;">&#9679;</span>&nbsp; Triangle du feu : combustible, comburant, énergie</div>
      <div style="margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3;"><span style="color:#c0392b;">&#9679;</span>&nbsp; Classes de feux &amp; pictogrammes</div>
      <div style="margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3;"><span style="color:#c0392b;">&#9679;</span>&nbsp; Agents extincteurs et procédés d'extinction</div>
    </div>
    <div class="a" style="left:458px; top:650px; font-size:12px; font-weight:700; color:#e67e22;">Mise en pratique</div>
    <div class="a" style="left:458px; top:672px; width:292px;">
      <div style="margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3;"><span style="color:#e67e22;">&#9679;</span>&nbsp; Extincteurs du site : eau, poudre, CO₂</div>
      <div style="margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3;"><span style="color:#e67e22;">&#9679;</span>&nbsp; Présentation et utilisation du RIA</div>
      <div style="margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3;"><span style="color:#e67e22;">&#9679;</span>&nbsp; Extinction réelle encadrée individuellement</div>
      <div style="margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3;"><span style="color:#e67e22;">&#9679;</span>&nbsp; Générateur « feux propres » sans fumée</div>
    </div>

    <!-- RIGHT: organisation -->
    <div class="rect" style="left:458px; top:782px; width:292px; height:248px; background:#263238; border-radius:8px;"></div>
    <div class="a bebas" style="left:474px; top:796px; width:260px; font-size:17px; line-height:1.05; color:#fff;">PLUSIEURS GROUPES ?<br/>JOURNÉE TYPE</div>
    __SLOTS__
    <div class="a" style="left:474px; top:894px; width:260px; font-size:11px; line-height:1.4; color:#fff;">Jusqu'à <b style="color:#f0a35e;">32 personnes / jour</b> et par formateur. Organisable par entité (Trestec / Composites).</div>
    <div class="rect" style="left:474px; top:958px; width:260px; height:1px; background:rgba(255,255,255,.2);"></div>
    <div class="a" style="left:474px; top:968px; width:260px; font-size:10.5px; line-height:1.4; color:#cfd4d8;">Financement : prise en charge <b style="color:#f0a35e;">OPCO</b> possible — organisme certifié Qualiopi.</div>

    <!-- footer -->
    <div class="a bebas" style="left:0; top:1049px; width:794px; text-align:center; font-size:20px; color:#fff; letter-spacing:.8px;">ANDRAGOPS ACADÉMIE</div>
    <div class="a" style="left:0; top:1073px; width:794px; text-align:center; font-size:10.5px; color:#ffffffd9;">Damien Lemort — Formateur SST INRS / Formateur de formateurs</div>
    <div class="a" style="left:0; top:1091px; width:794px; text-align:center; font-size:12px; color:#f3b27a; font-weight:500;">07 59 73 82 72 · info@andragops-academie.fr · www.andragops-academie.fr</div>
    <div class="a" style="left:0; top:1108px; width:794px; text-align:center; font-size:9.5px; color:#ffffffcc;">Organisme certifié <span style="color:#e67e22;">Qualiopi</span> · Référent handicap dédié · Devis sous 48 h · Document non contractuel</div>

  </div>
</body>
</html>'''

# chips
chips_data = [("PUBLIC","Personnel désigné (1ʳᵉ intervention)"),("DURÉE","Session de 1 h 30 · intra"),
              ("EFFECTIF","8 participants max / session"),("LIEU","Sur votre site (Wervicq-Sud)"),
              ("VALIDATION","Attestation + registre")]
chips=""
for i,(k,v) in enumerate(chips_data):
    x=44+i*142
    chips+=f'''<div class="rect" style="left:{x}px; top:252px; width:134px; height:70px; background:#f2f3f4;"></div>
    <div class="rect" style="left:{x}px; top:252px; width:134px; height:9px; background:#263238;"></div>
    <div class="a bebas" style="left:{x+10}px; top:266px; font-size:14px; color:#c0392b; letter-spacing:.5px;">{k}</div>
    <div class="a" style="left:{x+10}px; top:286px; width:114px; font-size:10.5px; color:#2b2f33; font-weight:500; line-height:1.25;">{v}</div>
    '''

# timeline steps
steps_data=[("10","Accueil &amp; cadrage","Émargement, tour de table, objectifs, rappel des consignes et plans de sécurité du site.",False),
            ("25","Théorie du feu","Triangle du feu · classes de feux et pictogrammes · agents et procédés d'extinction · alerte, conduite à tenir et évacuation.",False),
            ("45","Pratique sur feux réels","Extincteurs (eau pulvérisée, poudre, CO₂) et RIA · extinction réelle sur générateur écologique : <b>chaque participant manipule</b>.",True),
            ("10","Débriefing &amp; validation","Reprise des gestes · évaluation comportementale · signature du registre · remise des attestations.",False)]
tops=[556,668,792,916]
steps=""
for (n,h,d,red),t in zip(steps_data,tops):
    bg="#c0392b" if red else "#263238"
    hcol="#263238" if red else "#c0392b"
    steps+=f'''<div class="badge bebas" style="left:44px; top:{t}px; background:{bg};"><div class="n">{n}</div><div class="u">MIN</div></div>
    <div class="a" style="left:116px; top:{t}px; width:322px; font-size:13.5px; font-weight:700; color:{hcol};">{h}</div>
    <div class="a" style="left:116px; top:{t+19}px; width:322px; font-size:11px; color:#444a4f; line-height:1.3;">{d}</div>
    '''

# orga slots
slots_data=[("08h30","S1"),("10h15","S2"),("13h30","S3"),("15h15","S4")]
slots=""
for i,(tt,ss) in enumerate(slots_data):
    x=474+i*68
    slots+=f'''<div class="rect" style="left:{x}px; top:844px; width:59px; height:36px; background:rgba(255,255,255,.1); border-radius:4px;"></div>
    <div class="a" style="left:{x}px; top:849px; width:59px; text-align:center; font-size:9px; color:#ffffffd9;">{tt}</div>
    <div class="a bebas" style="left:{x}px; top:860px; width:59px; text-align:center; font-size:15px; color:#fff;">{ss}</div>
    '''

HTML = HTML.replace('__LOGO__',logo).replace('__CHIPS__',chips).replace('__STEPS__',steps).replace('__SLOTS__',slots)
open('/home/user/code-rouge/fiche_incendie_onepager.html','w').write(HTML)

from weasyprint import HTML as W
W(filename='/home/user/code-rouge/fiche_incendie_onepager.html').write_pdf('/home/user/code-rouge/fiche_preview.pdf')
import fitz
d=fitz.open('/home/user/code-rouge/fiche_preview.pdf'); pix=d[0].get_pixmap(dpi=110)
pix.save('/home/user/code-rouge/fiche_preview.png')
print('written', len(HTML), 'chars; rendered', pix.width, pix.height)
