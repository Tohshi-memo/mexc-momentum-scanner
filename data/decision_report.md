# Decision Report

- generated_at: 2026-09-05T20:21:15.980292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13774**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=13774, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.21% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.05% | **+0.03%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| MARKET_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$854.65** / 初期 $100.00 (+754.65%)
- 確定: 5080件 (Win 1523 / Loss 1657 / Flat 1900) / skip 5255件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $854.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.33** / 初期 $100.00 (+87.33%)
- 確定: 2519件 (Win 701 / Loss 596 / Flat 1222) / skip 4666件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0236 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $187.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.42** / 初期 $100.00 (+19.42%)
- 確定: 2391件 (Win 709 / Loss 908 / Flat 774) / pending 2件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.42

## 6. Latest Market Context

- 更新: 2026-09-05T20:21:05.886254+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79715.1
- Funnel: target 1050 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SUSHI/USDT:USDT | +23.70% | $2,727,766.52 |
| ARB/USDT:USDT | +22.65% | $35,591,436.56 |
| 4/USDT:USDT | +20.09% | $24,822,560.63 |
| UAI/USDT:USDT | +13.80% | $4,378,541.54 |
| UNI/USDT:USDT | +12.77% | $49,688,599.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.60% | +4.61% |
| UAI/USDT:USDT | below_1h_threshold | +3.06% | +3.07% |
| OP/USDT:USDT | below_1h_threshold | +2.55% | +2.56% |
| 4/USDT:USDT | below_1h_threshold | +2.13% | +2.13% |
| CRV/USDT:USDT | below_1h_threshold | +1.99% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
