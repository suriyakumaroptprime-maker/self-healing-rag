from retrievers.fusion_retriever import FusionRetriever


dense_results = {

    "documents": [[

        "Artificial Intelligence",

        "Machine Learning"
    ]],

    "distances": [[

        0.1,

        0.3
    ]]
}


bm25_results = [

    ("Artificial Intelligence", 12),

    ("FAISS", 20)
]


fusion = FusionRetriever()

results = fusion.fuse(
    dense_results,
    bm25_results
)

for doc, score in results:

    print(doc)
    print(score)
    print("-" * 50)