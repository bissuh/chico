import {Composition} from 'remotion';
import {Slide} from './Slide';
import {Reel, reelDuration, type ReelProps} from './Reel';
import {SLIDE, REEL, THEME} from './theme';

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="Slide"
      component={Slide}
      durationInFrames={1}
      fps={30}
      width={SLIDE.width}
      height={SLIDE.height}
      defaultProps={{
        theme: 'brand' as const,
        layout: 'cover' as const,
        kicker: 'Kicker',
        title: 'The headline that earns the swipe',
        subtitle: 'One line of context under it.',
        slideNo: 1,
        slideTotal: 8,
        handle: THEME.handle,
      }}
    />
    <Composition
      id="Reel"
      component={Reel}
      fps={30}
      width={REEL.width}
      height={REEL.height}
      durationInFrames={reelDuration(4)}
      defaultProps={{
        theme: 'brand' as const,
        kicker: 'Kicker',
        lines: ['Line one.', 'Line two.', 'Line three.', 'Line four.'],
        cta: 'The thing in bio',
        handle: THEME.handle,
      }}
      calculateMetadata={({props}: {props: ReelProps}) => ({
        durationInFrames: reelDuration((props.lines ?? []).length),
      })}
    />
  </>
);
