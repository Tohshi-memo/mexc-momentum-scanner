# Decision Report

- generated_at: 2026-11-04T13:56:29.324013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18121**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=18121, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.78% | **+0.39%** |
| LIMIT_BB3S | 8/18 | 44.4% | +0.83% | **+0.37%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.35% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.74% | **+0.74%** |
| MARKET_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.22% | **+0.08%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,510.20** / 初期 $100.00 (+1410.20%)
- 確定: 6940件 (Win 2006 / Loss 2224 / Flat 2710) / skip 7742件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,510.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$372.27** / 初期 $100.00 (+272.27%)
- 確定: 4532件 (Win 1213 / Loss 1016 / Flat 2303) / skip 7000件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $372.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6283件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000099 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T13:56:13.628823+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=78362.7
- Funnel: target 1078 → liquid 182 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +35.42% | $4,699,306.90 |
| CLANKER/USDT:USDT | +34.90% | $4,701,353.62 |
| BMT/USDT:USDT | +14.41% | $1,880,353.57 |
| IDOL/USDT:USDT | +12.82% | $8,752,005.39 |
| LSK/USDT:USDT | +11.61% | $5,020,371.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLANKER/USDT:USDT | below_1h_threshold | +4.26% | +4.15% |
| BTW/USDT:USDT | below_1h_threshold | +4.16% | +4.05% |
| Q/USDT:USDT | below_1h_threshold | +3.51% | +3.39% |
| ALGO/USDT:USDT | below_1h_threshold | +2.60% | +2.49% |
| FLUID/USDT:USDT | below_1h_threshold | +2.27% | +2.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
