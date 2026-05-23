import {AbsoluteFill, useCurrentFrame, interpolate, Img, staticFile} from 'remotion';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';

const {fontFamily: INTER} = loadInter();

const GREEN = '#2A7A6D';
const MINT = '#CFEFE7';

export const REEL_PER_LINE = 66;
export const REEL_CTA_HOLD = 102;
export const reelDuration = (n: number) => n * REEL_PER_LINE + REEL_CTA_HOLD;

export type GreenReelProps = {
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

export const GreenReel: React.FC<GreenReelProps> = ({
  kicker = 'Hot Take',
  lines = [],
  cta = 'Free playbook in bio',
  handle = '@thebillionperson',
}) => {
  const frame = useCurrentFrame();
  const linesEnd = lines.length * REEL_PER_LINE;
  const inCta = frame >= linesEnd;
  const activeIdx = Math.min(lines.length - 1, Math.floor(frame / REEL_PER_LINE));
  const local = frame - activeIdx * REEL_PER_LINE;

  // current line animation (fade/slide in, fade out at end of its window)
  const lineOpIn = interpolate(local, [0, 9], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const lineOpOut = interpolate(local, [REEL_PER_LINE - 10, REEL_PER_LINE], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const lineY = interpolate(local, [0, 14], [46, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

  // cta animation
  const ctaLocal = frame - linesEnd;
  const ctaOp = interpolate(ctaLocal, [0, 14], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const ctaScale = interpolate(ctaLocal, [0, 18], [0.86, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{backgroundColor: GREEN, fontFamily: INTER}}>
      <Texture />

      {/* top kicker */}
      <AbsoluteFill style={{padding: 90, justifyContent: 'flex-start'}}>
        <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 34, letterSpacing: '0.16em', textTransform: 'uppercase', color: MINT}}>
          {kicker}
        </div>
      </AbsoluteFill>

      {/* center: current line or cta */}
      <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', padding: '0 96px'}}>
        {!inCta ? (
          <div
            style={{
              opacity: lineOpIn * lineOpOut,
              transform: `translateY(${lineY}px)`,
              fontFamily: INTER,
              fontWeight: 800,
              fontSize: 82,
              lineHeight: 1.08,
              letterSpacing: '-0.02em',
              color: '#FFFFFF',
              textAlign: 'center',
              maxWidth: 900,
            }}
          >
            {lines[activeIdx]}
          </div>
        ) : (
          <div style={{opacity: ctaOp, transform: `scale(${ctaScale})`, textAlign: 'center'}}>
            <Img src={staticFile('logo-b.png')} style={{height: 150, width: 'auto', marginBottom: 40}} />
            <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 84, lineHeight: 1.06, color: '#FFFFFF', letterSpacing: '-0.02em', maxWidth: 880}}>
              {cta}
            </div>
          </div>
        )}
      </AbsoluteFill>

      {/* persistent bottom handle */}
      <AbsoluteFill style={{padding: 90, justifyContent: 'flex-end', alignItems: 'center'}}>
        <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 30, color: 'rgba(255,255,255,0.85)'}}>{handle}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
