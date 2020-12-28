import json
import boto3

def lambda_handler(event, context):
    
    StreamARN = 'arn:aws:kinesisvideo:us-east-1:841622902378:stream/AmazonRekognition_user_live_feed/1608478703022'
    api_name = 'GET_HLS_STREAMING_SESSION_URL'
    end_pt = "https://b-61687957.kinesisvideo.us-east-1.amazonaws.com"
    kvm = boto3.client('kinesis-video-archived-media',endpoint_url = end_pt) 
    response = kvm.get_hls_streaming_session_url(
        StreamARN=StreamARN,
        PlaybackMode='LIVE',
        HLSFragmentSelector={
            'FragmentSelectorType': 'PRODUCER_TIMESTAMP'#'SERVER_TIMESTAMP' # Producer is important as it skips lost frames --discontinuity-mode  NEVER
            },
        ContainerFormat='FRAGMENTED_MP4',
        DiscontinuityMode='NEVER',
        DisplayFragmentTimestamp='ALWAYS',
        Expires=3600,
        MaxMediaPlaylistFragmentResults=5
    )

    # TODO implement
    return {
        'statusCode': 200,
        'body': response["HLSStreamingSessionURL"]
    }
