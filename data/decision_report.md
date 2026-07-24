# Decision Report

- generated_at: 2026-07-24T10:11:15.760999+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9429**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9429, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.07% | **+0.72%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.20% | **+0.12%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.04% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.96% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.09% | **+0.44%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.22% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3324件 (Win 1048 / Loss 1076 / Flat 1200) / skip 2666件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1164件 (Win 312 / Loss 254 / Flat 598) / skip 1676件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1419 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$103.04** / 初期 $100.00 (+3.04%)
- 確定: 490件 (Win 163 / Loss 192 / Flat 135) / pending 4件 / skip 406件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000460 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $103.04

## 6. Latest Market Context

- 更新: 2026-07-24T10:11:09.051403+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=65046.0
- Funnel: target 897 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +32.50% | $11,725,087.87 |
| RE/USDT:USDT | +22.72% | $19,792,271.29 |
| ON/USDT:USDT | +18.39% | $6,055,383.07 |
| AKE/USDT:USDT | +18.29% | $32,610,131.55 |
| CAP/USDT:USDT | +16.60% | $1,166,717.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +2.02% | +2.08% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.91% | +1.98% |
| US/USDT:USDT | below_1h_threshold | +1.55% | +1.62% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.50% | +1.56% |
| CBRSSTOCK/USDT:USDT | below_1h_threshold | +1.06% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
