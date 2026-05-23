import {Composition} from 'remotion';
import {TBPCta} from './Composition';
import {PreCtaGoogle, PRE_CTA_DURATION} from './PreCtaGoogle';
import {CarouselSlide} from './CarouselSlide';
import {CleanSlide} from './CleanSlide';
import {GreenReel, reelDuration} from './GreenReel';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="CleanSlide"
        component={CleanSlide}
        durationInFrames={1}
        fps={30}
        width={1080}
        height={1350}
        defaultProps={{
          theme: 'dark' as const,
          layout: 'cover' as const,
          kicker: 'Editorial',
          title: 'Top AI tools',
          handle: '@thebillionperson',
          slideNo: 1,
          slideTotal: 6,
        }}
      />
      <Composition
        id="GreenReel"
        component={GreenReel}
        fps={30}
        width={1080}
        height={1920}
        durationInFrames={reelDuration(4)}
        defaultProps={{
          kicker: 'Hot Take Friday',
          lines: [
            'Hot take: you don’t need an audience to make your first $1,000 online.',
            'You need one offer and 10 real conversations.',
            'Audience is what you build after the first sale, not before.',
            'Stop posting into the void. Solve one person’s problem for money.',
          ],
          cta: 'Free playbook in bio',
          handle: '@thebillionperson',
        }}
        calculateMetadata={({props}) => ({
          durationInFrames: reelDuration(Math.max(1, (props.lines ?? []).length)),
        })}
      />
      <Composition
        id="CarouselSlide"
        component={CarouselSlide}
        durationInFrames={1}
        fps={30}
        width={1080}
        height={1350}
        defaultProps={{
          bg: 'bg1.png',
          slideNo: 1,
          slideTotal: 8,
          kicker: 'Faceless playbook',
          headline: 'YOU DON’T NEED A FACE TO WIN ONLINE',
          handle: '@thebillionperson',
        }}
      />
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
      <Composition
        id="PreCtaGoogle"
        component={PreCtaGoogle}
        durationInFrames={PRE_CTA_DURATION}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
