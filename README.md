# mishmash-hackathon-2020
Automatic cognitive information retrieval of educational text data
The present-day e-learning system is dependent on the instructor for the design and allocation of learning materials to the learner. This may often come as a hindrance and can be subject to bias, as often, the specific cognitive knowledge of the learner is not considered as a factor that can determine the success or failure of the learner. This is because the information present in the learning materials is mostly identified based on the topics, and less importance is given about the information structure. E.g., Newton's law of motion is not explained in the same way in a graduate-level textbook as it is in a middle school textbook. Considering the abundance of online learning materials that are available for a present-day learner, the challenge is how to identify the cognitive suitability of the information based on the query. An information retrieval problem is dependent on three pivots - (i) the query, (ii) the retrieved information, and (iii) the relevance of the retrieved information with the given query. Putting these three pivots on the context of education, they become (i) the learning objective, (ii) the learning materials, and (iii) the relevance of learning materials with the given objective. As the text is a significant format of learning materials (textbooks), the objective is to extract the information structure present in the text. If the information structure can be classified into groups or patterns such as Fact, Comparison, Summary, Analysis, etc. based on natural language processing, the cognitive information relevance of the text can be measured against a given query. Thus, information extraction will no longer be dependent only on keywords but also on the information structure that is present.  So it becomes a problem of cognitive information retrieval from educational data mining. The advantage of this method will be that it will no longer be dependent on Human expertise to select the appropriate learning material. Instead, the system itself will be able to analyze documents and provide a recommended list based on the relevance of the cognitive information structure present in the text content. For scalability purposes, only text is being considered as of now. The dataset will be the NCERT dataset (available freely from NCERT site). The Microsoft Azure service that will be used is Text Analytics (https://azure.microsoft.com/en-in/services/cognitive-services/text-analytics/).
