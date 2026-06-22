# -*- coding: utf-8 -*-
"""Fiche incendie A4 — ABSOLUTE positioning (pixel-perfect, robust for Express).
Renders to PNG via weasyprint for visual verification."""

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
  @page { size: 794px 1123px; margin: 0; }
  body { background:#d9dcde; }
  .flyer {
    position:absolute; top:0; left:0;
    width:794px; height:1123px; background:#ffffff; overflow:hidden;
    font-family:"roboto","Roboto",sans-serif; color:#2b2f33;
  }
  .abs { position:absolute; }
  .bebas { font-family:"bebas-neue-v14-deprecated","Bebas Neue",sans-serif; }

  /* bands */
  .topbar { position:absolute; left:0; top:0; width:794px; height:6px; background:#c0392b; }
  .stripe { position:absolute; left:0; top:98px; width:794px; height:10px; background:#e67e22; }
  .footer { position:absolute; left:0; top:1035px; width:794px; height:88px; background:#263238; }

  /* header */
  .logo { position:absolute; left:44px; top:22px; width:60px; height:56px; }
  .htag { position:absolute; left:120px; top:34px; width:236px; height:34px;
          border-left:3px solid #e67e22; padding-left:11px;
          font-size:11px; line-height:1.3; color:#56606a; font-weight:500; display:flex; align-items:center; }
  .flabel { position:absolute; right:44px; top:30px; width:320px; text-align:right;
            font-size:28px; line-height:1; color:#c0392b; letter-spacing:1px; }
  .fref { position:absolute; right:44px; top:64px; width:320px; text-align:right;
          font-size:10px; color:#6a727a; }

  /* title */
  .eyebrow { position:absolute; left:44px; top:122px; height:18px;
             border-left:3px solid #e67e22; padding-left:11px;
             font-size:16px; line-height:18px; color:#c0392b; letter-spacing:2px; }
  .h1 { position:absolute; left:44px; top:146px; width:706px;
        font-size:35px; line-height:0.98; color:#263238; letter-spacing:.5px; }
  .subtitle { position:absolute; left:44px; top:226px; width:706px;
              font-size:13px; color:#56606a; font-weight:500; }

  /* chips */
  .chip { position:absolute; top:252px; width:134px; height:70px; background:#f2f3f4; padding:9px 10px; }
  .chip .top { position:absolute; left:0; top:0; width:134px; height:9px; background:#263238; }
  .chip .k { font-size:14px; color:#c0392b; letter-spacing:.5px; margin-top:4px; }
  .chip .v { font-size:10.5px; color:#2b2f33; font-weight:500; line-height:1.25; margin-top:3px; }

  /* section titles */
  .sec { position:absolute; height:24px; border-bottom:1.5px solid #e2e4e6;
         font-size:20px; color:#263238; letter-spacing:.8px; padding-left:18px; }
  .sec::before { content:""; position:absolute; left:0; top:3px; width:13px; height:13px; background:#c0392b; border-radius:2px; }

  /* objectives */
  .obj { position:absolute; left:44px; width:394px; }
  .obj .it { position:relative; padding-left:24px; margin-bottom:9px; font-size:12.5px; line-height:1.35; color:#33383d; }
  .obj .it::before { content:"\2713"; position:absolute; left:0; top:1px; width:17px; height:17px; border-radius:50%;
                     background:#e67e22; color:#fff; font-size:10px; text-align:center; line-height:17px; font-weight:700; }
  .obj .it b { color:#263238; }

  /* timeline */
  .step { position:absolute; left:44px; width:394px; }
  .step .badge { position:absolute; left:0; top:0; width:58px; height:52px; background:#263238; border-radius:6px;
                 color:#fff; text-align:center; }
  .step .badge .n { font-size:23px; line-height:1; margin-top:9px; }
  .step .badge .u { font-size:8.5px; letter-spacing:.5px; opacity:.85; }
  .step.red .badge { background:#c0392b; }
  .step .b { position:absolute; left:72px; width:322px; top:0; }
  .step .b .h { font-size:13.5px; font-weight:700; color:#c0392b; }
  .step.red .b .h { color:#263238; }
  .step .b .d { font-size:11px; color:#444a4f; line-height:1.3; margin-top:3px; }
  .mnote { position:absolute; left:44px; width:394px; top:1006px; font-size:10px; color:#e67e22; font-weight:600; font-style:italic; }

  /* right column */
  .reg { position:absolute; left:458px; top:366px; width:292px; background:#f2f3f4;
         border-left:3px solid #c0392b; padding:11px 13px; font-size:11px; color:#3a4045; line-height:1.4; }
  .reg b { color:#263238; }
  .cbh { position:absolute; left:458px; font-size:12px; font-weight:700; }
  .cbl { position:absolute; left:458px; width:292px; }
  .cbl .it { position:relative; padding-left:14px; margin-bottom:5px; font-size:11px; color:#3a4045; line-height:1.3; }
  .cbl .it::before { content:""; position:absolute; left:0; top:5px; width:6px; height:6px; border-radius:50%; background:#c0392b; }
  .cbl.prat .it::before { background:#e67e22; }

  /* organisation */
  .orga { position:absolute; left:458px; top:782px; width:292px; height:248px; background:#263238; border-radius:8px; padding:14px 16px; color:#fff; }
  .orga .h { font-size:17px; letter-spacing:.5px; line-height:1.05; }
  .orga .grid { position:absolute; left:16px; top:62px; width:260px; height:36px; }
  .orga .slot { position:absolute; top:0; width:59px; height:36px; background:rgba(255,255,255,.1); border-radius:4px; text-align:center; }
  .orga .slot .t { font-size:9px; opacity:.85; margin-top:5px; }
  .orga .slot .s { font-size:15px; }
  .orga .tot { position:absolute; left:16px; top:112px; width:260px; font-size:11px; line-height:1.4; }
  .orga .tot b { color:#f0a35e; }
  .orga .fin { position:absolute; left:16px; top:176px; width:260px; font-size:10.5px; line-height:1.4; color:#cfd4d8;
               border-top:1px solid rgba(255,255,255,.18); padding-top:9px; }
  .orga .fin b { color:#f0a35e; }

  /* footer */
  .f-name { position:absolute; left:0; top:14px; width:794px; text-align:center; font-size:20px; color:#fff; letter-spacing:.8px; }
  .f-role { position:absolute; left:0; top:38px; width:794px; text-align:center; font-size:10.5px; color:#ffffffd9; }
  .f-contact { position:absolute; left:0; top:56px; width:794px; text-align:center; font-size:12px; color:#f3b27a; font-weight:500; }
  .f-badges { position:absolute; left:0; top:74px; width:794px; text-align:center; font-size:9.5px; color:#ffffffcc; }
  .f-badges span { color:#e67e22; }
</style>
</head>
<body>
  <div class="flyer">
    <div class="topbar"></div>

    <!-- header -->
    <img class="logo" src="__LOGO__" alt="ANDRAGOPS" />
    <div class="htag">Santé, sécurité au travail &amp; secours d'urgence</div>
    <div class="flabel bebas">FICHE PROGRAMME</div>
    <div class="fref">Réf. INC-EPI-1H30 · v1 · 06/2026</div>
    <div class="stripe"></div>

    <!-- title -->
    <div class="eyebrow bebas">SÉCURITÉ INCENDIE</div>
    <div class="h1 bebas">FORMATION INCENDIE —<br/>ÉQUIPIER DE PREMIÈRE INTERVENTION</div>
    <div class="subtitle">Manipulation des extincteurs &amp; RIA — exercices sur feux réels écologiques · Sessions de 1&nbsp;h&nbsp;30</div>

    <!-- chips -->
    <div class="chip" style="left:44px"><div class="top"></div><div class="k bebas">PUBLIC</div><div class="v">Personnel désigné (1ʳᵉ intervention)</div></div>
    <div class="chip" style="left:186px"><div class="top"></div><div class="k bebas">DURÉE</div><div class="v">Session de 1 h 30 · intra</div></div>
    <div class="chip" style="left:328px"><div class="top"></div><div class="k bebas">EFFECTIF</div><div class="v">8 participants max / session</div></div>
    <div class="chip" style="left:470px"><div class="top"></div><div class="k bebas">LIEU</div><div class="v">Sur votre site (Wervicq-Sud)</div></div>
    <div class="chip" style="left:612px"><div class="top"></div><div class="k bebas">VALIDATION</div><div class="v">Attestation + registre</div></div>

    <!-- LEFT -->
    <div class="sec bebas" style="left:44px; top:340px; width:394px;">OBJECTIFS PÉDAGOGIQUES</div>
    <div class="obj" style="top:374px;">
      <div class="it"><b>Identifier</b> un départ de feu et ses mécanismes (triangle du feu, classes de feux).</div>
      <div class="it"><b>Donner l'alerte</b> et appliquer la consigne d'évacuation de l'établissement.</div>
      <div class="it"><b>Choisir</b> l'agent extincteur adapté à la classe de feu rencontrée.</div>
      <div class="it"><b>Utiliser</b> un extincteur et un RIA en sécurité, sur flammes réelles.</div>
    </div>

    <div class="sec bebas" style="left:44px; top:520px; width:394px;">DÉROULÉ DE LA SESSION · 1 H 30</div>
    <div class="step" style="top:556px;"><div class="badge bebas"><div class="n">10</div><div class="u">MIN</div></div><div class="b"><div class="h">Accueil &amp; cadrage</div><div class="d">Émargement, tour de table, objectifs, rappel des consignes et plans de sécurité du site.</div></div></div>
    <div class="step" style="top:668px;"><div class="badge bebas"><div class="n">25</div><div class="u">MIN</div></div><div class="b"><div class="h">Théorie du feu</div><div class="d">Triangle du feu · classes de feux et pictogrammes · agents et procédés d'extinction · alerte, conduite à tenir et évacuation.</div></div></div>
    <div class="step red" style="top:792px;"><div class="badge bebas"><div class="n">45</div><div class="u">MIN</div></div><div class="b"><div class="h">Pratique sur feux réels</div><div class="d">Extincteurs (eau pulvérisée, poudre, CO₂) et RIA · extinction réelle sur générateur écologique : <b>chaque participant manipule</b>.</div></div></div>
    <div class="step" style="top:916px;"><div class="badge bebas"><div class="n">10</div><div class="u">MIN</div></div><div class="b"><div class="h">Débriefing &amp; validation</div><div class="d">Reprise des gestes · évaluation comportementale · signature du registre · remise des attestations.</div></div></div>
    <div class="mnote">Pédagogie active — 80 % de pratique · Méthode C.A.D.R</div>

    <!-- RIGHT -->
    <div class="sec bebas" style="left:458px; top:340px; width:292px;">CADRE RÉGLEMENTAIRE</div>
    <div class="reg"><b>Code du travail, art. R.4227-28 &amp; R.4227-39 :</b> l'employeur fournit des moyens de lutte contre l'incendie et organise, <b>au moins tous les 6 mois</b>, des exercices et essais. Le personnel doit être entraîné à manipuler extincteurs et RIA.</div>

    <div class="sec bebas" style="left:458px; top:486px; width:292px;">CONTENU</div>
    <div class="cbh" style="top:520px; color:#c0392b;">Apports théoriques</div>
    <div class="cbl" style="top:540px;">
      <div class="it">Consignes et plans de sécurité en place</div>
      <div class="it">Triangle du feu : combustible, comburant, énergie</div>
      <div class="it">Classes de feux &amp; pictogrammes</div>
      <div class="it">Agents extincteurs et procédés d'extinction</div>
    </div>
    <div class="cbh" style="top:632px; color:#e67e22;">Mise en pratique</div>
    <div class="cbl prat" style="top:652px;">
      <div class="it">Extincteurs du site : eau, poudre, CO₂</div>
      <div class="it">Présentation et utilisation du RIA</div>
      <div class="it">Extinction réelle encadrée individuellement</div>
      <div class="it">Générateur « feux propres » sans fumée</div>
    </div>

    <div class="orga">
      <div class="h bebas">PLUSIEURS GROUPES ?<br/>JOURNÉE TYPE</div>
      <div class="grid">
        <div class="slot" style="left:0;"><div class="t">08h30</div><div class="s bebas">S1</div></div>
        <div class="slot" style="left:68px;"><div class="t">10h15</div><div class="s bebas">S2</div></div>
        <div class="slot" style="left:136px;"><div class="t">13h30</div><div class="s bebas">S3</div></div>
        <div class="slot" style="left:204px;"><div class="t">15h15</div><div class="s bebas">S4</div></div>
      </div>
      <div class="tot">Jusqu'à <b>32 personnes / jour</b> et par formateur. Organisable par entité (Trestec / Composites).</div>
      <div class="fin">Financement : prise en charge <b>OPCO</b> possible — organisme certifié Qualiopi.</div>
    </div>

    <!-- footer -->
    <div class="footer">
      <div class="f-name bebas">ANDRAGOPS ACADÉMIE</div>
      <div class="f-role">Damien Lemort — Formateur SST INRS / Formateur de formateurs</div>
      <div class="f-contact">07 59 73 82 72 · info@andragops-academie.fr · www.andragops-academie.fr</div>
      <div class="f-badges">Organisme certifié <span>Qualiopi</span> · Référent handicap dédié · Devis sous 48 h · Document non contractuel</div>
    </div>
  </div>
</body>
</html>'''

HTML = HTML.replace('__LOGO__', logo)
open('/home/user/code-rouge/fiche_incendie_onepager.html', 'w').write(HTML)

# Render preview PNG with weasyprint
try:
    from weasyprint import HTML as WHTML
    WHTML(string=HTML).write_png('/home/user/code-rouge/fiche_preview.png', resolution=96)
    print('rendered preview OK')
except Exception as e:
    print('render error:', e)
print('written', len(HTML), 'chars')
