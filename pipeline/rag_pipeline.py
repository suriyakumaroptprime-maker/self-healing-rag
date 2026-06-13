from agents.query_agent import QueryAgent
from agents.memory_agent import MemoryAgent
from agents.planner_agent import PlannerAgent
from agents.retriever_agent import RetrieverAgent
from agents.generator_agent import GeneratorAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.repair_agent import RepairAgent
from agents.citation_agent import CitationAgent


class RAGPipeline:

    def __init__(self):

        self.query_agent = QueryAgent()

        self.memory_agent = MemoryAgent()

        self.planner_agent = PlannerAgent()

        self.retriever_agent = RetrieverAgent()

        self.generator_agent = GeneratorAgent()

        self.evaluator_agent = EvaluatorAgent()

        self.repair_agent = RepairAgent()

        self.citation_agent = CitationAgent()

    def run(
        self,
        query: str
    ):

        query_info = (
            self.query_agent.process(
                query
            )
        )

        cleaned_query = (
            query_info["cleaned_query"]
        )

        intent = (
            query_info["intent"]
        )

        memory_context = (
            self.memory_agent
            .get_long_term_context(
                cleaned_query
            )
        )

        plan = (
            self.planner_agent
            .create_plan(
                query=cleaned_query,
                intent=intent
            )
        )

        top_k = (
            plan["top_k"]
        )

        retrieval_results = (
            self.retriever_agent
            .retrieve(
                query=cleaned_query,
                top_k=top_k
            )
        )

        retrieved_documents = [

            doc

            for doc, score

            in retrieval_results[
                "documents"
            ]
        ]

        retrieved_metadata = (
            retrieval_results[
                "metadatas"
            ]
        )

        combined_context = (
            retrieved_documents
            +
            memory_context
        )

        answer = (
            self.generator_agent
            .generate(
                query=cleaned_query,
                documents=combined_context
            )
        )

        evaluation = (
            self.evaluator_agent
            .evaluate(
                query=cleaned_query,
                documents=combined_context,
                answer=answer
            )
        )

        repaired = False

        if (
            evaluation["confidence"]
            <
            0.75
        ):

            repaired = True

            rewritten_query = (
                self.repair_agent
                .rewrite_query(
                    cleaned_query
                )
            )

            retrieval_results = (
                self.retriever_agent
                .retrieve(
                    query=rewritten_query,
                    top_k=top_k
                )
            )

            retrieved_documents = [

                doc

                for doc, score

                in retrieval_results[
                    "documents"
                ]
            ]

            answer = (
                self.generator_agent
                .generate(
                    query=rewritten_query,
                    documents=retrieved_documents
                )
            )

            cleaned_query = (
                rewritten_query
            )

        final_answer = (
            self.citation_agent
            .add_citations(
                answer=answer,
                metadatas=retrieved_metadata
            )
        )

        self.memory_agent.add_interaction(
            user_message=query,
            assistant_message=answer
        )

        return {

            "answer":
                final_answer,

            "confidence":
                evaluation[
                    "confidence"
                ],

            "intent":
                intent,

            "query_used":
                cleaned_query,

            "repaired":
                repaired,

            "retrieved_docs":
                len(
                    retrieved_documents
                )
        }