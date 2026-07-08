# Decision Report

- generated_at: 2026-07-08T00:31:26.770165+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8460**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=8460, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.59% | **+0.69%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.62% | **+0.24%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.33% | **+0.21%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | -0.28% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$101.56** / 初期 $100.00 (+1.56%)
- 確定トレード: 70件 (TP 24 / SL 45 / EXP 1)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.56
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.75** / 初期 $100.00 (+219.75%)
- 確定: 2665件 (Win 847 / Loss 898 / Flat 920) / skip 2356件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $319.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1230件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T00:31:10.694046+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=63571.6
- Funnel: target 847 → liquid 171 → pre 50 → checked 50 → surge 6 → strict 5
- Surge前reject: below_1h_threshold=43, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +38.50% | $47,106,733.94 |
| AGLD/USDT:USDT | +16.56% | $1,457,411.67 |
| EDGE/USDT:USDT | +15.09% | $13,334,717.02 |
| US/USDT:USDT | +9.08% | $6,562,879.19 |
| SPELL/USDT:USDT | +8.71% | $2,834,421.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_relative_strength | +5.21% | +4.83% |
| SPELL/USDT:USDT | below_1h_threshold | +4.58% | +4.20% |
| DRAM/USDT:USDT | below_1h_threshold | +4.16% | +3.78% |
| VVV/USDT:USDT | below_1h_threshold | +4.06% | +3.68% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.23% | +2.85% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
