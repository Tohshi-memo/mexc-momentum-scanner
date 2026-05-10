# Decision Report

- generated_at: 2026-05-10T03:02:43.465258+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3938**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3938, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.81% | **+0.77%** |
| ASK | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.34% | **+1.17%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.33% | **+1.16%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.15% | **+0.64%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.56% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 196件 (Win 48 / Loss 66 / Flat 82) / skip 303件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T03:02:40.250514+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80740.0
- Funnel: target 769 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +29.15% | $6,145,705.88 |
| INX/USDT:USDT | +24.02% | $13,852,314.44 |
| LAYER/USDT:USDT | +23.97% | $1,097,619.08 |
| AIGENSYN/USDT:USDT | +12.63% | $1,139,284.25 |
| BIO/USDT:USDT | +12.00% | $1,567,627.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MITO/USDT:USDT | below_1h_threshold | +1.31% | +1.32% |
| SATO/USDT:USDT | below_1h_threshold | +1.21% | +1.22% |
| JTO/USDT:USDT | below_1h_threshold | +0.72% | +0.73% |
| LIT/USDT:USDT | below_1h_threshold | +0.60% | +0.61% |
| BILL/USDT:USDT | below_1h_threshold | +0.60% | +0.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
