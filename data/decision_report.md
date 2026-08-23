# Decision Report

- generated_at: 2026-08-23T05:06:23.435858+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12443**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=12443, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.74% | **+1.39%** |
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.98% | **+0.64%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.45% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.32% | **+1.06%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.88% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.71% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$706.07** / 初期 $100.00 (+606.07%)
- 確定: 4470件 (Win 1368 / Loss 1462 / Flat 1640) / skip 4534件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGI/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $706.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3919件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0113 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2052件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000111 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T05:06:14.354904+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=76582.1
- Funnel: target 1018 → liquid 200 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +34.87% | $51,176,814.77 |
| AGI/USDT:USDT | +21.27% | $1,023,229.54 |
| ZRO/USDT:USDT | +11.87% | $11,362,683.93 |
| UAI/USDT:USDT | +10.78% | $3,436,561.93 |
| BTW/USDT:USDT | +8.38% | $31,120,031.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGI/USDT:USDT | below_1h_threshold | +2.52% | +2.55% |
| TUT/USDT:USDT | below_1h_threshold | +1.94% | +1.98% |
| CYS/USDT:USDT | below_1h_threshold | +1.17% | +1.20% |
| HEI/USDT:USDT | below_1h_threshold | +1.15% | +1.18% |
| PEPE/USDT:USDT | below_1h_threshold | +1.02% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
