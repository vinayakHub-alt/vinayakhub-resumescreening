import networkx as nx

def compute_centrality(candidates, hr_prompt):
    """
    Builds a bipartite graph of candidates ↔ skills ↔ job
    and calculates centrality-based scores.
    """
    if not candidates:
        return candidates

    # Create an undirected graph
    G = nx.Graph()

    # Add job requirement as a node (if exists)
    job_skills = [s.strip().lower() for s in hr_prompt.split(",")] if hr_prompt else []

    # Add nodes and edges for candidates and their skills
    for cand in candidates:
        cand_name = cand["name"]
        skill_list = [s.strip().lower() for s in cand["skills"].split(",") if s.strip()]
        G.add_node(cand_name, type="candidate")

        for skill in skill_list:
            G.add_node(skill, type="skill")
            G.add_edge(cand_name, skill)

    # Add edges between job prompt and skills
    for skill in job_skills:
        if skill not in G:
            G.add_node(skill, type="skill")
        G.add_edge("JOB_REQUIREMENT", skill)

    # Compute degree centrality (you can also try betweenness or closeness)
    centrality = nx.degree_centrality(G)

    # Update candidate scores
    for cand in candidates:
        cand_name = cand["name"]
        # score = candidate’s centrality + avg of their skill centralities
        cand_skills = [s.strip().lower() for s in cand["skills"].split(",") if s.strip()]
        skill_centralities = [centrality.get(s, 0) for s in cand_skills]
        avg_skill_score = sum(skill_centralities) / len(skill_centralities) if skill_centralities else 0
        cand["score"] = round((centrality.get(cand_name, 0) + avg_skill_score) * 100, 2)

    return candidates


def quick_sort(candidates):
    if len(candidates) <= 1:
        return candidates
    pivot = candidates[0]
    left = [x for x in candidates[1:] if x["score"] >= pivot["score"]]
    right = [x for x in candidates[1:] if x["score"] < pivot["score"]]
    return quick_sort(left) + [pivot] + quick_sort(right)


def greedy_select(candidates, job_skills, k=5):
    shortlist = []
    for c in candidates:
        matches = sum([1 for s in job_skills if s.lower() in c["skills"].lower()])
        if matches > 0:
            shortlist.append(c)
        if len(shortlist) >= k:
            break
    return shortlist
