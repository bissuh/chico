import {Composition} from 'remotion';
import {TBPCta} from './Composition';
import {PreCtaGoogle, PRE_CTA_DURATION} from './PreCtaGoogle';
import {CarouselSlide} from './CarouselSlide';
import {CleanSlide} from './CleanSlide';
import {GreenReel, reelDuration} from './GreenReel';
import {TriangleScorecard} from './TriangleScorecard';
import {MoatsDiagram} from './MoatsDiagram';
import {BackOfficeMachine} from './BackOfficeMachine';
import {WrapperDiagram} from './WrapperDiagram';
import {ProofStrip} from './ProofStrip';
import {ValidationChart} from './ValidationChart';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="TriangleScorecard"
        component={TriangleScorecard}
        durationInFrames={1}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="MoatsDiagram"
        component={MoatsDiagram}
        durationInFrames={1}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="BackOfficeMachine"
        component={BackOfficeMachine}
        durationInFrames={1}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="WrapperDiagram"
        component={WrapperDiagram}
        durationInFrames={1}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="ProofStrip"
        component={ProofStrip}
        durationInFrames={1}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="ValidationChart"
        component={ValidationChart}
        durationInFrames={1}
        fps={30}
        width={1920}
        height={1080}
      />
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
          cta: '5 free prompts in bio',
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
          subhead: 'Get the 5 free prompts. Link in bio.',
          url: 'join.thebillionperson.com',
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
