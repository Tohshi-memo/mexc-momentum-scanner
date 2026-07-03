# Decision Report

- generated_at: 2026-07-03T13:54:01.185662+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8161**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.03% / filled 20/20。**
- 全期間 MARKET基準: n=8161, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |
| ASK | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.27% | **+1.02%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.01% | **-0.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.22% | **-0.11%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.44% | **-0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.86% | **-0.37%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$285.14** / 初期 $100.00 (+185.14%)
- 確定: 2482件 (Win 763 / Loss 829 / Flat 890) / skip 2240件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $285.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.84** / 初期 $100.00 (+5.84%)
- 確定: 607件 (Win 146 / Loss 145 / Flat 316) / skip 965件
- 成長率目線: 平均log +0.000094 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0528 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MANA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.23% 残高後 $105.84

## 5. Latest Market Context

- 更新: 2026-07-03T13:53:55.849450+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=62172.2
- Funnel: target 834 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +45.10% | $3,106,664.42 |
| ARPA/USDT:USDT | +29.76% | $5,854,083.68 |
| THE/USDT:USDT | +29.65% | $3,108,249.86 |
| ZKP/USDT:USDT | +26.69% | $5,543,029.67 |
| BLESS/USDT:USDT | +25.43% | $7,145,280.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +4.39% | +4.03% |
| SPX/USDT:USDT | below_1h_threshold | +4.06% | +3.71% |
| BAS/USDT:USDT | below_1h_threshold | +4.01% | +3.66% |
| UAI/USDT:USDT | below_1h_threshold | +3.65% | +3.30% |
| NEAR/USDT:USDT | below_1h_threshold | +2.26% | +1.90% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
