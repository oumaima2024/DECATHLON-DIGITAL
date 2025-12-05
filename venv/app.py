from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'decathlon_secret_key_2024'

# Route pour la page d'accueil (formulaire de personnalisation)
@app.route('/') 
def home(): 
    return render_template('index.html')

# Route pour le questionnaire QCM
@app.route('/creative-qcm') 
def qcm(): 
    return render_template('creative-qcm.html')

# Route pour les résultats du QCM
@app.route('/results', methods=['POST']) 
def results(): 
    nom = request.form.get('nom', '') 
    sport = request.form.get('sport', '') 
    niveau = request.form.get('niveau', '') 
    
    if sport == 'course': 
        rec = ['Chaussures Running Pro - 139€', 'Short technique - 45€', 'Montre Cardio GPS - 299€'] 
    else: 
        rec = ['Produit Premium 1 - 89€', 'Équipement Sportif 2 - 59€', 'Accessoire High-Tech 3 - 129€'] 
    
    return render_template('results.html', 
                          nom=nom, 
                          sport=sport, 
                          niveau=niveau, 
                          recommandations=rec)

# NOUVELLE ROUTE: Page principale après personnalisation
@app.route('/page-principale', methods=['GET', 'POST'])
def page_principale():
    # Si c'est une requête POST (formulaire soumis)
    if request.method == 'POST':
        # Récupérer les données du formulaire
        prenom = request.form.get('prenom', '').strip()
        nom = request.form.get('nom', '').strip()
        age = request.form.get('age', '')
        sport = request.form.get('sport', 'yoga')
        niveau = request.form.get('niveau', 'intermediaire')
        citation = request.form.get('citation', '').strip()
        
        # Sauvegarder dans la session
        session['user_profile'] = {
            'prenom': prenom,
            'nom': nom,
            'nom_complet': f"{prenom} {nom}",
            'age': age,
            'sport': sport,
            'niveau': niveau,
            'citation': citation if citation else "Cette technologie va révolutionner ma pratique sportive !",
            'initiales': f"{prenom[0] if prenom else ''}{nom[0] if nom else ''}".upper() or "NN"
        }
    
    # Récupérer le profil depuis la session ou rediriger vers l'accueil
    user_profile = session.get('user_profile')
    
    if not user_profile:
        # Si aucun profil, rediriger vers la page d'accueil
        return redirect(url_for('home'))
    
    # Déterminer la couleur et le message selon le sport
    sport_data = {
        'yoga': {
            'color': 'linear-gradient(45deg, #00b894, #00cec9)',
            'message': 'Atteignez l\'harmonie parfaite entre corps et esprit avec notre biofeedback.'
        },
        'musculation': {
            'color': 'linear-gradient(45deg, #ff6b6b, #ffa726)',
            'message': 'Optimisez vos performances avec notre technologie haptique avancée.'
        },
        'running': {
            'color': 'linear-gradient(45deg, #0984e3, #00cec9)',
            'message': 'Défiez vos limites avec nos parcours de réalité augmentée.'
        },
        'cyclisme': {
            'color': 'linear-gradient(45deg, #6c5ce7, #a29bfe)',
            'message': 'Pédalez dans des mondes virtuels époustouflants.'
        },
        'natation': {
            'color': 'linear-gradient(45deg, #00cec9, #0984e3)',
            'message': 'Analysez chaque mouvement avec notre technologie subaquatique.'
        },
        'crossfit': {
            'color': 'linear-gradient(45deg, #e17055, #fdcb6e)',
            'message': 'Repoussez vos limites avec notre suivi haute intensité.'
        },
        'tennis': {
            'color': 'linear-gradient(45deg, #00b894, #55efc4)',
            'message': 'Améliorez votre jeu avec notre analyse de mouvement précise.'
        }
    }
    
    sport_info = sport_data.get(user_profile.get('sport', 'yoga'), sport_data['yoga'])
    
    # Passer toutes les données au template
    return render_template('page-principale.html',
                         user=user_profile,
                         sport_color=sport_info['color'],
                         sport_message=sport_info['message'])

# Route pour le formulaire de personnalisation
@app.route('/personnaliser', methods=['POST'])
def personnaliser():
    # Récupérer les données du formulaire
    prenom = request.form.get('prenom', '').strip()
    nom = request.form.get('nom', '').strip()
    age = request.form.get('age', '')
    sport = request.form.get('sport', 'yoga')
    niveau = request.form.get('niveau', 'intermediaire')
    citation = request.form.get('citation', '').strip()
    
    # Sauvegarder dans la session
    session['user_profile'] = {
        'prenom': prenom,
        'nom': nom,
        'nom_complet': f"{prenom} {nom}",
        'age': age,
        'sport': sport,
        'niveau': niveau,
        'citation': citation if citation else "Cette technologie va révolutionner ma pratique sportive !",
        'initiales': f"{prenom[0] if prenom else ''}{nom[0] if nom else ''}".upper() or "NN"
    }
    
    # Rediriger vers la page principale
    return redirect(url_for('page_principale'))

if __name__ == '__main__': 
    print("=" * 60)
    print("🚀 SERVEUR FLASK DÉMARRÉ")
    print("=" * 60)
    print("📡 URLs disponibles :")
    print("  🌐 http://127.0.0.1:5000/              - Accueil")
    print("  🏠 http://127.0.0.1:5000/page-principale - Page principale")
    print("  📝 http://127.0.0.1:5000/creative-qcm  - Questionnaire QCM")
    print("  🎯 http://127.0.0.1:5000/results       - Résultats (POST uniquement)")
    print("=" * 60)
    app.run(debug=True, port=5000)