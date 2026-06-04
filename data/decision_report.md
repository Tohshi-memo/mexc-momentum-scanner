# Decision Report

- generated_at: 2026-06-04T04:02:40.314128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5598**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.22% / filled 20/20。**
- 全期間 MARKET基準: n=5598, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+3.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.22% | **+3.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.40% | **+3.40%** |
| MARKET | 20/20 | 100.0% | +3.22% | **+3.22%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.87% | **+2.44%** |
| LIMIT_ATR | 11/20 | 55.0% | +3.21% | **+1.76%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.65% | **+1.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.63% | **-0.22%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.62% | **-0.34%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1154件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T04:02:37.904945+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64393.0
- Funnel: target 771 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +28.38% | $24,389,517.51 |
| EPIC/USDT:USDT | +23.56% | $3,788,709.62 |
| STO/USDT:USDT | +19.47% | $7,065,446.72 |
| MAGMA/USDT:USDT | +12.69% | $4,597,578.50 |
| HEI/USDT:USDT | +11.49% | $1,016,122.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +2.67% | +2.58% |
| OPG/USDT:USDT | below_1h_threshold | +0.87% | +0.78% |
| HEI/USDT:USDT | below_1h_threshold | +0.81% | +0.72% |
| VVV/USDT:USDT | below_1h_threshold | +0.62% | +0.53% |
| ZORA/USDT:USDT | below_1h_threshold | +0.49% | +0.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
