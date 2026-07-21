# Decision Report

- generated_at: 2026-07-21T03:41:28.210056+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9148**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=9148, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.50%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.97% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.44% | **+1.30%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.14% | **+0.92%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.05% | **+0.79%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$108.05** / 初期 $100.00 (+8.05%)
- 確定トレード: 125件 (TP 44 / SL 76 / EXP 5)
- 最新: KIOXIASTOCK/USDT:USDT SL_HIT PnL -3.51% 残高後 $108.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$417.16** / 初期 $100.00 (+317.16%)
- 確定: 3210件 (Win 1006 / Loss 1021 / Flat 1183) / skip 2499件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $417.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.45** / 初期 $100.00 (+30.45%)
- 確定: 1109件 (Win 292 / Loss 229 / Flat 588) / skip 1450件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1051 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.26** / 初期 $100.00 (+1.26%)
- 確定: 339件 (Win 120 / Loss 150 / Flat 69) / pending 2件 / skip 281件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000282 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.26

## 6. Latest Market Context

- 更新: 2026-07-21T03:41:22.422168+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=65499.9
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +74.85% | $2,650,076.46 |
| JIMOTHY/USDT:USDT | +29.77% | $2,857,722.45 |
| ZHIPUSTOCK/USDT:USDT | +22.98% | $1,504,288.58 |
| BLESS/USDT:USDT | +14.79% | $2,155,888.89 |
| ON/USDT:USDT | +13.15% | $2,108,646.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.45% | +3.27% |
| ON/USDT:USDT | below_1h_threshold | +3.42% | +3.25% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +3.03% | +2.85% |
| KORU/USDT:USDT | below_1h_threshold | +2.97% | +2.80% |
| RE/USDT:USDT | below_1h_threshold | +2.62% | +2.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
