# Decision Report

- generated_at: 2026-05-04T15:32:44.726404+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3227**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3227, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.39% | **-1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.86% | **+1.40%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.62% | **+1.21%** |
| LIMIT_6PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.98% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.05% | **+2.43%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +6.62% | **+1.65%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +6.40% | **+1.60%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T15:32:42.505937+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.88% price=79467.1
- Funnel: target 761 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELIZAOS/USDT:USDT | +133.56% | $1,656,859.84 |
| SKYAI/USDT:USDT | +86.34% | $90,479,645.94 |
| TST/USDT:USDT | +75.07% | $18,822,669.81 |
| GIGA/USDT:USDT | +39.72% | $2,310,419.24 |
| ASTEROID/USDT:USDT | +33.27% | $4,736,686.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +4.00% | +4.88% |
| ELIZAOS/USDT:USDT | below_1h_threshold | +3.96% | +4.84% |
| BSB/USDT:USDT | below_1h_threshold | +3.87% | +4.75% |
| LAB/USDT:USDT | below_1h_threshold | +3.77% | +4.64% |
| TAG/USDT:USDT | below_1h_threshold | +3.26% | +4.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
