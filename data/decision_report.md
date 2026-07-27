# Decision Report

- generated_at: 2026-07-27T20:41:25.856452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9650**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9650, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.11% | **-0.09%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.16% | **-0.10%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +4.20% | **+2.10%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.69% | **+0.84%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.13% | **+0.74%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.56% | **+0.55%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.76% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$105.86** / 初期 $100.00 (+5.86%)
- 確定トレード: 147件 (TP 50 / SL 92 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.86
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$461.56** / 初期 $100.00 (+361.56%)
- 確定: 3434件 (Win 1088 / Loss 1118 / Flat 1228) / skip 2777件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: QBTSSTOCK/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $461.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1837件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0089 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.80** / 初期 $100.00 (+8.80%)
- 確定: 670件 (Win 220 / Loss 254 / Flat 196) / pending 3件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.80

## 6. Latest Market Context

- 更新: 2026-07-27T20:41:18.886790+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64921.4
- Funnel: target 902 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LA/USDT:USDT | +36.08% | $4,166,207.45 |
| RIF/USDT:USDT | +26.89% | $6,205,034.68 |
| AEON1/USDT:USDT | +15.55% | $1,629,138.47 |
| SOONNETWORK/USDT:USDT | +15.08% | $1,099,210.85 |
| JIMOTHY/USDT:USDT | +10.01% | $1,980,645.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QBTSSTOCK/USDT:USDT | below_1h_threshold | +4.29% | +4.34% |
| ALLO/USDT:USDT | below_1h_threshold | +3.12% | +3.18% |
| BANK/USDT:USDT | below_1h_threshold | +3.09% | +3.15% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +3.01% | +3.06% |
| KORU/USDT:USDT | below_1h_threshold | +2.81% | +2.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
