from crewai import Agent, Task, Crew, Process
from crewai.tools import tool
from typing import Dict, List, Any, Optional, TypedDict
import json
import datetime


# Typdefinitionen
class Transaction(TypedDict):
    transaction_id: str
    sender_account: str
    receiver_account: str
    amount: float
    timestamp: str
    description: Optional[str]
    is_realtime: bool


@tool
def get_user_transaction_history(account_id):
    """Ruft die letzten Transaktionen eines Nutzers aus der Datenbank ab."""
    # Simulierte Daten
    transactions = [
        {
            "transaction_id": "t123456",
            "amount": 1250.00,
            "timestamp": "2023-12-01T15:30:00Z",
            "receiver_account": "DE89370400440532013000",
            "description": "Monatsmiete Dezember"
        },
        {
            "transaction_id": "t123457",
            "amount": 89.99,
            "timestamp": "2023-12-03T10:15:00Z",
            "receiver_account": "DE12500105170648489890",
            "description": "Online-Einkauf Elektronik"
        },
        {
            "transaction_id": "t123458",
            "amount": 50.00,
            "timestamp": "2023-12-05T09:20:00Z",
            "receiver_account": "DE13600501017832594242",
            "description": "Überweisung an Freund"
        }
    ]
    return json.dumps(transactions)


@tool
def get_user_profile(account_id):
    """Ruft das Profil eines Nutzers aus der Datenbank ab."""
    # Simulierte Daten
    user_profile = {
        "account_id": account_id,
        "account_age_days": 730,
        "account_type": "private",
        "risk_score": 0.15,
        "average_transaction_amount": 450.75,
        "transaction_frequency": 12.5,  # Pro Monat
        "previous_flags": 1,
        "typical_countries": ["DE", "FR", "ES"],
        "typical_receivers": ["DE89370400440532013000", "DE12500105170648489890"]
    }
    return json.dumps(user_profile)


@tool
def get_similar_fraud_cases(case_features):
    """Findet ähnliche Betrugsfälle basierend auf den gegebenen Merkmalen."""
    # Simulierte Daten
    similar_cases = [
        {
            "case_id": "f987654",
            "similarity_score": 0.85,
            "features": {
                "amount_unusually_high": True,
                "new_receiver": True,
                "unusual_time": True
            },
            "outcome": "confirmed_fraud"
        },
        {
            "case_id": "f987655",
            "similarity_score": 0.78,
            "features": {
                "amount_unusually_high": True,
                "new_receiver": False,
                "unusual_time": True
            },
            "outcome": "false_positive"
        }
    ]
    return json.dumps(similar_cases)


class FraudDetectionSystem:
    def __init__(self):

        # Agenten erstellen
        self.ml_assessment_agent = self._create_ml_assessment_agent()
        self.rule_assessment_agent = self._create_rule_assessment_agent()
        self.explanation_agent = self._create_explanation_agent()
        self.decision_agent = self._create_decision_agent()
        self.coordinator_agent = self._create_coordinator_agent()
        self.react_agent = self._create_react_agent()

    def _create_ml_assessment_agent(self):
        """ML-Bewertungsagent erstellen."""
        return Agent(
            role="ML Fraud Assessment Model",
            goal="Bewerte Transaktionen auf ihre Betrugswahrscheinlichkeit mit ML-Methoden.",
            backstory="""Du bist ein fortschrittliches ML-Modell zur Betrugserkennung in Banktransaktionen.
            Du analysierst Transaktionen und bewertest ihre Betrugswahrscheinlichkeit.
            Deine Analyse basiert auf Transaktionsbetrag, Empfänger, Echtzeit-Status und Zeitpunkt.""",
            verbose=True,
            tools=[],
            allow_delegation=False
        )

    def _create_rule_assessment_agent(self):
        """Regelbasierter Bewertungsagent erstellen."""
        return Agent(
            role="Rule-Based Fraud Detection System",
            goal="Prüfe Transaktionen gegen feste Regeln, um Betrugsmuster zu erkennen.",
            backstory="""Du bist ein regelbasiertes System zur Betrugserkennung in Banktransaktionen.
            Du wendest feste Regeln an, um potenzielle Betrugsfälle zu identifizieren.
            Deine Regeln umfassen Betragsgrößen, Echtzeit-Status, ungewöhnliche Zeiten und neue Empfänger.""",
            verbose=True,
            tools=[],
            allow_delegation=False
        )

    def _create_explanation_agent(self):
        """Erklärungs-Agent erstellen."""
        return Agent(
            role="Fraud Explanation Expert",
            goal="Erkläre Betrugserkennungsergebnisse verständlich für Fraud-Manager.",
            backstory="""Du bist ein erklärender Agent für ein Betrugsbewertungssystem in einer Bank.
            Deine Aufgabe ist es, die Entscheidungen des Systems in natürlicher Sprache zu erklären.
            Du formulierst klare und präzise Erklärungen, warum eine Transaktion verdächtig erscheint.""",
            verbose=True,
            tools=[],
            allow_delegation=False
        )

    def _create_decision_agent(self):
        """Entscheidungs-Agent für Echtzeit-Transaktionen erstellen."""
        return Agent(
            role="Real-Time Decision Maker",
            goal="Triff autonome Entscheidungen für Echtzeit-Überweisungen.",
            backstory="""Du bist ein Entscheidungs-Agent für Echtzeitüberweisungen in einem Bankensystem.
            Du musst autonome Entscheidungen treffen, ob eine Transaktion genehmigt oder abgelehnt werden soll.
            Du wägst das Betrugsrisiko gegen die Kundenfreundlichkeit ab.""",
            verbose=True,
            tools=[],
            allow_delegation=False
        )

    def _create_coordinator_agent(self):
        """Koordinator-Agent erstellen."""
        return Agent(
            role="Fraud Detection Coordinator",
            goal="Koordiniere den Gesamtprozess der Betrugserkennung.",
            backstory="""Du bist ein Koordinator für das Betrugsbewertungssystem einer Bank.
            Du orchestrierst den Workflow zur Betrugserkennung und steuerst den Prozess zwischen verschiedenen Agenten.
            Du entscheidest, wie mit potenziellen Betrugsfällen weiter verfahren wird.""",
            verbose=True,
            tools=[],
            allow_delegation=True
        )

    def _create_react_agent(self):
        """ReAct-Agent für Datenbankabfragen erstellen."""
        return Agent(
            role="Database Query Agent",
            goal="Beantworte Anfragen des Fraud-Managers mit Datenbankabfragen.",
            backstory="""Du bist ein spezialisierter Agent für Datenbankabfragen in einem Betrugsbewertungssystem.
            Du hilfst dem Fraud-Manager, indem du relevante Informationen aus der Datenbank abrufst.
            Du kannst Transaktionshistorie, Nutzerprofile und ähnliche Betrugsfälle finden.""",
            verbose=True,

            tools=[
                get_user_transaction_history,
                get_user_profile,
                get_similar_fraud_cases
            ],
            allow_delegation=False
        )

    def process_transaction(self, transaction_data: Transaction):
        """
        Verarbeitet eine Transaktion durch das Betrugserkennungssystem.

        Args:
            transaction_data: Die zu prüfende Transaktion

        Returns:
            Ein Dictionary mit dem Ergebnis des Prozesses
        """
        # Task für ML-Bewertung erstellen
        ml_assessment_task = Task(
            description=f"""
            Bewerte die folgende Transaktion mit ML-Methoden:
            {json.dumps(transaction_data, indent=2)}

            Gib deine Antwort im folgenden Format zurück:
            {{
                "probability": 0.75,
                "threshold": 0.5,
                "is_fraud": true,
                "features": {{
                    "amount_unusually_high": true,
                    "new_receiver": true,
                    "is_realtime": true,
                    "unusual_time": false
                }},
                "model_version": "fraud-detection-v3.2"
            }}
            """,
            agent=self.ml_assessment_agent,
            expected_output="Eine JSON-Struktur mit der ML-Bewertung der Transaktion."
        )

        # Task für regelbasierte Bewertung erstellen
        rule_assessment_task = Task(
            description=f"""
            Prüfe die folgende Transaktion gegen das Regelwerk:
            {json.dumps(transaction_data, indent=2)}

            Prüfe folgende Regeln:
            1. Betrag > 5000 EUR -> "large_amount"
            2. Echtzeit-Überweisung -> "realtime_transfer"
            3. Transaktion zwischen 23:00 und 6:00 Uhr -> "unusual_time"
            4. Neue Empfänger-Kontonummer -> "new_receiver"
            5. Ungewöhnliche Beschreibung -> "suspicious_description"

            Gib deine Antwort im folgenden Format zurück:
            {{
                "is_flagged": true,
                "rules_triggered": ["large_amount", "realtime_transfer"],
                "version": "rule-engine-v2.1"
            }}
            """,
            agent=self.rule_assessment_agent,
            expected_output="Eine JSON-Struktur mit den ausgelösten Regeln."
        )

        # Task für Koordinator erstellen
        coordination_task = Task(
            description=f"""
            Koordiniere den weiteren Prozessverlauf basierend auf den Bewertungen.
            Verwende die Ergebnisse der ML-Bewertung und regelbasierten Bewertung, um zu entscheiden,
            welcher der folgenden Schritte als nächstes durchgeführt werden soll:

            1. "generate_explanation" - Bei Verdacht, aber nicht bei Echtzeit-Überweisungen
            2. "decision_agent" - Bei Echtzeit-Überweisungen und Verdacht
            3. "approve_transaction" - Bei keinem Verdacht

            Antworte nur mit einem der drei Befehle ohne weitere Erklärung.

            Dazu solltest du auf die Ergebnisse der vorherigen Bewertungen zugreifen:
            - ml_assessment_result: Das Ergebnis der ML-Bewertung
            - rule_assessment_result: Das Ergebnis der regelbasierten Bewertung
            """,
            agent=self.coordinator_agent,
            expected_output="Ein Befehl zur Weiterverarbeitung: 'generate_explanation', 'decision_agent' oder 'approve_transaction'.",
            context=[
                {
                    "ml_assessment_result": "{ml_assessment_task.output}",
                    "rule_assessment_result": "{rule_assessment_task.output}"
                }
            ]
        )

        # Task für Erklärung erstellen
        explanation_task = Task(
            description=f"""
            Erkläre, warum die folgende Transaktion verdächtig erscheint:
            {json.dumps(transaction_data, indent=2)}

            Nutze dazu die Ergebnisse der ML-Bewertung und regelbasierten Bewertung:
            - ml_assessment_result: Das Ergebnis der ML-Bewertung
            - rule_assessment_result: Das Ergebnis der regelbasierten Bewertung

            Formuliere eine klare, präzise und verständliche Erklärung für den Fraud-Manager.
            Beziehe dich dabei konkret auf die Bewertungsergebnisse und stelle Zusammenhänge her.
            """,
            agent=self.explanation_agent,
            expected_output="Eine Erklärung, warum die Transaktion verdächtig erscheint.",
            context=[
                {
                    "ml_assessment_result": "{ml_assessment_task.output}",
                    "rule_assessment_result": "{rule_assessment_task.output}"
                }
            ]
        )

        # Task für automatische Entscheidung erstellen
        decision_task = Task(
            description=f"""
            Treffe eine automatische Entscheidung für diese Echtzeit-Überweisung:
            {json.dumps(transaction_data, indent=2)}

            Nutze dazu die Ergebnisse der ML-Bewertung und regelbasierten Bewertung:
            - ml_assessment_result: Das Ergebnis der ML-Bewertung
            - rule_assessment_result: Das Ergebnis der regelbasierten Bewertung

            Gib deine Antwort im folgenden Format zurück:
            {{
                "decision": "approved",
                "confidence": 0.85,
                "reasoning": "Kurze Begründung deiner Entscheidung"
            }}

            Für decision darfst du nur "approved" oder "declined" verwenden.
            """,
            agent=self.decision_agent,
            expected_output="Eine Entscheidung mit Begründung im JSON-Format.",
            context=[
                {
                    "ml_assessment_result": "{ml_assessment_task.output}",
                    "rule_assessment_result": "{rule_assessment_task.output}"
                }
            ]
        )

        # Crew erstellen
        if transaction_data["is_realtime"]:
            # Bei Echtzeit-Transaktionen
            crew = Crew(
                agents=[
                    self.ml_assessment_agent,
                    self.rule_assessment_agent,
                    self.coordinator_agent,
                    self.decision_agent
                ],
                tasks=[
                    ml_assessment_task,
                    rule_assessment_task,
                    coordination_task,
                    decision_task
                ],
                verbose=True,
                process=Process.sequential  # Sequentieller Prozess für bessere Kontrolle
            )
        else:
            # Bei normalen Transaktionen
            crew = Crew(
                agents=[
                    self.ml_assessment_agent,
                    self.rule_assessment_agent,
                    self.coordinator_agent,
                    self.explanation_agent
                ],
                tasks=[
                    ml_assessment_task,
                    rule_assessment_task,
                    coordination_task,
                    explanation_task
                ],
                verbose=True,
                process=Process.sequential
            )

        # Crew ausführen
        result = crew.kickoff()

        # Ergebnisse auswerten und zurückgeben
        ml_assessment = self._extract_json(result[ml_assessment_task.id])
        rule_assessment = self._extract_json(result[rule_assessment_task.id])
        next_step = result[coordination_task.id].strip()

        if next_step == "approve_transaction":
            return {
                "transaction": transaction_data,
                "ml_assessment": ml_assessment,
                "rule_assessment": rule_assessment,
                "final_decision": "approved",
                "explanation": None
            }
        elif next_step == "decision_agent":
            decision = self._extract_json(result[decision_task.id])
            return {
                "transaction": transaction_data,
                "ml_assessment": ml_assessment,
                "rule_assessment": rule_assessment,
                "final_decision": decision["decision"],
                "explanation": decision["reasoning"]
            }
        elif next_step == "generate_explanation":
            explanation = result[explanation_task.id]
            return {
                "transaction": transaction_data,
                "ml_assessment": ml_assessment,
                "rule_assessment": rule_assessment,
                "explanation": explanation,
                "final_decision": None  # Hier würde in einer realen Anwendung auf den Fraud-Manager gewartet
            }
        else:
            return {
                "transaction": transaction_data,
                "ml_assessment": ml_assessment,
                "rule_assessment": rule_assessment,
                "error": f"Unerwartete Koordinator-Antwort: {next_step}"
            }

    def _extract_json(self, text):
        """Extrahiert JSON aus einem Text."""
        try:
            # Suche nach JSON-Strukturen im Text
            start = text.find('{')
            end = text.rfind('}') + 1
            if start >= 0 and end > start:
                json_str = text[start:end]
                return json.loads(json_str)
            return {}
        except:
            # Fallback bei ungültigem JSON
            return {}

    def interactive_fraud_manager_session(self, transaction_data: Transaction):
        """
        Startet eine interaktive Sitzung für einen Fraud-Manager.

        Args:
            transaction_data: Die zu überprüfende Transaktion

        Returns:
            Die finale Entscheidung
        """
        # Erste Analyse durchführen
        analysis_result = self.process_transaction(transaction_data)

        # Ergebnisse anzeigen
        print("\n===== FRAUD DETECTION SYSTEM =====")
        print(f"Transaktion ID: {transaction_data['transaction_id']}")
        print(f"Betrag: {transaction_data['amount']} EUR")
        print(
            f"ML-Bewertung: {analysis_result['ml_assessment'].get('probability', 0) * 100:.1f}% Betrugswahrscheinlichkeit")
        print(
            f"Regelbasierte Bewertung: {'Verdächtig' if analysis_result['rule_assessment'].get('is_flagged', False) else 'Unverdächtig'}")
        print("\nERKLÄRUNG:")
        print(analysis_result.get('explanation', 'Keine Erklärung verfügbar.'))
        print("\n-----------------------------------")
        print("Sie können nun mit dem System interagieren und Fragen stellen.")
        print("Befehle: GENEHMIGEN, ABLEHNEN, HILFE, BEENDEN")
        print("-----------------------------------")

        # Interaktiver Dialog mit dem ReAct-Agenten
        while True:
            user_input = input("\nFraud-Manager > ")

            if user_input.upper() == "BEENDEN":
                return "aborted"
            elif user_input.upper() == "GENEHMIGEN":
                return "approved"
            elif user_input.upper() == "ABLEHNEN":
                return "declined"
            elif user_input.upper() == "HILFE":
                print("\nVerfügbare Befehle:")
                print("- Stellen Sie Fragen zur Transaktion")
                print("- GENEHMIGEN: Transaktion freigeben")
                print("- ABLEHNEN: Transaktion ablehnen")
                print("- BEENDEN: Prozess abbrechen")
                continue

            # Frage an den ReAct-Agenten stellen
            query_task = Task(
                description=f"""
                Beantworte die folgende Frage des Fraud-Managers zur Transaktion {transaction_data['transaction_id']}:

                "{user_input}"

                Verwende deine Tools, um relevante Informationen aus der Datenbank abzurufen.
                Die Kontonummer des Absenders ist: {transaction_data['sender_account']}
                Die Kontonummer des Empfängers ist: {transaction_data['receiver_account']}
                """,
                agent=self.react_agent,
                expected_output="Eine ausführliche Antwort auf die Frage des Fraud-Managers."
            )

            # Eine temporäre Crew für diese einzelne Aufgabe erstellen
            temp_crew = Crew(
                agents=[self.react_agent],
                tasks=[query_task],
                verbose=False,
                process=Process.sequential
            )

            # Antwort abrufen und anzeigen
            query_result = temp_crew.kickoff()
            print(f"\n{query_result[query_task.id]}")

        return "undecided"


# Beispielnutzung
if __name__ == "__main__":
    # System initialisieren
    fraud_system = FraudDetectionSystem()

    # Beispieltransaktion für Überprüfung
    example_transaction = {
        "transaction_id": "tx98766",
        "sender_account": "DE55500105173984217489",
        "receiver_account": "FR7630006000011234567890189",
        "amount": 2500.00,
        "timestamp": "2023-12-15T22:45:00Z",
        "description": "Dringende Zahlung",
        "is_realtime": False
    }

    # Option zur automatischen oder interaktiven Verarbeitung
    mode = input("Modus wählen (1=Automatisch, 2=Interaktiv): ")

    if mode == "1":
        # Automatische Verarbeitung
        print("\n=== Automatische Betrugsanalyse wird durchgeführt ===")
        result = fraud_system.process_transaction(example_transaction)

        print("\n=== Ergebnis der Betrugsanalyse ===")
        print(f"Transaktion ID: {example_transaction['transaction_id']}")
        print(f"ML-Bewertung: {result['ml_assessment'].get('probability', 0) * 100:.1f}% Betrugswahrscheinlichkeit")
        print(
            f"Regelbasierte Bewertung: {'Verdächtig' if result['rule_assessment'].get('is_flagged', False) else 'Unverdächtig'}")

        if result.get('final_decision'):
            print(f"Finale Entscheidung: {result['final_decision'].upper()}")
        else:
            print("Empfehlung: Überprüfung durch Fraud-Manager erforderlich")

        if result.get('explanation'):
            print("\nErklärung:")
            print(result['explanation'])
    else:
        # Interaktive Sitzung
        print("\n=== Fraud Detection System gestartet ===")
        print("Starte interaktive Überprüfung für verdächtige Transaktion...")
        decision = fraud_system.interactive_fraud_manager_session(example_transaction)
        print(f"\nFinale Entscheidung: {decision.upper()}")
