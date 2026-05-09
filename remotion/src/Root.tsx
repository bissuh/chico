import {Composition} from 'remotion';
import {TBPCta} from './Composition';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="TBPCta"
        component={TBPCta}
        durationInFrames={180}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          headline1: 'STOP SCROLLING.',
          headline2: 'START BUILDING.',
          subhead: 'Start a business with AI. Join 4,000 people.',
          url: 'thebillionperson.com',
          bg1: 'bg1.png',
          bg2: 'bg2.png',
          bg3: 'bg3.png',
        }}
      />
    </>
  );
};
