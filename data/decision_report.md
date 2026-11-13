# Decision Report

- generated_at: 2026-11-13T06:56:27.646915+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18793**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=18793, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.84% | **+0.75%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.09% | **+1.88%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.71% | **+1.62%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.17% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,748.08** / 初期 $100.00 (+1648.08%)
- 確定: 7263件 (Win 2093 / Loss 2327 / Flat 2843) / skip 8091件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,748.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$402.81** / 初期 $100.00 (+302.81%)
- 確定: 4812件 (Win 1298 / Loss 1069 / Flat 2445) / skip 7392件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0400 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $402.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6955件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000177 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T06:56:09.769237+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.29% price=68994.9
- Funnel: target 1105 → liquid 153 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BARD/USDT:USDT | +53.84% | $11,050,859.44 |
| AKE/USDT:USDT | +50.42% | $10,224,390.84 |
| ARIA/USDT:USDT | +39.21% | $9,463,113.78 |
| KOR/USDT:USDT | +33.63% | $1,746,069.26 |
| GANG/USDT:USDT | +18.65% | $1,195,475.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_relative_strength | +6.13% | +4.83% |
| ZRO/USDT:USDT | below_1h_threshold | +4.96% | +3.66% |
| NEAR/USDT:USDT | below_1h_threshold | +4.26% | +2.96% |
| BARD/USDT:USDT | below_1h_threshold | +3.80% | +2.50% |
| STRK/USDT:USDT | below_1h_threshold | +3.77% | +2.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
