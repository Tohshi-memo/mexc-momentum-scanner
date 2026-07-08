# Decision Report

- generated_at: 2026-07-08T01:32:20.907422+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8462**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=8462, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.59% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.95% | **+0.40%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | -0.16% | **-0.09%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | -0.89% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$102.06** / 初期 $100.00 (+2.06%)
- 確定トレード: 72件 (TP 25 / SL 46 / EXP 1)
- 最新: KORU/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.06
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$319.75** / 初期 $100.00 (+219.75%)
- 確定: 2667件 (Win 847 / Loss 898 / Flat 922) / skip 2356件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KORU/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $319.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1232件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0161 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T01:32:15.721730+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=63403.2
- Funnel: target 847 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +36.78% | $49,464,362.89 |
| EDGE/USDT:USDT | +15.14% | $13,130,941.68 |
| AGLD/USDT:USDT | +13.36% | $2,035,267.65 |
| US/USDT:USDT | +8.78% | $4,377,431.65 |
| SYN/USDT:USDT | +8.30% | $4,357,590.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.25% | +2.54% |
| SYN/USDT:USDT | below_1h_threshold | +1.89% | +2.17% |
| H/USDT:USDT | below_1h_threshold | +1.52% | +1.81% |
| XTZ/USDT:USDT | below_1h_threshold | +1.02% | +1.30% |
| APE/USDT:USDT | below_1h_threshold | +0.77% | +1.05% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
