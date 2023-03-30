class BrowserHistory:
    def __init__(self, homepage: str):
        # 'homepage' is the first visited URL.
        self.visited_URLs = [homepage]
        self.curr_URL, self.last_URL = 0, 0

    def visit(self, url: str) -> None:
        self.curr_URL += 1
        if len(self.visited_URLs) > self.curr_URL:
            # We have enough space in our array to overwrite an old 'url' entry with new one.
            self.visited_URLs[self.curr_URL] = url
        else:
            # We have to insert a new 'url' entry at the end.
            self.visited_URLs.append(url)
        # This 'url' will be last URL if we try to go forward.
        self.last_URL = self.curr_URL

    def back(self, steps: int) -> str:
        # Move 'curr_URL' pointer in left direction.
        self.curr_URL = max(0, self.curr_URL - steps)
        return self.visited_URLs[self.curr_URL]

    def forward(self, steps: int) -> str:
        # Move 'curr_URL' pointer in right direction.
        self.curr_URL = min(self.last_URL, self.curr_URL + steps)
        return self.visited_URLs[self.curr_URL]


browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       # You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     # You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      # You are in "facebook.com". Visit "youtube.com"
print(browserHistory.back(1)=='facebook.com')                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
print(browserHistory.back(1)=="google.com")                   # You are in "facebook.com", move back to "google.com" return "google.com"
print(browserHistory.forward(1)=="facebook.com")                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com")     # You are in "facebook.com". Visit "linkedin.com"
print(browserHistory.forward(2)=="linkedin.com")                # You are in "linkedin.com", you cannot move forward any steps.
print(browserHistory.back(2)=='google.com')                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
print(browserHistory.back(7)=="leetcode.com")                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

