# Decision Report

- generated_at: 2026-10-24T06:26:13.000574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17341**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=17341, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.16% | **+1.10%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.00% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.34% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,329.29** / 初期 $100.00 (+1229.29%)
- 確定: 6594件 (Win 1909 / Loss 2101 / Flat 2584) / skip 7308件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BMT/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.35% 残高後 $1,329.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6823件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1190 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5500件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000339 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T06:26:03.599225+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80739.0
- Funnel: target 1088 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +82.24% | $1,709,428.63 |
| BIRB/USDT:USDT | +63.91% | $9,236,360.21 |
| IRYS/USDT:USDT | +36.04% | $102,550,545.08 |
| AXIS/USDT:USDT | +25.09% | $2,836,093.02 |
| AGT/USDT:USDT | +9.46% | $9,718,600.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXIS/USDT:USDT | below_1h_threshold | +4.43% | +4.42% |
| AGT/USDT:USDT | below_1h_threshold | +1.32% | +1.32% |
| DOS/USDT:USDT | below_1h_threshold | +0.86% | +0.85% |
| NIL/USDT:USDT | below_1h_threshold | +0.73% | +0.73% |
| IRYS/USDT:USDT | below_1h_threshold | +0.62% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
