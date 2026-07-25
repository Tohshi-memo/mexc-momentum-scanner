# Decision Report

- generated_at: 2026-07-25T04:11:14.674070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9481**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9481, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |
| LIMIT_BB3S | 4/20 | 20.0% | +1.11% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.19% | **+1.09%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.05% | **+1.00%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.01% | **+0.81%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.23% | **+0.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.11% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$423.36** / 初期 $100.00 (+323.36%)
- 確定: 3326件 (Win 1048 / Loss 1077 / Flat 1201) / skip 2716件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $423.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1727件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0950 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$104.51** / 初期 $100.00 (+4.51%)
- 確定: 532件 (Win 177 / Loss 208 / Flat 147) / pending 2件 / skip 416件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000281 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $104.51

## 6. Latest Market Context

- 更新: 2026-07-25T04:11:06.593952+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64097.8
- Funnel: target 898 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +67.93% | $51,225,824.63 |
| EUL/USDT:USDT | +22.41% | $1,039,618.49 |
| SLX/USDT:USDT | +13.89% | $2,499,824.80 |
| ACE/USDT:USDT | +12.18% | $9,772,173.72 |
| ZAMA/USDT:USDT | +11.27% | $3,109,851.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEXE/USDT:USDT | below_1h_threshold | +3.12% | +3.05% |
| PROM/USDT:USDT | below_1h_threshold | +1.99% | +1.92% |
| PONS/USDT:USDT | below_1h_threshold | +1.67% | +1.60% |
| LAB/USDT:USDT | below_1h_threshold | +1.63% | +1.56% |
| VELVET/USDT:USDT | below_1h_threshold | +0.82% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
