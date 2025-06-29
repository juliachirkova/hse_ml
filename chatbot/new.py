from mini_api import mini_chat
import re
import json

class ChatBot:
    roles_data = {
        "MLOps Engineer": {
            "intro": (
                "Ты выступаешь в роли HR-бота в компании, которая ищет MLOps-инженера. "
                "Твоя задача – проводить первичное интервью и выяснять детали, касающиеся автоматизации и деплоя ML-моделей."
            ),
            "requirements": (
                "Основные требования к кандидату:\n"
                "1) Глубокое понимание CI/CD-процессов и инструментария (Jenkins, GitLab CI, GitHub Actions)\n"
                "2) Опыт контейнеризации (Docker, Kubernetes) и оркестрации\n"
                "3) Знание облачных платформ (AWS, GCP, Azure) и навыки автоматизации инфраструктуры\n"
                "4) Понимание моделей ML и умение работать с ML-фреймворками\n"
                "5) Практический опыт построения ML-пайплайнов в проде."
            ),
            "red_flags": (
                "Ред-флаги:\n"
                "- Отсутствие реального опыта автоматизации и деплоя моделей\n"
                "- Недостаточное понимание DevOps-практик\n"
                "- Конфликты с предыдущими работодателями, нежелание работать в команде\n"
                "- Отсутствие интереса к оптимизации и мониторингу ML-систем."
            ),
            "hr_tasks": (
                "Твои задачи:\n"
                "1) Узнать опыт кандидата в CICD\n"
                "2) Узнать про реальные кейсы деплоя, сложные моменты\n"
                "3) Проверить понимание инфраструктуры и методов оптимизации\n"
                "4) Оценить готовность к обучению и гибкость в выборе инструментов\n"
                "5) Проверить командные и коммуникативные навыки."
            ),
            "keywords": [
                "jenkins", "gitlab ci", "github actions", "docker", "kubernetes",
                "aws", "gcp", "azure", "terraform", "ansible", "mlflow", "airflow", "ci/cd"
            ],
            "questions" : [

            ]
        },
        "Project Manager": {
            "intro": (
                "Ты выступаешь в роли HR-бота в компании, которая ищет Project Manager. "
                "Твоя задача – проводить первичное интервью и выяснять управленческие и коммуникационные навыки."
            ),
            "requirements": (
                "Основные требования к кандидату:\n"
                "1) Опыт ведения IT/диджитал-проектов от старта до релиза\n"
                "2) Знание гибких методологий (Scrum, Kanban) и умение настраивать процессы\n"
                "3) Работа с бэклогом, приоритизация, управление ресурсами\n"
                "4) Развитые коммуникационные навыки\n"
                "5) Бюджетирование и управление рисками."
            ),
            "red_flags": (
                "Ред-флаги:\n"
                "- Отсутствие понимания методологий управления проектами\n"
                "- Конфликты в команде, отсутствие навыков урегулирования\n"
                "- Нежелание осваивать новые инструменты\n"
                "- Завышенные ожидания без реальной практики."
            ),
            "hr_tasks": (
                "Твои задачи:\n"
                "1) Узнать, какие проекты кандидат уже вёл\n"
                "2) Проверить понимание жизненного цикла проекта\n"
                "3) Узнать, как взаимодействовал со стейкхолдерами\n"
                "4) Оценить гибкость в методологиях\n"
                "5) Проверить soft-skills: коммуникация, лидерство."
            ),
            "keywords": [
                "scrum", "kanban", "jira", "backlog", "stakeholder", "budgeting",
                "risk management", "sprint", "agile", "team management",
            ],
        },
        "Data Analyst": {
            "intro": (
                "Ты выступаешь в роли HR-бота в компании, которая ищет Data Analyst. "
                "Твоя задача – проводить первичное интервью и выяснять навыки аналитики данных."
            ),
            "requirements": (
                "Основные требования:\n"
                "1) Уверенное владение инструментами анализа (SQL, Excel, BI-платформы)\n"
                "2) Знание статистики и умение делать выводы\n"
                "3) Умение визуализировать данные и готовить отчёты\n"
                "4) Базовые навыки Python/R\n"
                "5) Понимание бизнес-процессов, умение формулировать гипотезы."
            ),
            "red_flags": (
                "Ред-флаги:\n"
                "- Отсутствие реальных кейсов анализа данных\n"
                "- Непонимание основ статистики\n"
                "- Нежелание разбираться в бизнес-контексте\n"
                "- Сложности с коммуникацией результатов."
            ),
            "hr_tasks": (
                "Твои задачи:\n"
                "1) Узнать, какие аналитические задачи кандидат уже решал\n"
                "2) Проверить знания SQL, BI\n"
                "3) Уточнить, как структурирует данные\n"
                "4) Оценить понимание бизнес-процессов\n"
                "5) Проверить умение работать в команде."
            ),
            "keywords": [
                "sql", "excel", "power bi", "tableau", "looker", "statistics",
                "python", "r ", "visualization", "business intelligence",
            ],
        },
        "Data Engineer": {
            "intro": (
                "Ты выступаешь в роли HR-бота в компании, которая ищет Data Engineer. "
                "Твоя задача – проводить первичное интервью и выяснять навыки построения дата-пайплайнов."
            ),
            "requirements": (
                "Основные требования:\n"
                "1) Опыт проектирования ETL/ELT-пайплайнов\n"
                "2) Знание облачных сервисов (AWS/GCP/Azure)\n"
                "3) Умение работать с системами потоковой обработки (Kafka, Spark)\n"
                "4) Оптимизация баз данных, работа с Data Warehouse\n"
                "5) Навыки Python/Scala/Java и оркестрация (Airflow)."
            ),
            "red_flags": (
                "Ред-флаги:\n"
                "- Отсутствие опыта с реальными пайплайнами\n"
                "- Непонимание оптимизации и масштабирования\n"
                "- Сложности с командной работой\n"
                "- Малоинтерес к новым технологиям."
            ),
            "hr_tasks": (
                "Твои задачи:\n"
                "1) Узнать опыт в построении и поддержке пайплайнов\n"
                "2) Проверить, как решал проблемы производительности\n"
                "3) Оценить знание облачных сервисов\n"
                "4) Проверить автоматизацию (Airflow, etc.)\n"
                "5) Узнать уровень командного взаимодействия."
            ),
            "keywords": [
                "etl", "elt", "aws", "gcp", "azure", "kafka", "spark",
                "data warehouse", "airflow", "scala", "java", "hadoop",
            ],
        },
        "Некомпентентный соискатель": {
            "intro": (
                "Ты нашел некомпетентного соискателя"
            ),
            "requirements": (
                "Основные требования:\n"
                "1) Малое знание технологий и однообразный ответ"
            ),
            "red_flags": (
                "Ред-флаги:\n"
                "- Противоречивые сведения об опыте\n"
                "- Слабое понимание ответов на вопросы"
            ),
            "hr_tasks": (
                "Твои задачи:\n"
                "1) Узнать опыт и число технологий, которые знает и вообще понять, знает ли что-то"
            ),
            "keywords": [
            ],
        },
            "Data Scientist": {
            "intro": (
                "Ты выступаешь в роли HR-бота в компании, которая ищет Data Scientist. "
                "Твоя задача – проводить первичное интервью и выяснять навыки построения ML-моделей."
            ),
            "requirements": (
                "Основные требования:\n"
                "1) Знания машинного обучения (регрессии, классификации, ансамбли, нейронные сети)\n"
                "2) Хорошее владение Python и ML-библиотеками\n"
                "3) Знание методов A/B-тестирования и статистических тестов\n"
                "4) Опыт работы с большими данными, оптимизация вычислений\n"
                "5) Понимание бизнес-целей, формулирование ML-задач."
            ),
            "red_flags": (
                "Ред-флаги:\n"
                "- Противоречивые сведения об опыте\n"
                "- Нежелание учиться новым подходам\n"
                "- Слабое понимание математики и статистики\n"
                "- Отсутствие интереса к бизнес-потребностям."
            ),
            "hr_tasks": (
                "Твои задачи:\n"
                "1) Узнать опыт в ML и реализованные проекты\n"
                "2) Проверить выбор архитектуры\n"
                "3) Выяснить уровень статистических знаний\n"
                "4) Оценить работу с большими данными\n"
                "5) Проверить, как адаптирует решение под бизнес."
            ),
            "keywords": [
                 "regression", "classification", "pytorch", "tensorflow",
                "pandas", "scikit-learn", "ab-test", "statistics",
                "big data", "optimization", "numpy", "matplotlib",
            ],
        },
    }
    def __init__(self):
        #self.roles_data = roles_data
        self.history = []
        self.scores = {role: 0 for role in ChatBot.roles_data}
        self.red_flags = {role: 0 for role in ChatBot.roles_data}
        self.max_questions = 8
        self.confidence = 70

        system_text = "Ты – HR-бот в компании, которая ищет сотрудников на несколько позиций:\n\n"
        for role_name, data in ChatBot.roles_data.items():
            system_text += f"=== {role_name} ===\n"
            system_text += f"{data['intro']}\n"
            system_text += f"{data['requirements']}\n"
            system_text += f"{data['red_flags']}\n"
            system_text += f"{data['hr_tasks']}\n\n"

        system_text += (
            "Мы будем анализировать его ответы и ключевые слова, чтобы определить, какая роль ему лучше подходит. "
            "Твоя задача – вести диалог как HR, задавая вопросы о навыках и опыте, "
            "учитывая всё, что описано выше.\n"
        )
        self.history.append({"role": "system", "content": system_text})

    def calculate_confidence(self, role):
        """Рассчитывает уверенность в процентах для конкретной роли"""
        max_possible = len(self.roles_data[role]['keywords']) * 3
        return min(100, int((self.scores[role] / max_possible) * 100))

    def analyze_response(self, text):
        """Анализ на основании требований и оценки от ИИ"""
        for role, data in ChatBot.roles_data.items():
            
            # Подсчет ключевых слов
            keywords_found = sum(
                1 for kw in data['keywords']
                if re.search(rf'\b{re.escape(kw)}\b', text, re.I)
            )
            self.scores[role] += keywords_found * 3

            #Оценка с помощью ИИ
            prompt = f"""
            Оцени от 0 до 5 соответствие ответа вакансии {role}:
            Ответ: {text[:500]}
            Требования: {ChatBot.roles_data[role]['requirements'][:200]}
            Если человек говорит о малом количестве технологий, то ответ должен быть 0.
            , а также на основании своего опыта в подборе на вакансии. Ответ предоставь в виде Я оцениваю кандидата на 
            """
            try:
                response, _ = mini_chat([{"role": "user", "content": prompt}])
                match = re.search(r'\d+', response)
                if match:
                    score = int(match.group())
                else:
                    score = 0
                self.scores[role] += score
            except:
                pass

    def check_early_exit(self):
        """Проверка условий для досрочного завершения"""
        for role in self.roles_data:
            if self.calculate_confidence(role) >= self.confidence:
                return role
        return None

    def generate_experience_question(self):
        """Генерация вопроса на основе предыдущих ответов"""
        last_answer = self.history[-1] if self.history else ""
        
        prompt = f"""
        Сгенерируй уточняющий вопрос о профессиональном опыте на основе ответа:
        Ответ кандидата: {last_answer}
        Вакансии: {list(self.roles_data.keys())}
        Формат: Вопрос о конкретных навыках/инструментах/реализованных задачах
        Примеры хороших вопросов:
        - "Как именно вы использовали [технологию] в этом проекте?"
        - "Можете привести пример решения проблемы с [упомянутым инструментом]?"
        - "Какие сложности возникли при реализации [упомянутой задачи]?"
        """
    
        try:
            question, _ = mini_chat([{"role": "user", "content": prompt}])
            return question
        except:
            return "Расскажите подробнее о вашем опыте работы в этой области"
    
    def answer_questions(self):
        """Переходит в режим ответов на вопросы кандидата."""
        print("Если у вас есть вопросы, пожалуйста, задайте их. Для завершения введите 'нет'.")
        while True:
            user_question = input("Ваш вопрос: ").strip()
            if user_question.lower() in ['нет', 'ничего', 'exit', 'quit']:
                print("HR-бот: Спасибо за вопросы! До свидания!")
                break
            try:
                answer, _ = mini_chat([{"role": "user", "content": user_question}])
                print(f"HR-бот: {answer}\n")
            except Exception as e:
                print(f"HR-бот: Ошибка при обработке вашего вопроса: {e}\n")

    def conduct_interview(self):
        print("HR-бот: Добрый день! Я HR-бот и готов провести с вами интервью.\n")
    
        # Первый вопрос о базовом опыте
        answer_1 = input()
        self.history.append({"role": "user", "content": answer_1})
        self.analyze_response(answer_1)

        q1 = "Расскажите о своем опыте и задачах, которые решали"
        print(q1)

        self.history.append({"role": "assistant", "content" : q1})

        answer_2 = input()
        self.history.append({"role": "user", "content": answer_2})
        self.analyze_response(answer_2)

        # Адаптивные вопросы на основе ответов
        for q in range(3, self.max_questions):
            question = self.generate_experience_question()
            print(f"\nВопрос: {question}")
            answer = input("Ваш ответ: ").strip()
            self.history.append({"role": "user", "content": answer})
            self.analyze_response(answer)
            detected_role = self.check_early_exit()
            if detected_role:
                print("\n=== Результат (досрочно) ===")
                self.show_results()
                self.answer_questions()
                return self.history
        
        # Финализация результатов
        self.show_results()

    def show_results(self):
        """Выводит итоговую рекомендацию на основе набранных баллов."""
        best_role = max(self.scores, key=self.scores.get)
        confidence = self.calculate_confidence(best_role)
        print("\n----- Итоговая оценка -----")
        if confidence >= self.confidence:
            print(f"Вакансия: [ {best_role} ]")
            print(f"Уверенность: {confidence}%")
            print("Краткое описание требований:")
            print('\n'.join(self.roles_data[best_role]['requirements'].split('\n')[:3]))
        else:
            print("Кандидат не подходит по заданным требованиям.")
            print("Рекомендуем обратить внимание на следующие вакансии:")
            for role in sorted(self.scores, key=self.scores.get, reverse=True)[:2]:
                print(f"- {role} ({self.calculate_confidence(role)}% совпадения)")
        print("--------------------------\n")
        return self.history