# Decision Report

- generated_at: 2026-08-05T04:11:27.315757+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10351**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10351, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/18 | 22.2% | +1.69% | **+0.37%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.24% | **+2.43%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.53% | **+1.94%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.15% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.82** / 初期 $100.00 (+503.82%)
- 確定: 3748件 (Win 1188 / Loss 1225 / Flat 1335) / skip 3164件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $603.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.53** / 初期 $100.00 (+40.53%)
- 確定: 1288件 (Win 361 / Loss 300 / Flat 627) / skip 2474件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0452 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.82** / 初期 $100.00 (+18.82%)
- 確定: 1107件 (Win 357 / Loss 426 / Flat 324) / pending 3件 / skip 716件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.82

## 6. Latest Market Context

- 更新: 2026-08-05T04:11:18.476130+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64103.6
- Funnel: target 939 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +88.04% | $9,139,232.95 |
| TAKE/USDT:USDT | +35.58% | $1,540,503.60 |
| MARSCOIN/USDT:USDT | +31.52% | $1,148,658.79 |
| CASHCAT/USDT:USDT | +30.33% | $1,172,500.64 |
| BLESS/USDT:USDT | +29.51% | $21,545,973.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.74% | +3.80% |
| SYN/USDT:USDT | below_1h_threshold | +2.97% | +3.03% |
| HFT/USDT:USDT | below_1h_threshold | +2.92% | +2.99% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.93% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.85% | +2.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
