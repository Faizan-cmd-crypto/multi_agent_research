from agents import writer_chain , reader_agent , search_agent , critic_chain

def research_pipeline(topic : str) -> dict:
    
    state = {}
    
    print("\n"+"="*50)
    print("STEP 1 - SEARCH AGENT IS WORKING ....")
    print("="*50)
    
    
    searchAgent = search_agent()
    search_results = searchAgent.invoke({
        "messages" : [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    
    
    state["search_result"] = search_results["messages"][-1].content
    print("\n search result", state["search_result"])
    
    
    
    print("\n"+"="*50)
    print("STEP 2 - READER AGENT IS SCRAPING TOP RESOURCES ....")
    print("\n"+"="*50)
    
    readerAgent = reader_agent()
    reader_result = readerAgent.invoke({
        "messages" : [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_result'][:800]}")]
    })
    
    state["reader_result"] = reader_result["messages"][-1].content
    print("\n reader result", state["reader_result"])
    
    
    
    print("\n"+"="*50)
    print("STEP 3 - WRITER IS DRAFTING THE REPORT ....")
    print("\n"+"="*50)
    
    combined_research = (
        f"SEARCH RESULT : \n {state['search_result']}\n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['reader_result']}"  
    )
    
    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : combined_research
    })
    
    print("\n Final Report\n",state['report'])
    
    print("\n"+"="*50)
    print("STEP 4 - CRITIC IS REVIEWING THE REPORT ....")
    print("\n"+"="*50)
    
    state["feedback"] = critic_chain.invoke({
        "report" : state["report"]
    })
    
    print("\n critic report \n", state["feedback"])
    
    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    research_pipeline(topic)