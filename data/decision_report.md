# Decision Report

- generated_at: 2026-05-25T02:24:11.651386+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4839**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=4839, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.80% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.17% | **+0.08%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.36% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.63% | **+0.44%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.27% | **+0.16%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.34% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.40** / 初期 $100.00 (+22.40%)
- 確定: 645件 (Win 159 / Loss 206 / Flat 280) / skip 755件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $122.40

## 4. Latest Market Context

- 更新: 2026-05-25T02:24:09.493293+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=77194.7
- Funnel: target 764 → liquid 112 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +14.40% | $1,134,491.31 |
| SUPER/USDT:USDT | +5.25% | $3,419,307.66 |
| EDU/USDT:USDT | +4.67% | $1,054,858.16 |
| BEAT/USDT:USDT | +4.58% | $38,793,757.01 |
| AGT/USDT:USDT | +4.11% | $7,256,326.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +3.21% | +2.83% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.69% | +1.32% |
| SPORTFUN/USDT:USDT | below_1h_threshold | +1.51% | +1.13% |
| ONDO/USDT:USDT | below_1h_threshold | +1.48% | +1.10% |
| DASH/USDT:USDT | below_1h_threshold | +1.23% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
