# Decision Report

- generated_at: 2026-07-23T22:56:11.589443+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9401**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9401, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_BB3S | 3/13 | 23.1% | +1.13% | **+0.26%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.21% | **-0.17%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.31% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.45% | **+1.56%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.61% | **+1.37%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.79% | **+1.34%** |
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.22% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.48** / 初期 $100.00 (+325.48%)
- 確定: 3322件 (Win 1048 / Loss 1076 / Flat 1198) / skip 2640件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.13% 残高後 $425.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1163件 (Win 312 / Loss 254 / Flat 597) / skip 1649件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0086 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BILL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.82** / 初期 $100.00 (+1.82%)
- 確定: 463件 (Win 154 / Loss 184 / Flat 125) / pending 3件 / skip 406件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000450 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $101.82

## 6. Latest Market Context

- 更新: 2026-07-23T22:56:04.831393+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=65149.8
- Funnel: target 897 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +26.90% | $6,979,295.24 |
| AKE/USDT:USDT | +18.93% | $24,310,576.98 |
| BILL/USDT:USDT | +16.40% | $7,226,126.21 |
| ON/USDT:USDT | +13.41% | $7,098,910.63 |
| PROM/USDT:USDT | +9.57% | $2,203,038.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.12% | +4.10% |
| BILL/USDT:USDT | below_1h_threshold | +2.69% | +2.67% |
| IDOL/USDT:USDT | below_1h_threshold | +2.14% | +2.12% |
| ON/USDT:USDT | below_1h_threshold | +1.80% | +1.78% |
| B2/USDT:USDT | below_1h_threshold | +1.30% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
