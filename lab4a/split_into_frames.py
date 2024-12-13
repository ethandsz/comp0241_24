import cv2
import os

# Path to the video file
video_path = 'couch.mp4'  # Replace with your video file name
output_folder = 'example/couch-half/images'  # Folder to save extracted frames

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file
video = cv2.VideoCapture(video_path)

# Get the total number of frames
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Calculate the interval to pick 30 frames
interval = max(frame_count // 15, 1)

frame_index = 0
saved_frames = 0

while saved_frames < 15 and video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Save every nth frame as determined by the interval
    if frame_index % interval == 0:
        frame_filename = os.path.join(output_folder, f'{saved_frames:04d}.png')
        cv2.imwrite(frame_filename, frame)
        saved_frames += 1

    frame_index += 1

# Release the video capture object
video.release()

print(f"Extracted {saved_frames} frames to '{output_folder}'.")
