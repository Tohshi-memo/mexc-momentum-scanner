# Decision Report

- generated_at: 2026-05-12T10:05:53.896432+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4109**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4109, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.50% | **+0.15%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 8/18 | 44.4% | -1.42% | **-0.63%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.69% | **-0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +3.40% | **+3.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.95% | **+1.46%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.33% | **+1.28%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.13% | **+1.07%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.43% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$114.47** / 初期 $100.00 (+14.47%)
- 確定: 245件 (Win 67 / Loss 84 / Flat 94) / skip 425件
- 成長率目線: 平均log +0.000552 / 幾何平均 +0.055% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $114.47

## 4. Latest Market Context

- 更新: 2026-05-12T10:05:50.763750+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=80744.9
- Funnel: target 762 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +63.68% | $4,565,019.26 |
| SAGA/USDT:USDT | +55.20% | $13,206,487.62 |
| USELESS/USDT:USDT | +38.21% | $7,777,539.08 |
| SKYAI/USDT:USDT | +36.92% | $43,322,069.16 |
| GUA/USDT:USDT | +28.22% | $3,281,268.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUTH/USDT:USDT | below_1h_threshold | +3.16% | +3.22% |
| GIGA/USDT:USDT | below_1h_threshold | +2.86% | +2.92% |
| SAGA/USDT:USDT | below_1h_threshold | +1.66% | +1.72% |
| AIOT/USDT:USDT | below_1h_threshold | +0.92% | +0.98% |
| NEAR/USDT:USDT | below_1h_threshold | +0.69% | +0.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
