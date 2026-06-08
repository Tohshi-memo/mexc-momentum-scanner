# Decision Report

- generated_at: 2026-06-08T06:56:03.785961+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6040**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=6040, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.17% | **+1.17%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.19% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.02% | **+0.67%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1457件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T06:55:59.763227+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=62960.1
- Funnel: target 773 → liquid 142 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.1 >= 65=1, 4h RSI 68.9 >= 65=1, 4h RSI 73.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +43.79% | $106,726,118.52 |
| ALLO/USDT:USDT | +36.06% | $38,757,168.26 |
| PIPPIN/USDT:USDT | +27.15% | $9,180,861.82 |
| ESPORTS/USDT:USDT | +23.41% | $7,227,475.99 |
| BANK/USDT:USDT | +16.98% | $5,177,302.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +4.16% | +3.81% |
| NEAR/USDT:USDT | below_1h_threshold | +4.05% | +3.70% |
| BANK/USDT:USDT | below_1h_threshold | +2.75% | +2.39% |
| HYPE/USDT:USDT | below_1h_threshold | +2.61% | +2.25% |
| ZEC/USDT:USDT | below_1h_threshold | +2.60% | +2.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
