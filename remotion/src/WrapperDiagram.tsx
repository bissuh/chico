import {AbsoluteFill, Img, staticFile} from 'remotion';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';

const {fontFamily: INTER} = loadInter();

const C = {
  bg: '#2A7A6D',
  ink: '#FFFFFF',
  sub: 'rgba(255,255,255,0.85)',
  accent: '#CFEFE7',
  line: 'rgba(255,255,255,0.24)',
  card: 'rgba(255,255,255,0.10)',
  dim: 'rgba(255,255,255,0.45)',
};

const Texture: React.FC = () => (
  <AbsoluteFill
    style={{
      opacity: 0.06,
      mixBlendMode: 'soft-light',
      backgroundImage: `radial-gradient(circle at 15% 25%, #fff 0.5px, transparent 1.5px)`,
      backgroundSize: '6px 6px',
      pointerEvents: 'none',
    }}
  />
);

// Concentric "wrapper": the AI is a tiny dim commodity core; the value is the rings around it.
const Rings: React.FC = () => {
  const cx = 340;
  const cy = 340;
  return (
    <svg width="640" height="680" viewBox="0 0 680 680" style={{flexShrink: 0}}>
      {/* outer ring: audience (brightest = most valuable) */}
      <circle cx={cx} cy={cy} r={300} fill="rgba(255,255,255,0.15)" stroke={C.accent} strokeWidth={3} />
      {/* middle ring: problem */}
      <circle cx={cx} cy={cy} r={208} fill="rgba(255,255,255,0.10)" stroke={C.accent} strokeWidth={2.5} />
      {/* center: the AI, small + dim + dashed (cheap commodity) */}
      <circle cx={cx} cy={cy} r={96} fill="rgba(255,255,255,0.05)" stroke={C.line} strokeWidth={2} strokeDasharray="7 7" />
      <text x={cx} y={cy - 6} textAnchor="middle" style={{fontFamily: INTER, fontWeight: 800, fontSize: 36, fill: C.dim}}>AI</text>
      <text x={cx} y={cy + 30} textAnchor="middle" style={{fontFamily: INTER, fontWeight: 600, fontSize: 24, fill: C.dim}}>$30/mo</text>
      {/* ring labels at 12 o'clock */}
      <text x={cx} y={cy - 150} textAnchor="middle" style={{fontFamily: INTER, fontWeight: 800, fontSize: 25, fill: C.ink, letterSpacing: 2}}>THE PROBLEM</text>
      <text x={cx} y={cy - 245} textAnchor="middle" style={{fontFamily: INTER, fontWeight: 800, fontSize: 25, fill: C.ink, letterSpacing: 2}}>THE AUDIENCE</text>
    </svg>
  );
};

const Row: React.FC<{name: string; hook: string; dim?: boolean}> = ({name, hook, dim}) => (
  <div>
    <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 44, color: dim ? C.dim : C.ink, lineHeight: 1.0, letterSpacing: '-0.01em'}}>{name}</div>
    <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 28, color: C.sub, marginTop: 8}}>{hook}</div>
  </div>
);

export const WrapperDiagram: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, fontFamily: INTER}}>
      <Texture />
      <AbsoluteFill style={{padding: 96, display: 'flex', flexDirection: 'column'}}>
        <div>
          <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 26, letterSpacing: '0.18em', textTransform: 'uppercase', color: C.accent}}>The reframe</div>
          <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 86, color: C.ink, lineHeight: 1.0, letterSpacing: '-0.02em', marginTop: 12}}>
            The AI is the cheap part
          </div>
          <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 34, color: C.sub, marginTop: 16}}>
            The wrapper around it is the actual business.
          </div>
        </div>

        <div style={{flex: 1, display: 'flex', alignItems: 'center', gap: 70}}>
          <Rings />
          <div style={{flex: 1, display: 'flex', flexDirection: 'column', gap: 40}}>
            <Row name="The AI" hook="$30/mo. A commodity. Identical for you and every rival." dim />
            <Row name="A problem you understand" hook="Free. Your real edge. Scratch your own itch." />
            <Row name="An audience that trusts you" hook="The moat. Months to build, so you start it today." />
          </div>
        </div>

        <div style={{paddingTop: 28, borderTop: `2px solid ${C.line}`, display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
          <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 32, color: C.ink}}>
            Everyone fights over the center. The money is in the wrapper.
          </div>
          <div style={{display: 'flex', alignItems: 'center', gap: 14, opacity: 0.9}}>
            <Img src={staticFile('logo-b.png')} style={{height: 42, width: 'auto'}} />
            <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 26, color: C.sub}}>@thebillionperson</div>
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
