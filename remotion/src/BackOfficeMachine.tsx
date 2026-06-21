import {AbsoluteFill, Img, staticFile} from 'remotion';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';

const {fontFamily: INTER} = loadInter();

const C = {
  bg: '#2A7A6D',
  ink: '#FFFFFF',
  sub: 'rgba(255,255,255,0.85)',
  accent: '#CFEFE7',
  line: 'rgba(255,255,255,0.22)',
  card: 'rgba(255,255,255,0.10)',
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

const Arrow: React.FC = () => (
  <svg width="64" height="40" viewBox="0 0 64 40" style={{flexShrink: 0}}>
    <path d="M2 20 H50" stroke={C.accent} strokeWidth={4} fill="none" strokeLinecap="round" />
    <path d="M44 8 L60 20 L44 32" stroke={C.accent} strokeWidth={4} fill="none" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

const Stage: React.FC<{n: string; tag: string; name: string; hook: string; highlight?: boolean}> = ({n, tag, name, hook, highlight}) => (
  <div
    style={{
      flex: 1,
      display: 'flex',
      flexDirection: 'column',
      padding: '38px 34px',
      borderRadius: 24,
      background: highlight ? 'rgba(255,255,255,0.17)' : C.card,
      border: `${highlight ? 3 : 2}px solid ${highlight ? C.accent : C.line}`,
      minHeight: 372,
    }}
  >
    <div style={{display: 'flex', alignItems: 'center', gap: 16}}>
      <div
        style={{
          width: 54,
          height: 54,
          borderRadius: 27,
          flexShrink: 0,
          background: highlight ? C.accent : 'transparent',
          border: `3px solid ${C.accent}`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontFamily: INTER,
          fontWeight: 800,
          fontSize: 27,
          color: highlight ? C.bg : C.accent,
        }}
      >
        {n}
      </div>
      <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 21, letterSpacing: '0.13em', textTransform: 'uppercase', color: C.accent}}>{tag}</div>
    </div>
    <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 54, color: C.ink, letterSpacing: '-0.01em', marginTop: 26, lineHeight: 1.0}}>{name}</div>
    <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 29, color: C.sub, marginTop: 18, lineHeight: 1.32}}>{hook}</div>
  </div>
);

export const BackOfficeMachine: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, fontFamily: INTER}}>
      <Texture />
      <AbsoluteFill style={{padding: 96, display: 'flex', flexDirection: 'column'}}>
        {/* header */}
        <div>
          <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 26, letterSpacing: '0.18em', textTransform: 'uppercase', color: C.accent}}>The shape that repeats</div>
          <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 84, color: C.ink, lineHeight: 1.0, letterSpacing: '-0.02em', marginTop: 12}}>
            The back-office machine
          </div>
          <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 34, color: C.sub, marginTop: 16}}>
            Getting paid and keeping the books run on the same three moves.
          </div>
        </div>

        {/* three stages + arrows */}
        <div style={{flex: 1, display: 'flex', alignItems: 'center', gap: 20, marginTop: 6}}>
          <Stage n="1" tag="Messy input" name="The mess" hook="A rough note. A bank transaction. A job marked done." />
          <Arrow />
          <Stage n="2" tag="The AI" name="The glue" hook="Claude reads the mess, structures it, writes the output. The new part." highlight />
          <Arrow />
          <Stage n="3" tag="The tool" name="The muscle" hook="Stripe sends and chases. QuickBooks logs and reports." />
        </div>

        {/* outcome strip */}
        <div style={{display: 'flex', justifyContent: 'center', marginTop: 4, marginBottom: 2}}>
          <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 29, letterSpacing: '0.06em', color: C.bg, background: C.accent, padding: '13px 32px', borderRadius: 30}}>
            PAID. RECONCILED. HANDS OFF.
          </div>
        </div>

        {/* footer */}
        <div style={{paddingTop: 24, borderTop: `2px solid ${C.line}`, display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
          <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 32, color: C.ink}}>
            You approve. The machine does the typing.
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
