essay = input("Please type your essay below that needs to be checked.\n\n").split()

ai_words = ["delve","delving","utilize","utilizing","leverage","leveraging","facilitate","facilitating","robust","comprehensive","streamline","streamlining","outline","outlining","optimize","optimizing","enhance","enhancing","framework","paradigm","scalable","scaling","synergy","holistic","innovative","cutting-edge","state-of-the-art","seamless","dynamic","efficient","significant","notably","substantial","moreover","furthermore","additionally","conclude","concluding","overall","ultimately","consequently","aforementioned","therein","thereby","herein","methodology","implement","implementing","implementation","infrastructure","solution-oriented","data-driven","best-practice","takeaway","noting","explore","exploring","aim","aiming","various","aspects","range","factors","high-level","low-level","end-to-end"]

human_words = ["look into","looking into","use","using","build on","building on","help","helping","strong","complete","simplify","simplifying","plan","planning","improve","improving","make better","making better","basic structure","idea","can grow","growing","working together","overall","new","modern","current","smooth","changing","works well","important","worth noticing","large","also","on top of that","and","wrap up","wrapping up","in general","in the end","as a result","mentioned earlier","there","because of that","here","method","do","doing","how it was done","system","goal-focused","based on data","common approach","main point","mentioning","look at","looking at","try","trying","different","parts","amount","reasons","big picture","small details","from start to finish"]

#checks if there is a ai word 
for word in essay:
    clean_word = word.lower().strip(".,!?;:'()[]")
    if clean_word in ai_words:
        print("AI word found! --> ", word)

        
#convert those ai words into human-like words
for i in range(len(essay)):
    w = essay[i].lower().strip(".,!?;:'s()[]")#makes sure there is no punctuation before/after a word so its easier to find the ai word
    if w in ai_words:
        essay[i] = human_words[ai_words.index(w)].capitalize()#each index value in human_words cooresponds to each index value in ai_words


print("NEW ESSAY: \n")
print(" ".join(essay))#join the essay back together so it doesnt appear like its a list.
