"""
Script de test pour vérifier l'installation de SEO Dev Env
"""

def test_imports():
    """Test que tous les modules s'importent correctement"""
    try:
        from seo import creer_projet, creer_projet_interactif, main
        from seo.cli import collecter_preferences, afficher_titre
        from seo.commandes import commande_db, commande_user, commande_run
        from seo.generators import EnvironnementGenerator
        from seo.utils import creer_fichier, copier_dossier
        print("✅ Tous les imports réussis")
        return True
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False


def test_cli_functions():
    """Test que les fonctions CLI existent"""
    from seo.cli import poser_question, poser_question_texte, confirmer
    print("✅ Fonctions CLI disponibles")
    return True


def test_commandes():
    """Test que les commandes sont définies"""
    from seo.commandes import afficher_aide
    print("✅ Commandes définies")
    return True


def main():
    print("\n" + "="*60)
    print("🧪 Test d'Installation - SEO Dev Env")
    print("="*60 + "\n")
    
    tests = [
        ("Imports de base", test_imports),
        ("Fonctions CLI", test_cli_functions),
        ("Commandes", test_commandes),
    ]
    
    resultats = []
    for nom, test_func in tests:
        print(f"\n🔍 Test: {nom}")
        try:
            resultat = test_func()
            resultats.append(resultat)
        except Exception as e:
            print(f"❌ Erreur: {e}")
            resultats.append(False)
    
    print("\n" + "="*60)
    if all(resultats):
        print("✅ TOUS LES TESTS RÉUSSIS")
        print("\n💡 Vous pouvez maintenant utiliser:")
        print("   seo create")
        print("   seo --help")
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("\n💡 Réinstaller avec: pip install -e .")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
