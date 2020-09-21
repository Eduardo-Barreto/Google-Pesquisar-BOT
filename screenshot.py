import cloudconvert
import authkeys

cloudconvert.configure(api_key = authkeys.convert, sandbox = False)

def get(url):
    job = cloudconvert.Job.create(payload={
        "tasks": {
            "print": {
                "operation": "capture-website",
                "url": url,
                "output_format": "png",
                "engine": "chrome",
                "screen_width": 1440,
                "fit": "max",
                "wait_until": "load",
                "wait_time": 0,
                "filename": "screenshot.png"
            },
            "export-it": {
                "operation": "export/url",
                "input": [
                    "print"
                ],
                "inline": True,
                "archive_multiple_files": False
            }
        }
    })

    job = cloudconvert.Job.wait(id=job['id'])

    for task in job["tasks"]:
        if task.get("name") == "export-it" and task.get("status") == "finished":
            export_task = task

    file = export_task.get("result").get("files")[0]
    cloudconvert.download(filename=file['filename'], url=file['url'])