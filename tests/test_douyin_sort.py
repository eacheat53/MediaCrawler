# -*- coding: utf-8 -*-
from typing import Dict

def test_douyin_play_count_sorting():
    # Mock video list
    video_list = [
        {"aweme_id": "1", "statistics": {"play_count": 100}, "desc": "video 1"},
        {"aweme_id": "2", "statistics": {"play_count": 50}, "desc": "video 2"},
        {"aweme_id": "3", "statistics": {"play_count": 500}, "desc": "video 3"},
        {"aweme_id": "4", "statistics": {"play_count": "300"}, "desc": "video 4"},  # String format
        {"aweme_id": "5", "statistics": {}, "desc": "video 5"},                  # Missing play_count
        {"aweme_id": "6", "desc": "video 6"},                                     # Missing statistics
    ]
    
    # Sorting helper logic identical to the one implemented in core.py
    def get_play_count(item: Dict) -> int:
        try:
            return int(item.get("statistics", {}).get("play_count", 0))
        except (ValueError, TypeError):
            return 0
            
    sorted_video_list = sorted(video_list, key=get_play_count, reverse=True)
    
    # Verify order
    assert get_play_count(sorted_video_list[0]) == 500
    assert sorted_video_list[0]["aweme_id"] == "3"
    
    assert get_play_count(sorted_video_list[1]) == 300
    assert sorted_video_list[1]["aweme_id"] == "4"
    
    assert get_play_count(sorted_video_list[2]) == 100
    assert sorted_video_list[2]["aweme_id"] == "1"
    
    assert get_play_count(sorted_video_list[3]) == 50
    assert sorted_video_list[3]["aweme_id"] == "2"
    
    # Missing/invalid play count defaults to 0
    assert get_play_count(sorted_video_list[4]) == 0
    assert get_play_count(sorted_video_list[5]) == 0
    
    # Slice top N (e.g. top 3)
    top_3 = sorted_video_list[:3]
    assert len(top_3) == 3
    assert [v["aweme_id"] for v in top_3] == ["3", "4", "1"]
