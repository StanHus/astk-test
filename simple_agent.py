#!/usr/bin/env python3
"""
Simple AI Agent for testing with ASTK (Agent Sprint TestKit)
This agent provides basic responses to various types of questions and scenarios.
"""

import sys
import re
import json
import random
from datetime import datetime


class SimpleAgent:
    def __init__(self):
        self.name = "SimpleAgent"
        self.version = "1.0.0"

    def respond(self, question):
        """Generate a response based on the input question"""
        question = question.strip().lower()

        # Handle different types of questions
        if self._is_math_question(question):
            return self._handle_math(question)
        elif self._is_reasoning_question(question):
            return self._handle_reasoning(question)
        elif self._is_creativity_question(question):
            return self._handle_creativity(question)
        elif self._is_ethics_question(question):
            return self._handle_ethics(question)
        elif self._is_technical_question(question):
            return self._handle_technical(question)
        elif self._is_analysis_question(question):
            return self._handle_analysis(question)
        else:
            return self._handle_general(question)

    def _is_math_question(self, question):
        """Check if the question involves mathematical calculations"""
        math_keywords = ['calculate', 'compute', 'solve',
                         '+', '-', '*', '/', 'math', 'equation']
        return any(keyword in question for keyword in math_keywords)

    def _is_reasoning_question(self, question):
        """Check if the question requires logical reasoning"""
        reasoning_keywords = ['analyze', 'compare', 'evaluate',
                              'reasoning', 'logic', 'problem', 'solution', 'strategy']
        return any(keyword in question for keyword in reasoning_keywords)

    def _is_creativity_question(self, question):
        """Check if the question requires creative thinking"""
        creative_keywords = ['design', 'create', 'innovative',
                             'creative', 'brainstorm', 'idea', 'invent']
        return any(keyword in question for keyword in creative_keywords)

    def _is_ethics_question(self, question):
        """Check if the question involves ethical considerations"""
        ethics_keywords = ['ethical', 'moral', 'bias', 'fair',
                           'responsible', 'privacy', 'gdpr', 'compliance']
        return any(keyword in question for keyword in ethics_keywords)

    def _is_technical_question(self, question):
        """Check if the question is technical in nature"""
        tech_keywords = ['code', 'programming', 'algorithm',
                         'database', 'api', 'architecture', 'performance', 'security']
        return any(keyword in question for keyword in tech_keywords)

    def _is_analysis_question(self, question):
        """Check if the question requires analysis"""
        analysis_keywords = ['market', 'competitive',
                             'analysis', 'trend', 'forecast', 'quantum', 'future']
        return any(keyword in question for keyword in analysis_keywords)

    def _handle_math(self, question):
        """Handle mathematical questions"""
        # Simple math parsing for basic operations
        numbers = re.findall(r'\d+(?:\.\d+)?', question)
        if len(numbers) >= 2:
            try:
                a, b = float(numbers[0]), float(numbers[1])
                if '+' in question:
                    result = a + b
                    return f"Agent: The sum of {a} and {b} is {result}. This calculation involves basic arithmetic addition."
                elif '-' in question:
                    result = a - b
                    return f"Agent: The difference between {a} and {b} is {result}. This subtraction shows the numerical gap."
                elif '*' in question or 'multiply' in question:
                    result = a * b
                    return f"Agent: The product of {a} and {b} is {result}. Multiplication scales one number by another."
                elif '/' in question or 'divide' in question:
                    if b != 0:
                        result = a / b
                        return f"Agent: {a} divided by {b} equals {result}. This division shows the ratio between the numbers."
                    else:
                        return "Agent: Division by zero is undefined in mathematics. Please provide a non-zero divisor."
            except:
                pass

        return "Agent: I can help with mathematical calculations. Please provide specific numbers and operations (+, -, *, /) for accurate results."

    def _handle_reasoning(self, question):
        """Handle questions requiring logical reasoning"""
        responses = [
            "Agent: To approach this problem systematically, I would first identify the key variables and constraints. Then, I'd analyze the relationships between different components and evaluate potential solutions based on their feasibility and impact.",
            "Agent: This requires multi-step reasoning. I would break down the problem into smaller, manageable parts, analyze each component individually, and then synthesize the findings to reach a comprehensive solution.",
            "Agent: For complex reasoning tasks, I employ a structured approach: 1) Problem definition, 2) Data gathering, 3) Analysis of alternatives, 4) Risk assessment, 5) Implementation planning, and 6) Evaluation criteria."
        ]
        return random.choice(responses)

    def _handle_creativity(self, question):
        """Handle creative and innovative questions"""
        if 'design' in question:
            return "Agent: For innovative design, I would focus on user-centered principles, incorporating modern UX/UI best practices, accessibility standards, and scalable architecture. The design should be intuitive, responsive, and future-proof with modular components."
        elif 'feature' in question:
            return "Agent: When creating new features, I consider user needs, technical feasibility, business value, and implementation complexity. The feature should integrate seamlessly with existing systems while providing clear value proposition."
        else:
            return "Agent: Creative problem-solving involves thinking outside conventional boundaries, combining different perspectives, and iterating on ideas. I would explore multiple approaches, prototype rapidly, and gather feedback for continuous improvement."

    def _handle_ethics(self, question):
        """Handle ethical and compliance questions"""
        if 'bias' in question:
            return "Agent: AI bias can be mitigated through diverse training data, regular auditing, fairness metrics, and inclusive development teams. It's crucial to test for demographic parity, equalized odds, and individual fairness across different user groups."
        elif 'privacy' in question or 'gdpr' in question:
            return "Agent: Privacy compliance requires implementing data minimization, purpose limitation, consent management, and user rights (access, rectification, deletion). GDPR compliance involves privacy by design, impact assessments, and proper documentation."
        else:
            return "Agent: Ethical AI development requires transparency, accountability, fairness, and human oversight. We must consider societal impact, ensure responsible deployment, and maintain human agency in decision-making processes."

    def _handle_technical(self, question):
        """Handle technical programming and architecture questions"""
        if 'performance' in question:
            return "Agent: Performance optimization involves profiling bottlenecks, implementing caching strategies, optimizing database queries, using CDNs, and employing lazy loading. Consider horizontal scaling, load balancing, and asynchronous processing for high-traffic applications."
        elif 'security' in question:
            return "Agent: Security best practices include input validation, authentication/authorization, HTTPS encryption, regular updates, secure coding practices, and vulnerability assessments. Implement defense in depth with multiple security layers."
        elif 'architecture' in question:
            return "Agent: Scalable architecture should follow microservices patterns, implement proper separation of concerns, use message queues for async processing, and design for fault tolerance. Consider containerization, API gateways, and database sharding."
        else:
            return "Agent: Technical solutions should prioritize maintainability, scalability, and performance. Use established design patterns, follow coding standards, implement comprehensive testing, and document APIs thoroughly."

    def _handle_analysis(self, question):
        """Handle analytical and strategic questions"""
        if 'market' in question or 'competitive' in question:
            return "Agent: Market analysis involves studying industry trends, competitor positioning, customer segments, and value propositions. Key metrics include market size, growth rate, customer acquisition costs, and competitive advantages."
        elif 'quantum' in question:
            return "Agent: Quantum computing represents a paradigm shift in computational capabilities. Organizations should prepare by understanding quantum algorithms, investing in quantum-safe cryptography, and exploring quantum advantage use cases in optimization and simulation."
        else:
            return "Agent: Strategic analysis requires examining internal capabilities, external market forces, stakeholder interests, and future scenarios. Use frameworks like SWOT, Porter's Five Forces, and scenario planning for comprehensive insights."

    def _handle_general(self, question):
        """Handle general questions"""
        general_responses = [
            f"Agent: Thank you for your question. Based on my analysis, I would approach this by considering multiple perspectives and providing a well-reasoned response that addresses the core aspects of your inquiry.",
            f"Agent: I understand your question and can provide insights. Let me break this down systematically to give you a comprehensive and helpful response.",
            f"Agent: This is an interesting question that requires careful consideration. I'll provide a thoughtful analysis based on best practices and logical reasoning."
        ]

        response = random.choice(general_responses)

        # Add some context about the current interaction
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response += f" [Response generated at {timestamp}]"

        return response


def main():
    """Main function to handle command-line arguments"""
    if len(sys.argv) < 2:
        print("Agent: Hello! I'm a Simple AI Agent ready to help. Please ask me a question as a command-line argument.")
        print("Usage: python simple_agent.py 'Your question here'")
        return

    # Join all arguments after the script name to form the question
    question = " ".join(sys.argv[1:])

    # Create agent instance and generate response
    agent = SimpleAgent()
    response = agent.respond(question)

    # Print the response
    print(response)


if __name__ == "__main__":
    main()
