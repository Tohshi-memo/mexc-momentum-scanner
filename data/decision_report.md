# Decision Report

- generated_at: 2026-11-26T08:41:28.398001+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19678**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.58% / filled 20/20。**
- 全期間 MARKET基準: n=19678, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.58% | **+2.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.58% | **+2.58%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.40% | **+2.28%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.28% | **+1.59%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.73% | **+1.21%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.29% | **+0.17%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.32% | **+0.05%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 289件 (TP 105 / SL 176 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.21** / 初期 $100.00 (+1888.21%)
- 確定: 7616件 (Win 2193 / Loss 2452 / Flat 2971) / skip 8623件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOR/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,988.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$465.65** / 初期 $100.00 (+365.65%)
- 確定: 5221件 (Win 1389 / Loss 1125 / Flat 2707) / skip 7868件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $465.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7841件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000062 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T08:41:14.212652+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=60700.8
- Funnel: target 1097 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +58.81% | $2,448,193.84 |
| SI/USDT:USDT | +51.85% | $1,451,367.74 |
| KOR/USDT:USDT | +40.64% | $1,842,657.10 |
| SOXL/USDT:USDT | +28.64% | $1,753,157,652.21 |
| MVLL/USDT:USDT | +22.56% | $5,070,487.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVE/USDT:USDT | below_1h_threshold | +3.56% | +3.23% |
| BULLA/USDT:USDT | below_1h_threshold | +2.20% | +1.86% |
| NVDL/USDT:USDT | below_1h_threshold | +1.47% | +1.14% |
| LIT/USDT:USDT | below_1h_threshold | +1.46% | +1.13% |
| FET/USDT:USDT | below_1h_threshold | +1.26% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
