# Decision Report

- generated_at: 2026-10-30T01:11:25.354060+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17820**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=17820, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_BB3S | 3/16 | 18.8% | +4.42% | **+0.83%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.22% | **+0.05%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.06% | **+0.03%** |
| LIMIT_4PCT | 9/20 | 45.0% | -0.19% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.41% | **+0.35%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.10% | **+0.03%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.08% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6804件 (Win 1975 / Loss 2180 / Flat 2649) / skip 7577件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.52** / 初期 $100.00 (+263.52%)
- 確定: 4338件 (Win 1167 / Loss 980 / Flat 2191) / skip 6893件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0027 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $363.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5978件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T01:11:12.076430+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=77102.6
- Funnel: target 1086 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +68.22% | $6,567,871.08 |
| Q/USDT:USDT | +24.91% | $23,847,185.71 |
| SOXS/USDT:USDT | +20.57% | $75,605,800.65 |
| BULLA/USDT:USDT | +8.72% | $1,585,720.41 |
| BLESS/USDT:USDT | +8.49% | $14,310,033.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.07% | +3.21% |
| JCT/USDT:USDT | below_1h_threshold | +1.89% | +2.03% |
| XMR/USDT:USDT | below_1h_threshold | +1.68% | +1.82% |
| NOWSTOCK/USDT:USDT | below_1h_threshold | +0.86% | +1.00% |
| AIN/USDT:USDT | below_1h_threshold | +0.81% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
