from modules.api_crawler import ApiCrawler
from modules.gif_generator import GifGenerator
from modules.file_handler import FileHandler

MAX_THRESHOLD = 5
FILE_NAME = "comment_analysis.json"

if __name__ == "__main__":
    #Modular Programming
    handler = FileHandler()
    crawler = ApiCrawler()
    generator = GifGenerator() # or GraphGenerator() etc

    # 1. Get Comments from videos
    fpath = f"src/{FILE_NAME}"
    videos = handler.get_videos(fpath)
    comments = crawler.get_comments(videos) # or get_thumbnail, get_livechat etc

    # 2. Do grouping by threshold
    groups = generator.grouping(comments, threshold=MAX_THRESHOLD)
    
    # 3. Generate gifs
    result = generator.generate(groups)
    handler.save_gif(result)

