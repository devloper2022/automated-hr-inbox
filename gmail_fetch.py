import base64
import os

def fetch_emails_and_download(service, save_dir="resumes", query="has:attachment"):
    os.makedirs(save_dir, exist_ok=True)
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    files = []

    for msg in messages:
        msg_id = msg['id']
        message = service.users().messages().get(userId='me', id=msg_id).execute()
        parts = message['payload'].get('parts', [])
        for part in parts:
            if part.get('filename') and part['filename'] != '':
                if 'attachmentId' in part['body']:
                    att_id = part['body']['attachmentId']
                    att = service.users().messages().attachments().get(
                        userId='me', messageId=msg_id, id=att_id
                    ).execute()
                    data = base64.urlsafe_b64decode(att['data'])
                    file_path = os.path.join(save_dir, part['filename'])
                    with open(file_path, 'wb') as f:
                        f.write(data)
                    files.append(file_path)
                    print(f"Downloaded {file_path}")
    return files
