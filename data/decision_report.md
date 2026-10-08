# Decision Report

- generated_at: 2026-10-08T04:01:26.188276+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16309**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=16309, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/16 | 31.2% | +4.41% | **+1.38%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.29% | **+1.16%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.35% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +0.59% | **+0.30%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.63% | **+0.25%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.29% | **+0.23%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.12** / 初期 $100.00 (+21.12%)
- 確定トレード: 234件 (TP 86 / SL 141 / EXP 7)
- 最新: LONGXIA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,322.43** / 初期 $100.00 (+1222.43%)
- 確定: 6278件 (Win 1845 / Loss 2011 / Flat 2422) / skip 6592件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORCA/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,322.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6088件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4470件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000288 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-08T04:01:14.624289+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=82729.7
- Funnel: target 1073 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MET/USDT:USDT | +42.98% | $12,229,055.48 |
| W/USDT:USDT | +24.09% | $2,204,248.72 |
| JUP/USDT:USDT | +18.08% | $20,709,548.64 |
| BSPSTOCK/USDT:USDT | +17.85% | $1,096,460.98 |
| ACE/USDT:USDT | +14.33% | $1,896,537.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +0.35% | +0.33% |
| JUP/USDT:USDT | below_1h_threshold | +0.32% | +0.31% |
| PONS/USDT:USDT | below_1h_threshold | +0.26% | +0.24% |
| TIA/USDT:USDT | below_1h_threshold | +0.23% | +0.21% |
| ORDI/USDT:USDT | below_1h_threshold | +0.20% | +0.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
