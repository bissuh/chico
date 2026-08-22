import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {SANS} from './fonts';
import {THEME, paletteFor, REEL, reelDuration, type ThemeName} from './theme';

export {reelDuration};

export type ReelProps = {
  theme?: ThemeName;
  kicker?: string;
  lines?: string[];
  cta?: string;
  handle?: string;
};

const Texture: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        opacity: 0.05,
        mixBlendMode: 'soft-light',
        backgroundImage: `radial-gradient(circle at ${15 + (f % 20)}% ${25 + (f % 18)}%, #fff 0.5px, transparent 1.5px)`,
        backgroundSize: '7px 7px',
        pointerEvents: 'none',
      }}
    />
  );
};

export const Reel: React.FC<ReelProps> = ({
  theme = 'brand',
  kicker = '',
  lines = [],
  cta = '',
  handle = THEME.handle,
}) => {
  const c = paletteFor(theme);
  const frame = useCurrentFrame();
  const linesEnd = lines.length * REEL.framesPerLine;
  const inCta = frame >= linesEnd;
  const activeIdx = Math.min(Math.max(0, lines.length - 1), Math.floor(frame / REEL.framesPerLine));
  const local = frame - activeIdx * REEL.framesPerLine;

  const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
  const lineOpIn = interpolate(local, [0, 9], [0, 1], clamp);
  const lineOpOut = interpolate(local, [REEL.framesPerLine - 10, REEL.framesPerLine], [1, 0], clamp);
  const lineY = interpolate(local, [0, 14], [46, 0], clamp);

  const ctaLocal = frame - linesEnd;
  const ctaOp = interpolate(ctaLocal, [0, 14], [0, 1], clamp);
  const ctaScale = interpolate(ctaLocal, [0, 18], [0.86, 1], clamp);

  return (
    <AbsoluteFill style={{backgroundColor: c.bg, fontFamily: SANS}}>
      <Texture />

      <AbsoluteFill style={{padding: 90, justifyContent: 'flex-start'}}>
        {kicker ? (
          <div
            style={{
              fontFamily: SANS,
              fontWeight: 700,
              fontSize: 34,
              letterSpacing: '0.16em',
              textTransform: 'uppercase',
              color: c.accent,
            }}
          >
            {kicker}
          </div>
        ) : null}
      </AbsoluteFill>

      <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', padding: '0 96px'}}>
        {!inCta ? (
          <div
            style={{
              opacity: lineOpIn * lineOpOut,
              transform: `translateY(${lineY}px)`,
              fontFamily: SANS,
              fontWeight: 800,
              fontSize: 82,
              lineHeight: 1.08,
              letterSpacing: '-0.02em',
              color: c.ink,
              textAlign: 'center',
              maxWidth: 900,
            }}
          >
            {lines[activeIdx]}
          </div>
        ) : (
          <div style={{opacity: ctaOp, transform: `scale(${ctaScale})`, textAlign: 'center'}}>
            {THEME.logo ? (
              <Img src={staticFile(THEME.logo)} style={{height: 150, width: 'auto', marginBottom: 40}} />
            ) : null}
            <div
              style={{
                fontFamily: SANS,
                fontWeight: 800,
                fontSize: 84,
                lineHeight: 1.06,
                color: c.ink,
                letterSpacing: '-0.02em',
                maxWidth: 880,
              }}
            >
              {cta}
            </div>
          </div>
        )}
      </AbsoluteFill>

      <AbsoluteFill style={{padding: 90, justifyContent: 'flex-end', alignItems: 'center'}}>
        <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 30, color: c.sub}}>{handle}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
