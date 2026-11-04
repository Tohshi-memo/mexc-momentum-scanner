# Decision Report

- generated_at: 2026-11-04T06:51:40.669196+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18110**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.54% / filled 20/20。**
- 全期間 MARKET基準: n=18110, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.54% | **+2.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.54% | **+2.54%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.12% | **+1.48%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.58% | **+1.03%** |
| LIMIT_BB3S | 7/19 | 36.8% | +2.27% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.07% | **-0.04%** |
| MARKET_LONG | 20/20 | 100.0% | -0.56% | **-0.56%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.35% | **-0.59%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,506.22** / 初期 $100.00 (+1406.22%)
- 確定: 6929件 (Win 2004 / Loss 2222 / Flat 2703) / skip 7742件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,506.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$375.61** / 初期 $100.00 (+275.61%)
- 確定: 4524件 (Win 1211 / Loss 1011 / Flat 2302) / skip 6997件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $375.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6273件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T06:51:24.079249+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=77984.2
- Funnel: target 1085 → liquid 177 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.9 >= 65=1, 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +35.59% | $2,657,683.51 |
| BMT/USDT:USDT | +23.07% | $1,526,108.45 |
| USELESS/USDT:USDT | +10.91% | $2,499,851.16 |
| LSK/USDT:USDT | +10.01% | $2,288,314.25 |
| EVAA/USDT:USDT | +8.09% | $3,859,821.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +4.95% | +4.61% |
| BMT/USDT:USDT | below_1h_threshold | +4.77% | +4.43% |
| USELESS/USDT:USDT | below_1h_threshold | +4.75% | +4.41% |
| GRASS/USDT:USDT | below_1h_threshold | +3.34% | +3.00% |
| DNA/USDT:USDT | below_1h_threshold | +3.15% | +2.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
