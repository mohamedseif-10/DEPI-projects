import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re

# Load data
data = pd.read_csv("final_cleaned_version.csv", encoding="utf-8")
data["song_time"] = data["song_time"].str.replace("1900-01-01 ", "")


# Functions for extracting song name and artist
def song_artist(entry):
    match = re.match(r"(.+)\s*-\s*(.+)", entry)
    if match:
        song_name = match.group(1).strip()
        artist_name = match.group(2).strip()
        return song_name, artist_name
    return None, None


def calculate_avg_time():
    data["song_time"] = pd.to_datetime(data["song_time"], format="%H:%M:%S")
    avg_time = data["song_time"].mean().strftime("%H:%M:%S")
    return avg_time


# Group data for playlists
grouped_playlist_data = data.groupby("playlist_ID").agg(
    {
        "num_artists": "first",
        "num_followers": "first",
        "num_edits": "first",
        "playlist_length": "first",
        "playlist_name": "first",
        "collaborative": "first",
        "num_tracks": "first",
        "num_albums": "first",
        "modified_at": "first",
    }
)

# Streamlit page layout
st.title("Spotify Playlist Analysis Dashboard")
st.sidebar.title("Spotify Playlist Analysis Dashboard by MS")
st.sidebar.header("Filters and Options")

# Sliders for top items
top_n_artists = st.sidebar.slider("Number of Top Artists to Display", 1, 20, 10)
top_n_songs = st.sidebar.slider("Number of Top Songs to Display", 1, 20, 10)
top_n_albums = st.sidebar.slider("Number of Top Albums to Display", 1, 20, 10)
top_n_playlists = st.sidebar.slider("Number of Top Playlists to Display", 1, 20, 10)

# Dropdown for year selection
year = st.sidebar.selectbox(
    "Select Year for Modifications Analysis", [2014, 2015, 2016, 2017]
)

cutoff_date = f"{year}-01-01"

# Filter data for top songs and artists
top_songs_data = data["song_artist"].value_counts().head(top_n_songs)
top_artists_data = data["artist"].value_counts().head(top_n_artists)
top_albums_data = data["album"].value_counts().head(top_n_albums)
top_playlists_data = grouped_playlist_data.sort_values(
    by="num_followers", ascending=False
).head(top_n_playlists)

# Bar chart for Top Artists
st.subheader("Top Artists")
fig_top_artists = px.bar(
    top_artists_data,
    x=top_artists_data.index,
    y=top_artists_data.values,
    labels={"x": "Artist", "y": "Count"},
    title="Top Artists",
)
st.plotly_chart(fig_top_artists)

# Bar chart for Top Songs
st.subheader("Top Songs")
fig_top_songs = px.bar(
    top_songs_data,
    x=top_songs_data.index,
    y=top_songs_data.values,
    labels={"x": "Song - Artist", "y": "Count"},
    title="Top Songs",
)
st.plotly_chart(fig_top_songs)

# Bar chart for Top Albums
st.subheader("Top Albums")
fig_top_albums = px.bar(
    top_albums_data,
    x=top_albums_data.index,
    y=top_albums_data.values,
    labels={"x": "Album", "y": "Count"},
    title="Top Albums",
)
st.plotly_chart(fig_top_albums)

# Bar chart for Top Playlists
st.subheader("Top Playlists")
fig_top_playlists = px.bar(
    top_playlists_data,
    x=top_playlists_data["playlist_name"],
    y=top_playlists_data["num_followers"],
    labels={"x": "Playlist", "y": "Followers"},
    title="Top Playlists",
)
st.plotly_chart(fig_top_playlists)

# Add correlation plot between Artists and Followers
st.subheader("Correlation between Artists and Followers")
fig_corr = px.scatter(
    grouped_playlist_data,
    x="num_artists",
    y="num_followers",
    title="Correlation between Artists and Followers",
)
st.plotly_chart(fig_corr)

# Static summary statistics for demonstration
total_number_of_playlists = 60000
total_number_of_U_songs = 371539
number_of_listened_songs = 3959349
avg_listening_time = number_of_listened_songs / total_number_of_U_songs

# Data for pie chart
after_year = grouped_playlist_data.loc[
    grouped_playlist_data["modified_at"] > cutoff_date
].copy()
before_year = grouped_playlist_data.loc[
    grouped_playlist_data["modified_at"] <= cutoff_date
].copy()


def modifications_per_year(df, cutoff_date):
    df["modified_year"] = pd.to_datetime(df["modified_at"]).dt.year
    start_date = pd.to_datetime(cutoff_date)
    years_range = range(df["modified_year"].min(), df["modified_year"].max() + 1)
    return len(df) / len(years_range) if years_range else 0


modifications_per_year_after = modifications_per_year(after_year, cutoff_date)
modifications_per_year_before = modifications_per_year(before_year, "2000-01-01")

labels = ["Modifications After " + str(year), "Modifications Before " + str(year)]
sizes = [modifications_per_year_after, modifications_per_year_before]
colors = ["#003f5c", "#ffa600"]
explode = (0.1, 0)

# Create pie chart using Plotly
fig_pie = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=sizes,
            hole=0.3,
            marker=dict(colors=colors),
            textinfo="label+percent",
            pull=explode,
        )
    ]
)
fig_pie.update_layout(
    title_text=f"Ratio of Modifications Per Year for Playlists Modified After and Before {year}"
)

# Display the pie chart
st.subheader(
    f"Ratio of Modifications Per Year for Playlists Modified After and Before {year}"
)
st.plotly_chart(fig_pie)


st.subheader("Statistics Summary")
st.write(f"Total number of playlists: {total_number_of_playlists}")
st.write(f"Number of unique songs: {total_number_of_U_songs}")
st.write(f"Total number of songs across all playlists: {number_of_listened_songs}")
st.write(f"Average number of playlists per track: {round(avg_listening_time)}")

# Show the top song duration and average song time
top_duration = data["song_time"].value_counts().head(1)
st.write(
    f"Top duration song is: {top_duration.index[0]} for {top_duration.values[0]} listens"
)
st.write(f"Average duration of a song is: {calculate_avg_time()}")

# Display the top artist, album, song, and playlist
topA = data["artist"].value_counts()
st.write(f"Top artist listened to is: '{topA.index[0]}' with {topA.values[0]} listens")

top_album = data["album"].value_counts()
st.write(
    f"Top album listened to is: '{top_album.index[0]}' with {top_album.values[0]} listens"
)

top_song = data["song_artist"].value_counts()
top_song_name, top_song_artist = song_artist(top_song.index[0])
st.write(
    f"Top song listened to is: {top_song_name} by {top_song_artist} with {top_song.values[0]} listens"
)

top_playlist = data.sort_values(by="num_followers", ascending=False).iloc[0]
st.write(
    f"Top playlist is: '{top_playlist['playlist_name']}' with {top_playlist['num_followers']} followers"
)
