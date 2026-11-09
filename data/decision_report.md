# Decision Report

- generated_at: 2026-11-09T11:31:14.055265+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18518**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=18518, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.62% | **+1.13%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.91% | **+1.02%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.82% | **+1.64%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.11% | **+1.55%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +1.94% | **+1.55%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.30% | **+1.49%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.60% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,626.14** / 初期 $100.00 (+1526.14%)
- 確定: 7162件 (Win 2057 / Loss 2285 / Flat 2820) / skip 7917件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,626.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4757件 (Win 1277 / Loss 1047 / Flat 2433) / skip 7172件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0622 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6680件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000237 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-09T11:31:05.084703+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.48% price=74483.8
- Funnel: target 1089 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +42.40% | $1,653,302.79 |
| RITUAL/USDT:USDT | +27.10% | $1,535,979.16 |
| PIEVERSE/USDT:USDT | +16.24% | $1,468,977.64 |
| ANSEM/USDT:USDT | +10.42% | $1,145,908.06 |
| IDOL/USDT:USDT | +9.77% | $2,814,410.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RITUAL/USDT:USDT | below_1h_threshold | +3.47% | +2.99% |
| USELESS/USDT:USDT | below_1h_threshold | +3.26% | +2.78% |
| ON/USDT:USDT | below_1h_threshold | +2.54% | +2.05% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.47% | +1.98% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.37% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
