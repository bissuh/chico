import {Composition} from 'remotion';
import {CtaVideo} from './CtaVideo';

// Edit these defaults to your brand, OR pass --props with a JSON file at render time.
export const RemotionRoot: React.FC = () => (
  <Composition
    id="Cta"
    component={CtaVideo}
    durationInFrames={180}   // 6 seconds at 30fps
    fps={30}
    width={1080}
    height={1920}
    defaultProps={{
      headline1: 'STOP SCROLLING.',
      headline2: 'START BUILDING.',
      subhead: 'One sentence. Who it is for, plus proof. Keep it short.',
      url: 'yourdomain.com',
      brandColor: '#2A4A52',
      bg1: 'bg1.png',
      bg2: 'bg2.png',
      bg3: 'bg3.png',
    }}
  />
);
