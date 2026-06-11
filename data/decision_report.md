# Decision Report

- generated_at: 2026-06-11T14:40:52.120313+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6359**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6359, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.02% | **+0.02%** |
| LIMIT_ATR | 12/20 | 60.0% | -0.01% | **-0.01%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.10% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.24% | **+0.68%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.97% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.66** / 初期 $100.00 (+49.66%)
- 確定: 1279件 (Win 324 / Loss 404 / Flat 551) / skip 1641件
- 成長率目線: 平均log +0.000315 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $149.66

## 4. Latest Market Context

- 更新: 2026-06-11T14:40:45.539797+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=62855.6
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1, 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +95.82% | $85,876,994.66 |
| H/USDT:USDT | +79.75% | $27,577,020.90 |
| BEAT/USDT:USDT | +60.51% | $245,590,150.28 |
| AIO/USDT:USDT | +60.30% | $8,921,773.77 |
| COLLECT/USDT:USDT | +53.47% | $2,373,578.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.37% | +4.66% |
| SPACE/USDT:USDT | below_1h_threshold | +3.92% | +4.20% |
| AIO/USDT:USDT | below_1h_threshold | +3.19% | +3.48% |
| PYTH/USDT:USDT | below_1h_threshold | +3.16% | +3.45% |
| CRV/USDT:USDT | below_1h_threshold | +3.14% | +3.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
