from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = "questions"

    # noinspection PyUnresolvedReferences,Pylint
    def ready(self):
        import questions.signals
