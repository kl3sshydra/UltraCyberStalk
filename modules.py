from googlesearch import search
import utils
import threading
import requests

url_list = []

class dork:
    depth = 0
    def processurls_dork(query):
            for j in search(query, tld="co.in", num=dork.depth, stop=dork.depth):
                if dork.shouldprinturl(j):
                    utils.betterprint(j)
                    url_list.append(j)
    def shouldprinturl(j):
        for x in url_list:
            if x == j:
                return False
        return True
    def setdepth(self):
        f = open("CONFIG/dorksdepth.txt", "w")
        f.write(input("Insert dorking depth: "))
        f.close()
    def dorkingmodule(self, mode):
        url_list = []
        utils.set_target()
        target = open("CONFIG/target.txt", "r").readline()
        depth = 30
        if mode == "normal":
            try:
                depth = int(input("Max urls per request: "))
            except:
                pass
        else:
            try:
                depth = int(open("CONFIG/dorksdepth.txt", "r").readline())
            except Exception as e:
                print(e)
                exit()
                depth = 30
        dork.depth = depth
        utils.betterprint(f"Using the dork module against '{target}' with depth {str(depth)}..")
        for line in open("CONFIG/dorks.txt","r").readlines():
            exec(f"dork.processurls_dork(f\"{line.strip()}\")")
    def main(self, mode):
        dork.dorkingmodule(self, mode)

class instagrambio:
    def searchmybio(query):
        r = requests.get(f"https://www.searchmy.bio/search?q={query}")
        result = r.text.split("const initial_results = '[")[1].split("]';")[0].split('],"username":"')
        for x in range(len(result)-1):
            user = result[x+1].split('","')[0]
            followers = result[x].split('","followers_count":')[1].split(',')[0]
            utils.betterprint(f"Matching bio with username: '{user}' -> followers: {followers}")

    def main(self):
        target = open("CONFIG/target.txt", "r").readline()
        utils.betterprint(f"Using instagrambio against '{target}'..")
        try:
            instagrambio.searchmybio(target)
        except IndexError:
            utils.betterprint("No result found with instagrambio module")

class usernamesearch:
    def searchusername(url):
        try:
            domain = url.split("https://")[1].split("/")[0]
            r = requests.get(url, headers={"Accept-Language": "en-US,en;q=0.5", 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'})
            for line in open("CONFIG/usernamesearchresults.txt", "r").readlines():
                line = line.strip()
                if domain == line.split(' :: ')[0]:
                    if line.split(f"{domain} :: ")[1].startswith("CONTENT"):
                        utils.betterprint(str(line.split(f"{domain} :: ")[1].split(" :: ")[1] in r.text).replace("False", f"Target found at -> {url}").replace("True", f"Target ·NOT· found at -> {url}"))
                    if line.split(f"{domain} :: ")[1].startswith("STATUSCODE"):
                        utils.betterprint(str(line.split("STATUSCODE :: ")[1] == str(r.status_code)).replace("False", f"Target found at -> {url}").replace("True", f"Target ·NOT· found at -> {url}"))

                    break
        except KeyboardInterrupt:
                return

    def main(self):
        utils.set_target()
        target = open("CONFIG/target.txt", "r").readline()
        utils.betterprint(f"Searching '{target}'..")
        if " " in target:
            utils.betterprint("Skipping the usernamesearchmodule as the target contains spaces")
        else:
            for line in open("CONFIG/usernamesearch.txt", "r").readlines():
                try:
                    exec("threading.Thread(target=usernamesearch.searchusername, args=(line.strip().replace('{target}','"+target+"'),)).start()")
                except KeyboardInterrupt:
                    break

class peoplesearch:
    def radaris(name):
        r = requests.get(name)
        try:
            found = r.text.split('<p class="narrow-normal-small pft-top-text">')[1].split("</span>")[0].replace("<span>", "")
        except:
            found = f"No pepole found for '{name}' in the US using radaris"
        utils.betterprint(f"---\n{name} -> \n{found}\n---")

    def paginebianche(nome, citta):
        if citta == "no_city_specified":
            citta = "italia"
        url = f'https://www.paginebianche.it/ricerca?qs={nome.replace(" ", "%20")}&dv={citta}'
        r = requests.get(url)
        linksfound = r.text.split('<a href="')
        if len(linksfound) == 16:
            return 0
        count = 0
        validlinks = 0
        for l in linksfound:
            if l.startswith("https://www.paginebianche.it/") and '"><svg' not in l and "localita.html" not in l and "ricerca?qs" not in l:
                utils.betterprint("PagineBianche -> "+l.split('" title="')[0])
                validlinks+=1 
            count+=1
        return validlinks

    def paginegialle(nome, citta):
        if citta == "no_city_specified":
            citta = "italia"
        url = f'https://www.paginegialle.it/ricerca/{nome.replace(" ", "%20")}/{citta}'
        r = requests.get(url)
        linksfound = r.text.split("href=\"")
        foundlist = []
        if len(linksfound) == 306:
            return 0
        for l in linksfound:
            l = l.split("\">")[0]
            if l.startswith("https://www.paginegialle.it/") and 'rel="nofollow' not in l and "/ricerca/" not in l and nome.split(" ")[0] in l:
                try:
                    l = l.split('" title="')[0].split("\n")[0]
                    if l not in foundlist and "/commenti" not in l and "-timetable" not in l:
                        utils.betterprint("PagineGialle -> "+l)
                        foundlist.append(l)
                except:
                    pass

    def peopledorks():
        dorklist = ["paginebianche {target}", "paginegialle {target}"]
        for d in dorklist:
            for j in search(d, tld="co.in", num=15, stop=15):
                if dork.shouldprinturl(j) and ("pagine" in j and ("gialle" in j or "bianche" in j)):
                    utils.betterprint(f"---\nPeopleSearch dorks -> \n{j}\n---")
                    url_list.append(j)

    def main(self):
        target = utils.currenttarget()
        query = f"https://radaris.com/p/{target.replace(' ', '/')}/"
        utils.betterprint(f"Starting peoplesearch against '{target}'")
        peoplesearch.radaris(query)
        peoplesearch.peopledorks()
        pbianche = peoplesearch.paginebianche(target, utils.gettargetlocation())
        if pbianche == 0:
            utils.betterprint("No people found with paginebianche module.")
        pgialle = peoplesearch.paginegialle(target, utils.gettargetlocation())
        if pgialle == 0:
            utils.betterprint("No companies found with paginegialle module")