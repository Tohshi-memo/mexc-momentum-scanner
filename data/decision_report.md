# Decision Report

- generated_at: 2026-11-04T06:36:35.574192+00:00
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
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6271件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T06:36:19.727392+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=77981.4
- Funnel: target 1085 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +37.91% | $2,562,426.58 |
| BMT/USDT:USDT | +26.36% | $1,496,854.66 |
| LSK/USDT:USDT | +11.07% | $2,251,512.36 |
| USELESS/USDT:USDT | +9.27% | $2,422,282.08 |
| AXIS/USDT:USDT | +7.83% | $1,404,550.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +4.95% | +4.61% |
| VVV/USDT:USDT | below_1h_threshold | +3.50% | +3.16% |
| USELESS/USDT:USDT | below_1h_threshold | +3.20% | +2.86% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.43% | +2.10% |
| DNA/USDT:USDT | below_1h_threshold | +2.36% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
