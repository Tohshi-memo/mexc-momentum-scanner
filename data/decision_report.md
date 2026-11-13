# Decision Report

- generated_at: 2026-11-13T01:06:28.231974+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18772**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=18772, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.71% | **+0.26%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.35% | **+0.32%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +1.06% | **+0.21%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.39% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,721.94** / 初期 $100.00 (+1621.94%)
- 確定: 7243件 (Win 2087 / Loss 2321 / Flat 2835) / skip 8090件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,721.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$395.20** / 初期 $100.00 (+295.20%)
- 確定: 4791件 (Win 1289 / Loss 1063 / Flat 2439) / skip 7392件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0215 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $395.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6932件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T01:06:14.500261+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.46% price=70771.9
- Funnel: target 1105 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOR/USDT:USDT | +67.27% | $1,308,061.42 |
| BARD/USDT:USDT | +51.66% | $6,295,766.63 |
| ARIA/USDT:USDT | +30.22% | $8,486,295.59 |
| GANG/USDT:USDT | +17.69% | $1,007,443.22 |
| PLAY/USDT:USDT | +12.17% | $1,552,620.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.85% | +3.31% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.46% | +1.92% |
| GANG/USDT:USDT | below_1h_threshold | +1.30% | +1.77% |
| ARIA/USDT:USDT | below_1h_threshold | +1.30% | +1.77% |
| CBRSSTOCK/USDT:USDT | below_1h_threshold | +1.09% | +1.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
