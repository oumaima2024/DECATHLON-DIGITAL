from flask import Flask, render_template, request 
app = Flask(__name__) 
@app.route('/') 
def home(): return render_template('index.html') 
@app.route('/page-principale') 
def pageprincipale(): return render_template('page-principale.html') 
@app.route('/creative-qcm') 
def qcm(): return render_template('creative-qcm.html') 
@app.route('/results', methods=['POST']) 
def results(): 
    nom = request.form.get('nom', '') 
    sport = request.form.get('sport', '') 
    niveau = request.form.get('niveau', '') 
    if sport == 'course': rec = ['Chaussures', 'Short', 'Montre'] 
    else: rec = ['Produit 1', 'Produit 2', 'Produit 3'] 
    return render_template('results.html', nom=nom, sport=sport, niveau=niveau, recommandations=rec) 
if __name__ == '__main__': app.run(debug=True, port=5000) 
