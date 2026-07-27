# Decision Report

- generated_at: 2026-07-27T13:21:17.967954+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9630**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9630, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.71% | **+1.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.76% | **+0.72%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +3.31% | **+2.84%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.63% | **+1.84%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.74% | **+1.78%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.14% | **+1.57%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 145件 (TP 50 / SL 90 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.92
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$456.85** / 初期 $100.00 (+356.85%)
- 確定: 3421件 (Win 1084 / Loss 1114 / Flat 1223) / skip 2770件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $456.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1818件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0017 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.64** / 初期 $100.00 (+8.64%)
- 確定: 652件 (Win 216 / Loss 247 / Flat 189) / pending 3件 / skip 445件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000436 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.64

## 6. Latest Market Context

- 更新: 2026-07-27T13:21:11.121985+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=65003.8
- Funnel: target 902 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +54.58% | $6,179,014.32 |
| AKE/USDT:USDT | +48.43% | $44,209,043.08 |
| ON/USDT:USDT | +42.07% | $7,282,799.86 |
| NIL/USDT:USDT | +22.84% | $3,966,975.78 |
| DIA/USDT:USDT | +22.14% | $10,916,171.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +1.89% | +1.99% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +1.75% | +1.84% |
| US/USDT:USDT | below_1h_threshold | +1.14% | +1.23% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.61% | +0.71% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.55% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
