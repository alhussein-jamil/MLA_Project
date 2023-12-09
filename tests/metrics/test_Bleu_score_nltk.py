import unittest
import torch
from metrics.bleu import BLEUScoreNLTK

class TestBLEUScoreNLTK(unittest.TestCase):
    def setUp(self):
        # Créer des exemples de tenseurs pour les tests
        self.reference_tensor = torch.tensor([[1, 2, 3, 4, 8], [4, 5, 7, 10, 5]])
        self.candidate_tensor = torch.tensor([[1, 2, 3, 4, 8], [5, 5, 7, 10, 5]])

        # Créer une instance de la classe BLEUScoreNLTK pour les tests
        self.bleu_score_nltk = BLEUScoreNLTK(self.reference_tensor, self.candidate_tensor)

    def test_initialization(self):
        # Vérifier si les attributs sont correctement initialisés
        self.assertEqual(self.bleu_score_nltk.reference_tensor.tolist(), self.reference_tensor.tolist())
        self.assertEqual(self.bleu_score_nltk.candidate_tensor.tolist(), self.candidate_tensor.tolist())
        self.assertEqual(self.bleu_score_nltk.bleu_scores, [])

    def test_bleu_score_calculation(self):
        # Calculer le score BLEU à l'aide de la méthode de la classe
        result = self.bleu_score_nltk.calculate_bleu_score()

        # Ajouter des assertions en fonction des résultats attendus
        # Par exemple, vérifier si le score BLEU est dans une plage acceptable
        self.assertIsInstance(result, torch.Tensor)
        scores = torch.tensor([1.0000,0.6687])
        for i,r in enumerate(result):
            self.assertGreaterEqual(r, 0.0)
            self.assertLessEqual(r, 1.0)
            self.assertAlmostEqual(r.item(), scores[i].item(), places=4)
            

# Créer un test runner et exécuter les tests
runner = unittest.TextTestRunner()
result = runner.run(unittest.makeSuite(TestBLEUScoreNLTK))