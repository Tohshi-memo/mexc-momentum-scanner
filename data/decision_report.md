# Decision Report

- generated_at: 2026-06-03T22:34:45.398809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5582**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.98% / filled 20/20。**
- 全期間 MARKET基準: n=5582, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |
| ASK | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_BB3S | 2/11 | 18.2% | +5.06% | **+0.92%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.86% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +2.67% | **+1.49%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.71% | **+0.64%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.45% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1139件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T22:34:43.240971+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.83% price=65195.0
- Funnel: target 767 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +49.66% | $18,184,198.20 |
| STO/USDT:USDT | +22.86% | $6,197,804.57 |
| BP/USDT:USDT | +15.22% | $1,515,970.53 |
| LIT/USDT:USDT | +9.10% | $8,652,150.65 |
| MAGMA/USDT:USDT | +7.71% | $4,126,541.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.90% | +5.73% |
| LAB/USDT:USDT | below_1h_threshold | +3.10% | +3.93% |
| BP/USDT:USDT | below_1h_threshold | +1.80% | +2.63% |
| STO/USDT:USDT | below_1h_threshold | +1.15% | +1.97% |
| HYPE/USDT:USDT | below_1h_threshold | +0.77% | +1.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
