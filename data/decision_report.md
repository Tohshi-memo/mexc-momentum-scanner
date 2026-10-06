# Decision Report

- generated_at: 2026-10-06T21:31:28.803161+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16254**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=16254, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.22% | **+0.08%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.04% | **-0.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.15% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 232件 (TP 84 / SL 141 / EXP 7)
- 最新: BEAT/USDT:USDT TP_HIT PnL +3.87% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,322.43** / 初期 $100.00 (+1222.43%)
- 確定: 6274件 (Win 1845 / Loss 2011 / Flat 2418) / skip 6541件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,322.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6033件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0519 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4416件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000338 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T21:31:17.496584+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=85538.0
- Funnel: target 1074 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +48.94% | $4,846,603.11 |
| ORCA/USDT:USDT | +13.81% | $7,653,045.68 |
| CHIP/USDT:USDT | +5.68% | $2,396,791.06 |
| EDU/USDT:USDT | +3.55% | $1,305,361.18 |
| INJ/USDT:USDT | +3.38% | $23,160,724.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +2.24% | +2.29% |
| BTW/USDT:USDT | below_1h_threshold | +1.22% | +1.26% |
| RAY/USDT:USDT | below_1h_threshold | +1.21% | +1.25% |
| HNT/USDT:USDT | below_1h_threshold | +1.20% | +1.24% |
| ENA/USDT:USDT | below_1h_threshold | +0.99% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
